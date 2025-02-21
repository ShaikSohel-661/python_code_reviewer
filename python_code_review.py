import streamlit as st
import os
import google.generativeai as genai

# Configure the API key
genai.configure(api_key=os.getenv("AIzaSyD1tUU_qj7R9rsk13hjND9P7FfLJCYf1TA"))

# Initialize the model
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")  # Or "gemini-2.0-flash"

# Streamlit UI
st.title("🕵🏽‍♂️ Python Code Reviewer")
st.write("Review your Python code here to detect bugs and receive suggested fixes!")

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

            # Display AI response with better formatting
            st.subheader("🔍 AI Code Review Report")

            if response.text:
                # Split text and extract code sections
                sections = response.text.split("```python")  

                # Display Bug Report as Markdown
                st.markdown(sections[0], unsafe_allow_html=True)  

                # Display formatted code block if AI response contains one
                if len(sections) > 1:
                    st.code(sections[1].split("```")[0], language="python")  

    else:
        st.warning("⚠️ Please enter Python code before submitting.")
