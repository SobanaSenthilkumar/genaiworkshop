from gtts import gTTS
import os
import streamlit as st

# Streamlit app configuration
st.title("📝 Text to Speech (gTTS)")

# User input text
text = st.text_area("Enter text to convert to speech:")

if st.button("Generate Speech"):
    if text:
        with st.spinner("Generating speech..."):
            # Convert text to speech
            tts = gTTS(text=text, lang='en')
            # Save the audio file
            tts.save("output.mp3")
            
            # Play the audio file
            st.audio("output.mp3", format="audio/mp3")
            st.success("Speech generated and playing!")
    else:
        st.error("Please enter some text to convert to speech.")
