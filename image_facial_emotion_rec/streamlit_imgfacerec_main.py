import streamlit as st

st.set_page_config(layout="wide")
st.markdown("""
<style>
#sec_p{
    color:grey;
}

#stats{
    margin-top: 20px;
    
}

</style>
""", unsafe_allow_html=True)


st.markdown("<h1 >Static Image Facial Feature Recognition "
                        "</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='color:grey' id='sec_p'>This model is too big to display interactively for performance reasons, for more information visit this github repo:"
                "<a href='https://github.com/martinesk/Personal-Projects/tree/main/image_facial_emotion_rec'>"
                    "https://github.com/martinesk/Personal-Projects/tree/main/image_facial_emotion_rec"
                "</a>"
            "</h5>", unsafe_allow_html=True)

st.header(" ")

intro, stats = st.columns(2)
with intro:
    st.subheader("Model Abstract")
    st.write("As CNNs grow deeper, vanishing gradient tend to occur which negatively impact network performance,"
             "Residual Neural Network includes 'skip connection' feature which enables training of 152 layers without vanishing gradient issues"
             "RESNET works by adding 'identity mapping' on top of the CNN"
             "ImageNet containes 11 million images and 11,000 categories"
             "ImageNet is used to train RESNET Deep Neural Network.      "
             "*This is a mini version of the actual working example* ")
with stats:
    st.subheader("Model Stats : ")

    st.markdown("<h6 id='stats'>Model Accuracy: 0.778816 <br>"
                "Model RMSE value: 3.03147 <br>"
                "Total params: 18,016,286 <br>"
                "Trainable params: 18,007,710 <br>"
                "Non-trainable params: 8,576"

                "</h6>", unsafe_allow_html=True)



st.subheader("Model Flowchart :")
col1, col2 = st.columns(2)
with col1:
    st.image("https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/RESNET1.png")
with col2:
    st.image("https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/RESNET2.png")




st.header(" ")

col3, col4 = st.columns(2)
with col3:
    st.header("Trainning Data Examples")
    st.image("https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/Figure_1.png")
with col4:
    st.header("Model Results Example")
    st.image("https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/Figure_2.png")
