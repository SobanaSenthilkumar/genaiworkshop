import os
import streamlit as st
from phi.agent import Agent
from phi.model.cohere import CohereChat  # Assuming you're using Cohere for responses

# Set your Cohere API key (use environment variables or hardcode it)
os.environ["COHERE_API_KEY"] = "API_KEY"

# Initialize the Phi Agent with Cohere model
agent = Agent(
    model=CohereChat(id="command-xlarge"),  # Using the correct Cohere model ID
    markdown=True,
)

# Example function to interact with Phi and get a response
def phi_response(prompt):
    return agent.print_response(prompt)

# Streamlit Web Interface
st.title('Phi Model Response')
prompt = st.text_input("Enter your prompt:", "What are in these images? Is there any difference between them?")

if prompt:
    response = phi_response(prompt)
    st.subheader("Phi Model Response")
    st.write(response)
