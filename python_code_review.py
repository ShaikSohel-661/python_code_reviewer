import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv  

load_dotenv()

api_key = os.getenv("AIzaSyD1tUU_qj7R9rsk13hjND9P7FfLJCYf1TA")

if not api_key:
    st.error("❌ API Key is missing. Please set the environment variable 'GENAI_API_KEY' in a .env file.")
else:
    genai.configure(api_key=api_key)


system_prompt = """You are an expert Python code reviewer with deep knowledge of best practices, debugging, optimization, and clean coding standards. Your task is to carefully analyze the provided Python code, identifying potential errors, inefficiencies, and areas for improvement.

Provide a structured response that includes:

- **Code Analysis**: Summary of the code's functionality.
- **Error Detection**: Identify syntax errors, logical errors, and runtime issues.
- **Performance Optimization**: Suggestions for improving efficiency.
- **Best Practices**: Recommendations on readability, maintainability, and security.
- **Final Rating**: Score out of 5 based on quality and correctness.

Only accept Python code as input. If the input is not valid Python code, politely reject it and request a valid submission."""

# Initialize AI model
try:
    gemini = genai.GenerativeModel(
        model_name="models/gemini-1.5-pro-latest",
        system_instruction=system_prompt
    )
except Exception as e:
    st.error(f"❌ Error initializing AI model: {e}")

# Streamlit UI
st.title("🚀 Python Code Reviewer")
st.write("Enter your Python code snippet for review.")

# Text input for user
user_prompt = st.text_area("📌 Enter your Python code:", height=250)

# Button to process the code
if st.button("🔍 Review Code"):
    if user_prompt.strip():
        try:
            with st.spinner("Reviewing your code... ⏳"):
                response = gemini.generate_content(user_prompt, stream=True)
            
            # Display AI Review
            st.subheader("✅ AI Review:")
            for chunk in response:
                st.write(chunk.text)
        except Exception as e:
            st.error(f"❌ An error occurred while fetching the review: {e}")
    else:
        st.warning("⚠️ Please enter a Python code snippet first.")

# Sidebar Instructions
st.sidebar.header("📌 Instructions")
st.sidebar.markdown("""
1. Paste your Python code in the text area.
2. Click 'Review Code'.
3. View the AI-generated review feedback.
""")

