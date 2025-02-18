import streamlit as st
import time
import os
import logging
from dotenv import load_dotenv
from utils import get_pdf_text, get_chunks, get_vectorstore, get_conversation_chain
from rich.console import Console
from rich.logging import RichHandler


console = Console()
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True)]
)

def init():
    """Initialize the Streamlit app."""
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        logging.info("GROQ_API_KEY is not set")
        st.warning("GROQ_API_KEY is not set. Please check your environment variables.")
    else:
        logging.info("GROQ_API_KEY is set")
    
    # Setup Streamlit page
    st.set_page_config(
        page_title="Your PiDiF GPT",
        page_icon="📖"
    )
    st.header("Welcome to CHAT PiDiF 📚")

def process_pdf_upload(pdf_docs):
    """Process the uploaded PDFs and set up the conversation chain."""
    with st.spinner("Processing your PDFs..."):
        raw_text = get_pdf_text(pdf_docs)
        chunks = get_chunks(raw_text)
        vectorstore = get_vectorstore(chunks)
        chain = get_conversation_chain(vectorstore)
    st.success("PDFs processed successfully")
    return chain

def handle_input(user_input):
    
    st.session_state.messages.append({"role": "user", "text": user_input})
    if st.session_state.chain:
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.spinner("Thinking..."):
            time.sleep(2)  
            input_data = {
                'question': user_input,
                'chat_history': st.session_state.messages  
            }
            response = st.session_state.chain(input_data)
        answer = response.get('answer', 'No answer provided.')
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "text": answer})
    else:
        st.error("⚠️ Please upload and process a PDF first.")

def clear_chat():
    """Clear the chat history."""
    st.session_state.messages = []
    st.success("Chat cleared.")

def main():
    init()
    
    # Initialize session state variables if they don't exist
    if "chain" not in st.session_state:
        st.session_state.chain = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display previous messages in the chat interface
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["text"])
    

    user_input = st.chat_input("Ask me anything about your PDFs", key="user_input")
    if user_input:
        handle_input(user_input)
        
        
    with st.sidebar:
        st.image("logo.png", width=50)
        st.subheader("Your PDFs 📖")
        pdf_docs = st.file_uploader("Upload your PDFs", accept_multiple_files=True)
        
        if st.button("Process") and pdf_docs:
            st.session_state.chain = process_pdf_upload(pdf_docs)
        
        if st.button("Clear Chat"):
            clear_chat()

if __name__ == "__main__":
    main()
