import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

# Initialize Ollama embeddings (Local)
embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)

def load_docs(directory):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    docs = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            if file.lower().endswith('.pdf'):
                loader = PyPDFLoader(file_path)
                pages = loader.load_and_split()
                docs.extend(pages)
            else:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    text = f.read()
                chunks = text_splitter.split_text(text)
                docs.extend(chunks)
    return docs

# Load documents and create vector store
docs = load_docs("./data/")
vectorstore = FAISS.from_texts([doc.page_content for doc in docs], embedding=embeddings)

# Create conversational chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# Streamlit UI
st.title("ATS Assistant")

st.markdown('''This is a simple app to understand how Retrieval Augmented Generation (RAG) works by answering basic questions about a USA based company called Advanced Telecom Services (ATS). It uses a Ollama Local model (nomic-embed-text) for embeddings and a Groq LLM model (llama3-8b-8192) for response generation.''')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What would you like to know about ATS?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        # System prompt to limit response to given context
        system_prompt = "You are a helpful assistant. Please answer the question based only on the information provided in the context. Try to give a detailed response. Important: Avoid sentences like 'Based on the context provided, the answer is...' or 'According to the provided context,'. If the answer is not in the context, say 'I don't have enough information to answer that question.'"

        result = qa_chain({"question": prompt, "chat_history": [(m["role"], m["content"]) for m in st.session_state.messages]})
        response = result['answer']
        message_placeholder.markdown(response)

    # Print Augmented Query information
    st.write("**Augmented Query:**")
    st.write(f"**System Prompt:** {system_prompt}")
    st.write(f"**User Query:** {prompt}")

    # Print retrieved context as part of Augmented Query
    st.write("**Retrieved Context:**")
    if result['source_documents']:
        for i, doc in enumerate(result['source_documents'], 1):
            st.write(f"{i}. {doc.page_content}")
    else:
        st.write("No relevant context found.")

    # Print LLM Response
    st.write("**LLM Response:**")
    st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})