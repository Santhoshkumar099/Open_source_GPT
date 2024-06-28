import streamlit as st
import openai
from openai import OpenAI

# Streamlit app setup
st.set_page_config(page_title="AI Chat App", page_icon="🤖")

# User registration and verification
def user_auth():
    if "username" not in st.session_state:
        st.session_state.username = None
        st.session_state.verified = False

    if not st.session_state.username:
        username = st.text_input("Create a username:")
        if username:
            st.session_state.username = username
            st.success(f"Username '{username}' created successfully!")
            st.info("Please verify your username on the next step.")
            st.experimental_rerun()
    
    elif not st.session_state.verified:
        verify_username = st.text_input("Verify your username:")
        if st.button("Verify"):
            if verify_username == st.session_state.username:
                st.session_state.verified = True
                st.success("Username verified successfully!")
                st.experimental_rerun()
            else:
                st.error("Username verification failed. Please try again.")
    
    return st.session_state.verified

# Main app
if user_auth():
    st.title(f"Welcome to AI Chat App, {st.session_state.username}!")

    # Sidebar for adjustments
    st.sidebar.header("Adjust Parameters")
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2, 0.1)
    max_words = st.sidebar.number_input("Max Words", 1, 1000, 200)

    # Input for user prompt
    user_prompt = st.text_area("Enter your prompt:", height=100)


    # Disclaimer
    st.sidebar.markdown("---")
    st.sidebar.warning("Disclaimer: This AI model may produce inaccurate information. Use the generated content responsibly and verify important information.")

    if st.button("Generate Response"):
        # Suggestions
        st.sidebar.header("Prompt Suggestions")
        suggestions = [
            "GUVI was founded by",
            "GUVI is a",
            "Tell me about GUVI"
        ]
        selected_suggestion = st.sidebar.selectbox("Try a suggestion:", suggestions)
    if st.sidebar.button("Use Suggestion"):
        user_prompt = selected_suggestion
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
   
else:
    st.info("Please create and verify your username to access the app.")
