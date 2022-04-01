import streamlit as st
from PIL import Image



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
#image_face img{
    width:300px;
    display: inline-block;
    margin-left:100px;
    
}
#video_face img{
    width:300px;
    display: inline-block;
    margin-left:100px;
}
.ds_showcase{
    
    color:grey;

}
#pro_pic{
    margin-left=1000px;

}

#DS-showcase img{
    width:800px;
    display: inline-block;
    margin-left:100px;

}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="header">Empower Business With Data</p>', unsafe_allow_html=True)
st.markdown('<p id="subheader"> Strategy + Data + Execution </p>', unsafe_allow_html=True)


st.header("  ")
st.header(" ")

pic ,spacer, intro = st.columns([3,1,8])
with pic:
    #st.image("https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/IMG_3565.png", width=200)
    st.markdown('<div>'                
                '<img id=pro_pic src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/IMG_3565.png" width="200px" >'
               
                '</div>'
                , unsafe_allow_html=1)
    st.header(' ')
    st.markdown('<div>'
                '<a id="img-git" href="https://github.com/martinesk/Personal-Projects">'
                '<img src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/GitHub-Mark-Light-120px-plus.png" width="30px" height="30px">'
                '</a>'
                '<a style="align"     href="https://www.linkedin.com/in/ding-ma-0b5781110/">'
                '<img src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/LI-In-Bug.png" width="30px" height="30px">'
                '</a>'

                '</div>'
                , unsafe_allow_html=1)
    st.header(' ')
    st.markdown("""

        I love travel around the world and also fascinated by the endless possibilities of what a business can achieve.

        I started my business ventures early in my life. After a couple early successes I started to help other businesses, regardless of sizes, with their oversea expansions with my good friends and partners around the world. 

        Not long after my study in Foster MBA at UW, I realized the power of big data and the astonishing things you can achieve by leveraging those state of art Machine Learning and Deep Learning models.
        Combining years of internation business strategy and execution experiences with the insights from big data, I serve my clients with insightful business strategy, big data analysis and firm execution planning.

        Current based in 📍Los Angeles with clients in 📍London 📍Dubai 📍Shanghai 📍Beijing 📍Seattle 📍New York.   University of Washington alumni. 


        """)


with intro:
    st.markdown("<h1 style= 'right-align '>DS/ML Selected Work Portfolio</h1>", unsafe_allow_html=True)

    st.markdown("<h1 class='ds_showcase'>"
                "<a href='http://52.15.187.123:5000/' style='color:grey'>"
                "Video Facial/Emotional Recognition"
                "</a>"
                "</h1>", unsafe_allow_html=True)



    st.markdown('<div>'
                '<a id="video_face" href="http://52.15.187.123:5000/">'
                '<img src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/Capture4.png" >'
                '</a>'

                '</div>'
                , unsafe_allow_html=1)

    st.markdown("<h1 class='ds_showcase'>"
                "<a href='https://share.streamlit.io/martinesk/personal-projects/main/image_facial_emotion_rec/streamlit_imgfacerec_main.py' style='color:grey'>"
                "Static Facial Feature Recognition"
                "</a>"
                "</h1>", unsafe_allow_html=True)

    st.markdown('<div>'
                '<a id="image_face" href="https://share.streamlit.io/martinesk/personal-projects/main/image_facial_emotion_rec/streamlit_imgfacerec_main.py">'
                '<img src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/Figure_5.png" >'
                '</a>'

                '</div>'
                , unsafe_allow_html=1)


    st.markdown("<h1 class='ds_showcase'>"
                "<a href='https://share.streamlit.io/martinesk/personal-projects/main/Data-Science-Web-App/TrafficDashBoard.py' style='color:grey'>"
                "Data Mining Showcase"
                "</a>"
                "</h1>", unsafe_allow_html=True)

    st.markdown('<div>'
                '<a id="DS-showcase" href="https://share.streamlit.io/martinesk/personal-projects/main/Data-Science-Web-App/TrafficDashBoard.py">'
                '<img src="https://raw.githubusercontent.com/martinesk/Personal-Projects/main/pic/DS-showcase.png" >'
                '</a>'

                '</div>'
                , unsafe_allow_html=1)



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




st.header(" ")



st.header(" ")
st.markdown("<h1 id='consult_intro'>More About International Business Consulting: <a id='consult_link' href='https://www.pioneerunion.com/'>"
                            'https://www.pioneerunion.com'
                        '</a>''</h1>', unsafe_allow_html=True)


















