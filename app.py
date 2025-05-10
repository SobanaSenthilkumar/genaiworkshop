import streamlit as st
import os
from langchain_community.chat_models import ChatCohere
from langchain.schema import HumanMessage, SystemMessage

# Set Cohere API key (ensure it's secure for production)
os.environ["COHERE_API_KEY"] = "API_KEY"

# Function to get response from Cohere chat model
def get_cohere_response(question):
    # Create the chat model instance
    chat = ChatCohere(model="command-nightly", temperature=0.5)

    # Send the question with context as an NLP expert
    messages = [
        SystemMessage(content="You are an expert in Natural Language Processing (NLP). Answer all questions related to NLP in detail and in simple terms."),
        HumanMessage(content=question)
    ]
    
    # Get the response from Cohere API (Don't use token_count, just content)
    response = chat(messages)
    
    # Return only the content of the response, which contains the answer
    return response.content

# Streamlit app setup
st.set_page_config(page_title="NLP ChatBot", page_icon="🧠", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 NLP Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Ask anything about Natural Language Processing!</p>", unsafe_allow_html=True)

# Input section with text box and submit button
with st.form("chat_form"):
    input_question = st.text_input("💬 Enter your NLP-related question:")
    submitted = st.form_submit_button("🔍 Get Answer")

# Handle the submission
if submitted and input_question.strip():
    with st.spinner("Thinking... 💡"):
        response = get_cohere_response(input_question)
    st.markdown("### ✅ Answer:")
    st.success(response)
elif submitted:
    st.warning("⚠️ Please enter a valid question.")

# Add example buttons to guide users
st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Or try these:</h3>", unsafe_allow_html=True)
if st.button("📘 What is NLP?"):
    response = get_cohere_response("What is NLP?")
    st.markdown("### ✅ Answer:")
    st.success(response)

if st.button("🔍 What is Tokenization?"):
    response = get_cohere_response("What is Tokenization?")
    st.markdown("### ✅ Answer:")
    st.success(response)

if st.button("📖 What is the difference between Stemming and Lemmatization?"):
    response = get_cohere_response("What is the difference between Stemming and Lemmatization?")
    st.markdown("### ✅ Answer:")
    st.success(response)
