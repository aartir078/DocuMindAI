# DocuMind AI 🤖

### AI Chatbot for General Questions, PDFs, and Websites

DocuMind AI is an AI-powered chatbot that answers general questions and helps users find information from uploaded PDF documents and website content. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information and generate useful answers using a locally running AI model.

## ✨ Features

- **General AI Chat:** Ask questions and get answers using a local language model.
- **PDF Question Answering:** Upload PDF documents and ask questions about their content.
- **Website Question Answering:** Enter a website URL to process its text and ask questions about it.
- **Local AI Model:** Uses Ollama to run the language model locally.
- **Document Retrieval:** Uses ChromaDB to store and retrieve relevant text chunks.
- **Simple Web Interface:** Built with Flask, HTML, and CSS.

## 🛠️ Technologies Used

- Python
- Flask
- Ollama
- Llama 3.2 (3B)
- ChromaDB
- Nomic Embed Text
- PyPDF
- BeautifulSoup
- HTML and CSS

## 📂 Project Structure

```text
DocuMindAI/
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── uploads/
└── chroma_db_ollama/
```

*Note: The `uploads/` and `chroma_db_ollama/` folders are created locally when needed and are excluded from GitHub.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/aartir078/DocuMindAI.git
cd DocuMindAI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bat
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and start Ollama

Download Ollama from [ollama.com](https://ollama.com/).

Download the required models:

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

Ensure Ollama is running before starting the application.

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000

## 🚀 How to Use

1. Start the DocuMind AI web application.
2. Ask a general question in the chat interface.
3. Upload a PDF or enter a website URL to process its content.
4. Ask questions about the processed information.
5. Read the generated answer and view the available source references.

## 🔮 Future Improvements

- Support for more document formats.
- Improved source citations and answer accuracy.
- Conversation history.
- Better document management.
- Enhanced user interface and mobile responsiveness.

## 👨‍💻 Project Information

**Project Name:** DocuMind AI  
**Project Type:** AI Chatbot / Retrieval-Augmented Generation (RAG)  
**Purpose:** To make information retrieval from documents and websites easier using AI.

## 📄 License

This project is currently intended for learning and educational purposes.
