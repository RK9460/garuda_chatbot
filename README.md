# Garuda Mental Health Chatbot

Garuda is an AI-powered chatbot designed to provide mental health support. It uses **Google Gemini AI** via **LangChain** and can also process PDFs for enhanced interactions. Built with **Streamlit**, it offers a simple web interface for user interaction.

## Features
- **AI Chatbot**: Powered by Google Gemini AI (via LangChain).
- **Conversational Memory**: Retains chat history for context-aware responses.
- **PDF Processing**: Users can upload PDFs to train the bot on custom data.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.

---

## Installation

### 1️⃣ **Clone the Repository**
```bash
git clone <repository_url>
cd chatbot
```

### 2️⃣ **Create and Activate Virtual Environment**
```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set API Key** (Google Gemini AI)
Create an environment variable for security:
```bash
export GOOGLE_GENAI_API_KEY="your-api-key-here"  # Linux/macOS
set GOOGLE_GENAI_API_KEY=your-api-key-here  # Windows
```

---

## Usage

### Run the Streamlit App
```bash
python -m streamlit run main.py
```

### Upload PDFs
- Click on **"Upload Documents to Train"** in the sidebar.
- Select PDF files to train the chatbot on additional knowledge.
- Click **"Compile"** to process uploaded files.

### Chat with Garuda
- Enter your message in the text input field.
- Click **"Generate"** to receive AI-powered responses.

---

## Project Structure
```
chatbot/
│── main.py             # Streamlit chatbot application
│── requirements.txt    # List of required Python packages
│── README.md           # Project documentation
│── venv/               # Virtual environment (optional)
```

---

## Dependencies
The chatbot requires the following Python packages:
```
streamlit
langchain
langchain-google-genai
PyPDF2
```
Install them via:
```bash
pip install -r requirements.txt
```

---

## License
This project is developed by **SIN Technologies**. Use it responsibly!

