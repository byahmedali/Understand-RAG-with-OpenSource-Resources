# ATS Assistant

ATS Assistant is a Streamlit-based application that demonstrates Retrieval Augmented Generation (RAG) by answering questions about Advanced Telecom Services (ATS), a USA-based company. The app uses a local [Ollama](https://ollama.com/) model for embeddings and a [Groq](https://console.groq.com/docs/quickstart) LLM model for response generation.

## Purpose

The purpose of this repository is to showcase a practical implementation of how Retrieval Augmented Generation (RAG) works. It serves as an educational tool and a starting point for developers interested in building similar AI-powered question-answering systems. By focusing on a specific company (ATS), it demonstrates how RAG can be applied to create a specialized knowledge assistant.

## Features

- Chat-based interface for asking questions about ATS
- Uses RAG to provide context-aware answers
- Displays the augmented query, retrieved context, and LLM response for transparency

## Prerequisites

- Python 3.8 or higher (project was created using Python 3.12.2)
- [Ollama](https://ollama.com/) (for local embeddings)
- [Groq API key](https://console.groq.com/docs/quickstart)

## Setup Instructions

1. **Clone the repository**

   ```
   git clone https://github.com/byahmedali/Understand-RAG-with-OpenSource-Resources understand-RAG
   cd understand-RAG
   ```

2. **Set up a virtual environment**

   a. Create a new virtual environment:
   ```
   python -m venv venv
   ```

   b. Activate the virtual environment:
   
   For Linux/macOS:
   ```
   source venv/bin/activate
   ```
   
   For Windows:
   ```
   venv\Scripts\activate.bat
   ```

   c. Confirm you're using the newly created environment:
   
   If you see environment name `(venv)` at the beginning of your command prompt, it confirms that you're using the newly created virtual environment.

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Install and set up Ollama**

   a. Visit the [Ollama website](https://ollama.com/) and download the appropriate version for your operating system.
   
   b. Install Ollama following the instructions for your OS.
   
   c. Once installed, run the following command to download the required embedding model:
   
   ```
   ollama pull nomic-embed-text
   ```

   This will download the [nomic-embed-text](https://ollama.com/library/nomic-embed-text) model, which is a lightweight and high-performing open embedding model with a large token context window.

5. **Set up environment variables**

   Set up your Groq API key as an environment variable. Run these commands in your terminal or command prompt:

   For Linux/macOS:
   ```
   export GROQ_API_KEY=your_groq_api_key_here
   ```

   For Windows:
   ```
   set GROQ_API_KEY=your_groq_api_key_here
   ```

   Alternatively, you can create a `.env` file in the project root directory and add the following line:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

   You can obtain your Groq API key from the [Groq Console](https://console.groq.com/docs/quickstart).

## Running the Application

1. Ensure Ollama is running in the background. You can start it by running the `ollama` command in a separate terminal window.

2. Run one of the Streamlit apps:

   For the RAG-enabled chat:
   ```
   streamlit run rag_chat_assistant.py
   ```

   For the simple chat without RAG:
   ```
   streamlit run simple_chat_assistant.py
   ```

3. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

Note: The `simple_chat_assistant.py` file provides a basic chat interface without any RAG implementation, while `rag_chat_assistant.py` implements RAG for enhanced context-based responses.

## Usage

1. Choose the app you want to run:
   - `rag_chat_assistant.py`: This app uses Retrieval Augmented Generation (RAG) to answer questions about Advanced Telecom Services (ATS).
   - `simple_chat_assistant.py`: This app provides a basic chat interface without RAG, useful for understanding the LLM's capabilities without additional context.

2. For the RAG-enabled chat (rag_chat_assistant.py):
   - The app will display a chat interface where you can ask questions about ATS.
   - Type your question in the input box and press Enter.
   - The assistant will provide an answer based on the retrieved context.
   - You can view the augmented query, including the system prompt, user query, retrieved context, and LLM response below the chat interface for each interaction.

3. For the simple chat (simple_chat_assistant.py):
   - The app will display a basic chat interface.
   - Type your question or message in the input box and press Enter.
   - The assistant will respond based solely on its pre-trained knowledge, without additional context.

## Troubleshooting

- If you encounter issues with Ollama, make sure it's running and accessible at `http://localhost:11434`.
- If you get API errors, check that your Groq API key is correctly set in the `.env` file or environment variables.
- For any other issues, please check the console output for error messages and ensure all dependencies are correctly installed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Additional Resources

- [Groq Documentation](https://console.groq.com/docs/quickstart)
- [Ollama GitHub Repository](https://github.com/ollama/ollama)
- [Nomic-embed-text Model Information](https://ollama.com/library/nomic-embed-text)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)