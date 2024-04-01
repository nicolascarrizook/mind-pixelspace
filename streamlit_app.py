import streamlit as st
import requests

st.title("mind.")
st.caption("Generate personalized meditation sessions")

API_URL = st.text_input("Enter the API URL:", value="http://127.0.0.1:5000/generate_meditation")

prompt = st.text_area("Enter your intention for the meditation session:", height=150)

# Reemplazar esto con un text_area
immersion = st.text_area("Enter the type of immersion for your session:", height=50)

voice_options = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
voice = st.radio("Select the voice for your session:", voice_options)

session_durations = [5, 10, 15, 20] 
session_duration = st.radio("Select the session duration (minutes):", session_durations)

if st.button("Generate Meditation Session"):
    with st.spinner('Wait while your meditation session is being generated...'):
        response = requests.post(API_URL, json={"prompt": prompt, "immersion": immersion, "voice": voice, "duration": session_duration})
        
        if response.status_code == 200:
            data = response.json()
            audio_path = data.get("audio_file_path")
            cover_image_path = data.get("cover_image_path")
            
            st.success("Meditation session successfully generated.")
            st.audio(audio_path)
            
            if cover_image_path:
                st.image(cover_image_path, caption="Meditation Session Cover")
        else:
            st.error("Error generating the meditation session. Please try again.")
