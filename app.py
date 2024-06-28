import streamlit as st
import openai
from openai import OpenAI

# Streamlit app setup
st.set_page_config(page_title="NVIDIA AI Chat App", page_icon="🤖")

# Login function
def check_password():
    def password_entered():
        if st.session_state["password"] == "your_password":
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Enter password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Enter password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        return True

# Main app
if check_password():
    st.title("AI Chat App")

    # Sidebar for adjustments
    st.sidebar.header("Adjust Parameters")
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2, 0.1)
    max_words = st.sidebar.number_input("Max Words", 1, 1000, 200)

    # Input for user prompt
    user_prompt = st.text_area("Enter your prompt:", height=100)

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

    # Disclaimer
    st.sidebar.markdown("---")
    st.sidebar.warning("Disclaimer: This AI model may produce inaccurate information. Use the generated content responsibly and verify important information.")

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
    st.warning("Please enter the correct password to access the app.")
