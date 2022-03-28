import streamlit as st
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from PIL import Image

json_file = open('./bart-simpson-text-generator/model.json', 'r')
loaded_json_model = json_file.read()
json_file.close()

loaded_model = model_from_json(loaded_json_model)

loaded_model.load_weights('./bart-simpson-text-generator/model.h5')

with open('./bart-simpson-text-generator/bart-chalkboard-data.txt','r',encoding='utf-8') as file:
    data = file.read()

def generate_text(model,tokenizer,max_length,seed_text,n_words):
    text_generated = seed_text
    for i in range(n_words):
        encoded = tokenizer.texts_to_sequences([text_generated])[0]

        encoded = pad_sequences([encoded],maxlen=max_length,padding='pre')

        yhat = model.predict(encoded,verbose=0)

        #normalize = [round(x) for x in yhat[0]]

        predicted_word = ''
        for word, index in tokenizer.word_index.items():

            if index == yhat.any():
                predicted_word = word
                break
        text_generated += ' ' + predicted_word

    return text_generated

tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
max_length = 67

st.title('The Simpsons Chalkboard Gag Text Generator.')

image = Image.open('./bart-simpson-text-generator/1.jpeg')
st.image(image, use_column_width=True)

n_words = st.number_input('Type the number of words you want to generate', min_value=1)
seed_text = st.text_input('Type a word or words you want to generate after')

if n_words and seed_text:
    st.header(generate_text(loaded_model,tokenizer,max_length,seed_text,int(n_words)))
else:
    st.warning('Please input a word and a number')

#print(generate_text(loaded_model,tokenizer,max_length,'how',2))