import streamlit as st
from PIL import Image

# st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
#
# st.markdown("""
# <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
#   <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Data Professor</a>
#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#   </button>
#   <div class="collapse navbar-collapse" id="navbarNav">
#     <ul class="navbar-nav">
#       <li class="nav-item active">
#         <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank">YouTube</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank">Twitter</a>
#       </li>
#     </ul>
#   </div>
# </nav>
# """, unsafe_allow_html=True)

st.set_page_config(layout="wide")

st.markdown("""
<style>
.header {
    font-size:60px !important;
}
#subheader {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="header">Empower Business With Data</p>', unsafe_allow_html=True)
st.markdown('<p id="subheader"> Strategy + Data + Execution </p>')

profile = Image.open()




pic , intro = st.columns([2,1])
with pic:
    st.image(profile, use_column_width='auto')


st.header('Create Business Solution with the Power of Data')
st.write('')

st.write('[Create](https://share.streamlit.io/martinesk/personal-projects/main/ML-Web-App/MLWebAppFramework.py)')
st.header('other shit')
st.slider('somehting',0,100)
st.markdown('https://share.streamlit.io/martinesk/personal-projects/main/ML-Web-App/MLWebAppFramework.py', unsafe_allow_html=1)



col1 , col2 = st.columns([2,1])
with col1:
    st.header('Facial Recognition')

with col2:
    st.header('ML Dashboard')