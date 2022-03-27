import pandas as pd
import numpy as np
import copy
import random
import tensorflow as tf
from tensorflow.python.keras import Sequential
from tensorflow.keras import layers, optimizers
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.initializers import glorot_uniform
from tensorflow.keras.utils import plot_model
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint, LearningRateScheduler
from IPython.display import display
from tensorflow.keras import backend as K
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras import optimizers
from sklearn.metrics import mean_squared_error
from math import sqrt

# Load Data
facialpoints_df = pd.read_csv('./Dataset/KeyFacialPoints.csv')
facialpoints_df['Image'] = facialpoints_df['Image'].apply(lambda x: np.fromstring(x, dtype = int, sep=' ').reshape(96,96))



# Data Ploting
fig = plt.figure(figsize=(20,20))
for i in range(16):
    ax = fig.add_subplot(4, 4, i+1)
    plt.imshow(facialpoints_df['Image'][i], cmap='gray')
    for j in range(1,31,2):
        plt.plot(facialpoints_df.loc[i][j-1], facialpoints_df.loc[i][j], 'rx')

plt.show()

# Image Augmentation
facialpoints_df_copy = copy.copy(facialpoints_df)
columns = facialpoints_df_copy.columns[:-1]
facialpoints_df_copy['Image'] = facialpoints_df_copy['Image'].apply(lambda x: np.flip(x, axis = 1))
for i in range(len(columns)):
  if i%2 == 0:
    facialpoints_df_copy[columns[i]] = facialpoints_df_copy[columns[i]].apply(lambda x: 96. - float(x) )
facialpoints_df_augmented = np.concatenate((facialpoints_df,facialpoints_df_copy))

## Augment brightness
facialpoints_df_copy_one = copy.copy(facialpoints_df)
facialpoints_df_copy_one['Image'] = facialpoints_df_copy_one['Image'].apply(lambda x:np.clip(random.uniform(1, 2) * x, 0.0, 255.0))
facialpoints_df_augmented = np.concatenate((facialpoints_df_augmented, facialpoints_df_copy_one))




# Obtain the value of 'Images' and normalize it
# Note that 'Images' are in the 31st column but since indexing start from 0, we refer 31st column by 30
img = facialpoints_df_augmented[:, 30]
img = img/255.

# Create an empty array of shape (10700, 96, 96, 1) to train the model
X = np.empty((len(img), 96, 96, 1))

# Iterate through the normalized images list and add image values to the empty array
# Note that we need to expand it's dimension from (96,96) to (96,96,1)
for i in range(len(img)):
  X[i,] = np.expand_dims(img[i], axis = 2)

# Convert the array type to float32
X = np.asarray(X).astype(np.float32)
X.shape
# Obtain the values of key face points coordinates, which are to used as target.
y = facialpoints_df_augmented[:,:30]
y = np.asarray(y).astype(np.float32)
y.shape
# Split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)


