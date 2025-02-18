# 📚 PiDiF GPT

PiDiF GPT is a very basic Streamlit-based chatbot that allows users to interact with their PDFs using natural language. It processes PDFs, extracts their content, and enables a conversational AI experience.&#x20;

## 🚀 Features

- Upload and process multiple PDFs.
- Ask questions about the content.
- Interactive chat interface.
- Uses vector search for efficient retrieval.

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ayoobzz/Chat-PDF.git
cd Chat-PDF
```

### 2. Create a virtual environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

## ▶️ Usage

Run the application with:

```bash
streamlit run app.py
```

Then, open the provided URL in your browser.

## 📄 How It Works

1. Upload PDFs via the sidebar.
2. Click **Process** to extract text and generate embeddings.
3. Start asking questions about the content in the chat input.

