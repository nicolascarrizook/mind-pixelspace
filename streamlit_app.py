import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/generate_meditation"

st.title("mind.")
st.caption("Generate personalized meditation sessions")

prompt = st.text_area("Enter your intention for the meditation session:", height=150)

immersion_options = ["relaxation", "focus", "sleep"]
immersion = st.selectbox("Select the type of immersion for your session:", immersion_options)

voice_options = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
voice = st.radio("Select the voice for your session:", voice_options)

session_durations = [5, 10, 15, 20]  # Duraciones disponibles en minutos
session_duration = st.radio("Select the session duration (minutes):", session_durations)


if st.button("Generate Meditation Session"):
    with st.spinner('Wait while your meditation session is being generated...'):
        response = requests.post(API_URL, json={"prompt": prompt, "immersion": immersion, "voice": voice, "duration": session_duration})
        
        if response.status_code == 200:
            data = response.json()
            audio_path = data.get("audio_file_path")
            cover_image_path = data.get("cover_image_path")  # Obtener la ruta de la imagen de portada de la respuesta
            
            st.success("Meditation session successfully generated.")
            st.audio(audio_path)
            
            if cover_image_path:
                # Si es una ruta de archivo local, necesitas asegurarte de que Streamlit pueda acceder a ella
                # o, si estás trabajando localmente, podría ser necesario convertir la ruta a una URL o mover el archivo a un directorio accesible
                st.image(cover_image_path, caption="Meditation Session Cover")
        else:
            st.error("Error generating the meditation session. Please try again.")
