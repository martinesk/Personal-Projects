import streamlit as st
from ImageFacialRec import *

with open('http://52.15.187.123/KeyPointDetector.json', 'r') as json_file:
    json_SavedModel = json_file.read()
model = tf.keras.models.model_from_json(json_SavedModel)
model.load_weights('http://52.15.187.123/weights.hdf5')
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