def res_block(X, filter, stage):
    # CONVOLUTIONAL BLOCK
    X_copy = X
    f1, f2, f3 = filter

    # Main Path
    X = Conv2D(f1, (1, 1), strides=(1, 1), name='res_' + str(stage) + '_conv_a',
               kernel_initializer=glorot_uniform(seed=0))(X)
    X = MaxPool2D((2, 2))(X)
    X = BatchNormalization(axis=3, name='bn_' + str(stage) + '_conv_a')(X)
    X = Activation('relu')(X)

    X = Conv2D(f2, kernel_size=(3, 3), strides=(1, 1), padding='same', name='res_' + str(stage) + '_conv_b',
               kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_' + str(stage) + '_conv_b')(X)
    X = Activation('relu')(X)

    X = Conv2D(f3, kernel_size=(1, 1), strides=(1, 1), name='res_' + str(stage) + '_conv_c',
               kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_' + str(stage) + '_conv_c')(X)

    # Short path
    X_copy = Conv2D(f3, kernel_size=(1, 1), strides=(1, 1), name='res_' + str(stage) + '_conv_copy',
                    kernel_initializer=glorot_uniform(seed=0))(X_copy)
    X_copy = MaxPool2D((2, 2))(X_copy)
    X_copy = BatchNormalization(axis=3, name='bn_' + str(stage) + '_conv_copy')(X_copy)

    # Add data from main and short paths
    X = Add()([X, X_copy])
    X = Activation('relu')(X)

    # IDENTITY BLOCK 1
    X_copy = X

    # Main Path
    X = Conv2D(f1, (1, 1), strides=(1, 1), name='res_' + str(stage) + '_identity_1_a',
               kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_' + str(stage) + '_identity_1_a')(X)
    X = Activation('relu')(X)

    X = Conv2D(f2, kernel_size=(3, 3), strides=(1, 1), padding='same', name='res_' + str(stage) + '_identity_1_b',
               kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_' + str(stage) + '_identity_1_b')(X)
    X = Activation('relu')(X)

    X = Conv2D(f3, kernel_size=(1, 1), strides=(1, 1), name='res_' + str(stage) + '_identity_1_c',
               kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_' + str(stage) + '_identity_1_c')(X)

    # Add both paths together (Note that we feed the original input as is hence the name "identity")
    X = Add()([X, X_copy])
    X = Activation('relu')(X)

    # IDENTITY BLOCK 2
    X_copy = X

    # Main Path
    X = Conv2D(f1, (1, 1), strides=(1, 1), name='res_' + str(stage) + '_identity_2_a',
               kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_' + str(stage) + '_identity_2_a')(X)
    X = Activation('relu')(X)

    X = Conv2D(f2, kernel_size=(3, 3), strides=(1, 1), padding='same', name='res_' + str(stage) + '_identity_2_b',
               kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_' + str(stage) + '_identity_2_b')(X)
    X = Activation('relu')(X)

    X = Conv2D(f3, kernel_size=(1, 1), strides=(1, 1), name='res_' + str(stage) + '_identity_2_c',
               kernel_initializer=glorot_uniform(seed=0))(X)
    X = BatchNormalization(axis=3, name='bn_' + str(stage) + '_identity_2_c')(X)

    # Add both paths together (Note that we feed the original input as is hence the name "identity")
    X = Add()([X, X_copy])
    X = Activation('relu')(X)
    return X


input_shape = (96,96,1)

# Input tensor shape
X_input = Input(input_shape)

# Zero-padding
X = ZeroPadding2D((3,3))(X_input)

# Stage #1
X = Conv2D(64, (7,7), strides= (2,2), name = 'conv1', kernel_initializer= glorot_uniform(seed = 0))(X)
X = BatchNormalization(axis =3, name = 'bn_conv1')(X)
X = Activation('relu')(X)
X = MaxPooling2D((3,3), strides= (2,2))(X)

# Stage #2
X = res_block(X, filter= [64,64,256], stage= 2)

# Stage #3
X = res_block(X, filter= [128,128,512], stage= 3)

# Average Pooling
X = AveragePooling2D((2,2), name = 'Averagea_Pooling')(X)

# Final layer
X = Flatten()(X)
X = Dense(4096, activation = 'relu')(X)
X = Dropout(0.2)(X)
X = Dense(2048, activation = 'relu')(X)
X = Dropout(0.1)(X)
X = Dense(30, activation = 'relu')(X)


model = Model( inputs= X_input, outputs = X)
model.summary()

'''
Train the Model
'''
# adam = tf.keras.optimizers.Adam(learning_rate = 0.001, beta_1=0.9, beta_2=0.999, amsgrad=False)
# model.compile(loss="mean_squared_error", optimizer = adam, metrics = ['accuracy'])
# # save the best model with least validation loss
# checkpointer = ModelCheckpoint(filepath = "./weights.hdf5", verbose = 1, save_best_only = True)
# history = model.fit(X_train, y_train, batch_size = 256, epochs= 100, validation_split = 0.05, callbacks=[checkpointer], verbose=2)


'''
Load the results
'''
with open('./Dataset/KeyPointDetector.json', 'r') as json_file:
    json_SavedModel = json_file.read()
model = tf.keras.models.model_from_json(json_SavedModel)
model.load_weights('./Dataset/weights.hdf5')
model.compile(loss="mean_squared_error", optimizer = 'adam', metrics = ['accuracy'])

result = model.evaluate(X_test,y_test)
print("Accuracy : {}".format(result[1]))

df_predict = model.predict(X_test)

rms = sqrt(mean_squared_error(y_test, df_predict))
print("RMSE value : {}".format(rms))
df_predict= pd.DataFrame(df_predict, columns = columns)
df_predict.head()

fig = plt.figure(figsize=(20, 20))

for i in range(8):
    ax = fig.add_subplot(4, 2, i + 1)
    # Using squeeze to convert the image shape from (96,96,1) to (96,96)
    plt.imshow(X_test[i].squeeze(),cmap='gray')
    for j in range(1,31,2):
            plt.plot(df_predict.loc[i][j-1], df_predict.loc[i][j], 'rx')

plt.show()