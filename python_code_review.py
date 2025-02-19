import streamlit as st
import google.generativeai as genai
import os

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f5f5;
        color: #333;
    }
    .stTitle {
        color: #3498db;
        font-size: 40px;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        display: inline-block;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set up API key
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    st.error("API Key is missing. Please set the environment variable 'GENAI_API_KEY'.")
else:
    genai.configure(api_key=api_key)

    # Define system prompt for Gemini AI
    system_prompt = """You are an expert Python code reviewer..."""

    # Initialize the Generative Model
    model = genai.GenerativeModel("gemini-pro")  # Make sure you're using a valid model name

    # Streamlit App UI
    st.title("🚀 Python Code Reviewer")

    # Input for Python code
    user_code = st.text_area("Paste your Python code here:")

    if st.button("🔍 Review Code"):
        if user_code.strip():
            try:
                with st.spinner("Reviewing your code... ⏳"):
                    response = model.generate_content(user_code)
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please paste some Python code first!")

    st.sidebar.header("Instructions")
    st.sidebar.markdown("""
    1. Paste your Python code in the text box.
    2. Click **Review Code** to see the review.
    """)

