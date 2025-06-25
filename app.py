import streamlit as st
import base64

# Background lagane ka function
def set_bg(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            min-height: 100vh;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Music play karne ka function
def autoplay_music(music_file):
    audio_bytes = open(music_file, "rb").read()
    st.audio(audio_bytes, format='audio/mp3', start_time=0)

# Background Set karo
set_bg("background.jpg")

# Message show karo
st.markdown("<h1 style='text-align: center; color: red;'>❤️ HAPPY 1 YEAR RELATIONSHIP ❤️</h1>", unsafe_allow_html=True)

st.write("""
## Dear Jnuu ❤️

1 YEAR TOGETHER MY LOVE! 🥰  
Tum meri zindagi ki sabse khoobsurat feeling ho.  

Thank you for every smile, every memory, and every loving moment.  

**I Love You Forever ❤️**

- [Your's Reeeeeebbb] 😘
""")

