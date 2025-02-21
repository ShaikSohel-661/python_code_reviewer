import streamlit as st
import google.generativeai as genai
import os

import streamlit as st  # Missing import statement
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyD1tUU_qj7R9rsk13hjND9P7FfLJCYf1TA")


# Initialize the model
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")  # Or "gemini-2.0-flash"

# Streamlit UI
st.title("🕵🏽‍♂️ Python Code Reviewer")
st.write("Submit your Python code for review and get bug reports & fixes!")

# User Input
code_input = st.text_area("Paste your Python code here:", height=200)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Reviewing your code... ⏳"):
            user_prompt = f"""
            You are a professional Python code reviewer.
            - Analyze the following Python code for **errors, inefficiencies, and improvements**.
            - Provide a **bug report** with explanations.
            - Give a **fully corrected version** of the code.

            Here is the user's code:
            ```python
            {code_input}
            ```

            Please return the response in **Markdown format** with:
            - A "Bug Report" section listing errors and explanations.
            - A "Fixed Code" section containing the corrected Python code inside a Markdown block.
            """
            response = model.generate_content(user_prompt)

            st.subheader("🔍 AI Code Review Report")
            st.markdown(response.text) 

    else:
        st.warning("⚠️ Please enter Python code before submitting.")
