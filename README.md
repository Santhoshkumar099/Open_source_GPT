# AI Chat App

This Streamlit-based application provides an interface for users to interact with NVIDIA's AI model, allowing them to generate responses based on custom prompts.

## Features

- Simple username-based access
- Customizable AI parameters (temperature and max words)
- Real-time streaming of AI responses
- Clean and intuitive user interface

## Requirements

To run this app, you need:

- Python 3.7+
- Streamlit
- OpenAI Python library
- Valid NVIDIA API key

## Installation
  Install the required packages

## Usage

1. Run the Streamlit app:
      streamlit run app.py
2. Open the provided local URL in your web browser.

3. Enter a username when prompted.

4. In the main interface:
- Adjust the temperature and max words parameters in the sidebar if desired.
- Enter your prompt in the text area.
- Click "Generate Response" to get the AI's reply.

## Customization

- Modify the `get_username()` function to implement more complex authentication if needed.
- Adjust the model parameters in the `client.chat.completions.create()` call to fine-tune the AI's behavior.

## Disclaimer

This application uses an AI model which may produce inaccurate or biased information. Users should verify important information and use the generated content responsibly.

## Deploying to Streamlit Cloud

1. Push your code to a GitHub repository.
2. Visit https://share.streamlit.io/ and connect your GitHub account.
3. Select your repository and the main file (app.py).
4. Add your NVIDIA API key as a secret in the Streamlit Cloud dashboard.

## License

[Specify your license here, e.g., MIT, GPL, etc.]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any problems or have any questions, feel free to contact me 
