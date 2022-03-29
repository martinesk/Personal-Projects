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
#img-git{
    margin-right:20px;
    margin-left:50px
}
#consult_link{
    font-size: 40px;
    margin-left:22px;
    color:grey;
}
#consult_intro{
    color:grey;
}
#image_face{
    width=300px;
    height=500px;
}
#video_face{
    width=300px;
    height=500px;
}
.ds_showcase{
    margin-left: 220px;
    color:grey;

}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="header">Empower Business With Data</p>', unsafe_allow_html=True)
st.markdown('<p id="subheader"> Strategy + Data + Execution </p>', unsafe_allow_html=True)

#profile = Image.open("https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/IMG_3565.JPG")


st.header("  ")
st.header(" ")

pic , intro = st.columns([2,5])
with pic:
    st.image("https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/IMG_3565.png", width=200)

with intro:
    st.markdown("""
    
    Hi I'm Ding, 
    
    I'm a seasoned consultant/DS in international trade and business strategy. 
    
    Combining years of internation business insights with state of art big data analysis and deeplearning models, I serve my clients with insightful business strategy, big data analysis and firm execution planning.
    
    Current based in 📍Los Angelos with clients in 📍UK 📍Dubai 📍Shanghai 📍Beijing 📍Seattle 📍New York. University of Washington alumni. 
    
    
    """)


st.markdown('<div>'
                '<a id="img-git" href="https://github.com/martinesk/Personal-Projects">'
                    '<img src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/GitHub-Mark-Light-120px-plus.png" width="30px" height="30px">'
                '</a>'
                '<a style="align"     href="https://www.linkedin.com/in/ding-ma-0b5781110/">'
                    '<img src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/LI-In-Bug.png" width="30px" height="30px">'
                '</a>'
                
            '</div>'
            , unsafe_allow_html=1)
st.header(" ")

if st.button("More about my work"):

    st.header(" ")
    st.markdown("<h1 id='consult_intro'>More About International Business Consulting: <a id='consult_link' href='https://www.pioneerunion.com/'>"
                            'https://www.pioneerunion.com'
                        '</a>''</h1>', unsafe_allow_html=True)
    st.markdown("<h1 style= 'right-align '>DS/ML Selected Work Portfolio</h1>", unsafe_allow_html=True)




    st.markdown("<h1 class='ds_showcase'>"
                    "<a href='http://52.15.187.123:5000/' style='color:grey'>"
                    "Video Facial/Emotional Recognition"
                "</a>"
                "</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='ds_showcase'>"
                "<a href='https://share.streamlit.io/martinesk/personal-projects/main/image_facial_emotion_rec/streamlit_imgfacerec_main.py' style='color:grey'>"
                    "Static Facial Feature Recognition"
                "</a>"
                "</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='ds_showcase'>"
                "<a href='https://share.streamlit.io/martinesk/personal-projects/main/ML-Web-App/MLWebAppFramework.py' style='color:grey'>"
                    "Interactive Machine Learning Web App Framework"
                "</a>"
                "</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='ds_showcase'>"
                "<a href='https://share.streamlit.io/martinesk/personal-projects/main/bart-simpson-text-generator/SimpsonMain.py' style='color:grey'>"
                    "NLP: Text Generation"
                "</a>"
                "</h1>", unsafe_allow_html=True)
    st.markdown("<h1 class='ds_showcase'>"
                "<a href='https://share.streamlit.io/martinesk/personal-projects/main/Data-Science-Web-App/TrafficDashBoard.py' style='color:grey'>"
                    "Data Mining Showcase"
                "</a>"
                "</h1>", unsafe_allow_html=True)











    # st.markdown('<div>'
    #             '<a id="image_face" href="https://share.streamlit.io/martinesk/personal-projects/main/image_facial_emotion_rec/streamlit_imgfacerec_main.py">'
    #             '<img src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/Figure_5.png" >'
    #             '</a>'
    #
    #             '</div>'
    #             , unsafe_allow_html=1)

    # st.markdown('<div>'
    #             '<a id="video_face" href="http://52.15.187.123:5000/">'
    #             '<img src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/Capture4.png" >'
    #             '</a>'
    #
    #             '</div>'
    #             , unsafe_allow_html=1)



