from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import PyPDF2
import streamlit as st
import os

# Function to interact with Gemini AI
def prompt(user_query, memory):
    # Securely load API Key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("API Key not found! Set GEMINI_API_KEY environment variable.")

    # Load the model
    model = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-1.5-pro")

    # Define Prompt Template
    idea = PromptTemplate(
        input_variables=["query", "history"],
        template="""
        You are a mental health expert named Garuda, created by TechSyndicate.
        Conversational History: {history}
        
        Current Query: {query}
        
        Provide a thoughtful response based on the user's history and current query.
        Do not make it obvious that you are an AI. Understand human emotions.
        """
    )

    # Create LLM Chain
    chain = LLMChain(llm=model, prompt=idea, memory=memory)

    # Load conversation history
    hist = memory.load_memory_variables({})

    # Invoke the model
    response = chain.invoke({"query": user_query, "history": hist.get("history", "")})

    return response["text"]

# Function to read PDFs and store content in memory
def pdf_builder(file, memory):
    reader = PyPDF2.PdfReader(file)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text() or ""  # Avoid NoneType errors

    # Store extracted text in AI memory
    memory.chat_memory.add_ai_message(text.strip())

# Streamlit Application
def main():
    st.sidebar.title("Upload Documents to Train")
    st.sidebar.write("Upload PDF files to train Garuda:")

    # Session memory setup
    if "mem" not in st.session_state:
        st.session_state.mem = ConversationBufferMemory(memory_key="history")

    mem = st.session_state.mem

    # Upload PDF section
    files = st.sidebar.file_uploader("Choose PDFs", type=["pdf"], accept_multiple_files=True)
    btn = st.sidebar.button("Compile")

    if btn and files:
        for file in files:
            pdf_builder(file, mem)
        st.sidebar.success("Update complete ✅")

    # Main chat interface
    st.write("### Garuda V1.0")
    st.write("Enter your queries, I am here to help!")

    user_input = st.text_input("Message Garuda:")
    btn_generate = st.button("Generate")

    if user_input and btn_generate:
        response_text = prompt(user_input, mem)

        # Display response
        st.write(response_text)

        # Display memory (debugging)
        st.write("Conversation History:", mem.load_memory_variables({}))

# Run Streamlit app
if __name__ == "__main__":
    main()
