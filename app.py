import streamlit as st
import openai
from openai import OpenAI

# Streamlit app setup
st.set_page_config(page_title="AI Chat App", page_icon="🤖")

# User registration
def get_username():
    if "username" not in st.session_state:
        username = st.text_input("Enter your username:")
        if username:
            st.session_state.username = username
            return True
    return "username" in st.session_state

# Main app
if get_username():
    st.title(f"Welcome to AI Chat App, {st.session_state.username}!")

    # Sidebar for adjustments
    st.sidebar.header("Adjust Parameters")
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2, 0.1)
    max_words = st.sidebar.number_input("Max Words", 1, 1000, 200)

    # Input for user prompt
    user_prompt = st.text_area("Enter your prompt:", height=100)

    # Disclaimer
    st.markdown("---")
    st.warning("Disclaimer: This AI model may produce inaccurate information. Use the generated content responsibly and verify important information.")

    if st.button("Generate Response"):
        if user_prompt:
            client = OpenAI(
                base_url="https://integrate.api.nvidia.com/v1",
                api_key="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"
            )

            try:
                completion = client.chat.completions.create(
                    model="nvidia/nemotron-4-340b-instruct",
                    messages=[{"role": "user", "content": user_prompt}],
                    temperature=temperature,
                    top_p=0.7,
                    max_tokens=max_words * 4,  # Approximate tokens to words
                    stream=True
                )

                response = ""
                response_container = st.empty()
                for chunk in completion:
                    if chunk.choices[0].delta.content is not None:
                        response += chunk.choices[0].delta.content
                        response_container.markdown(response)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

    # Requirements to run the app
    st.sidebar.markdown("---")
    st.sidebar.header("Requirements")
    st.sidebar.markdown("""
    To run this app, you need:
    - Python 3.7+
    - Streamlit
    - OpenAI Python library
    - Valid NVIDIA API key
    """)
else:
    st.info("Please enter a username to access the app.")
