import streamlit as st
import os
from phi.agent import Agent
from phi.model.cohere import CohereChat  # Using the Cohere model for Phi.Agent

# Set your API keys (for testing, replace with actual environment variable management in production)
os.environ["COHERE_API_KEY"] = "API_KEY"

# Initialize Phi.Agent with Cohere model
agent = Agent(
    model=CohereChat(id="command-r-plus"),  # Make sure to use the correct Cohere model ID
    markdown=True,
)

st.set_page_config(page_title="Recipe Generator", page_icon="🍽️")

st.title("AI Recipe Generator")
st.write("Enter ingredients and get a recipe powered by Cohere and Phi!")

# User input for ingredients
ingredients = st.text_input("Enter ingredients (comma-separated):", "")

if st.button("Generate Recipe"):
    if ingredients.strip() == "":
        st.warning("Please enter some ingredients.")
    else:
        with st.spinner("Generating recipe..."):
            # Generate recipe using the Phi.Agent powered by Cohere
            prompt = f"Generate a recipe using the following ingredients: {ingredients.strip()}. Provide the recipe name, ingredients, preparation steps, and cooking instructions."
            response = agent.print_response(prompt)

        st.subheader("Your Recipe:")
        st.write(response)  # Display the response from Phi.Agent (recipe)
