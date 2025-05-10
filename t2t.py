import streamlit as st
import cohere
import os
# Initialize Cohere client (replace with your actual API key)
api_key = 'API_KEY'  # Replace with your real key
co = cohere.Client(api_key)

st.set_page_config(page_title="Text-to-Text Generator with Cohere")
st.title("📝 Text-to-Text Generator (Cohere)")

# User input
prompt = st.text_area("Enter your prompt here:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating..."):
            try:
                # Use Cohere's `generate()` method with a supported model
                response = co.generate(
                    model='command-xlarge',  # Use 'command-xlarge' model
                    prompt=prompt,
                    max_tokens=300,
                    temperature=0.7
                )
                # Display the response
                st.subheader("✍️ AI Response:")
                st.write(response.generations[0].text.strip())
            except cohere.errors.BadRequestError as e:
                st.error(f"Error generating text: {e}")
    else:
        st.error("Please enter some text to generate a response.")
