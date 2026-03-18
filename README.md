# YouTube Transcript Q&A with RAG (LangChain + FAISS + Groq)

This project allows you to **ask questions about any YouTube video** by leveraging its transcript. It uses a **Retrieval-Augmented Generation (RAG)** pipeline to fetch relevant transcript chunks and generate accurate answers using an LLM.


## 🚀 Features

* 🔍 Fetches YouTube video transcripts automatically
* ✂️ Splits transcript into manageable chunks
* 🧠 Converts text into embeddings using HuggingFace models
* 📦 Stores embeddings in a FAISS vector database
* 🔎 Retrieves relevant context based on user queries
* 🤖 Uses Groq LLM (LLaMA 3) to answer questions
* 💬 Interactive CLI for continuous Q&A


## 🏗️ Tech Stack

* Python
* LangChain
* FAISS (Vector Store)
* HuggingFace Embeddings
* Groq LLM (LLaMA 3)
* YouTube Transcript API


## 📁 Project Structure

```
.
├── main.py              # Main script
├── .env                # Environment variables (API keys)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```


## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```


### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACE_API_KEY=huggingface_api_token
```


## ▶️ How to Run

Run the script:

```bash
python main.py
```


## 🧪 Usage

1. Enter a **YouTube video ID**
   Example:

   ```
   Enter video id: dQw4w9WgXcQ
   ```

2. Ask questions about the video:

   ```
   Enter question to ask: What is the main topic of the video?
   ```

3. The system will:

   * Retrieve relevant transcript chunks
   * Generate an answer using the LLM

4. To exit, press Enter without typing a question.


## 🔄 How It Works

1. **Transcript Fetching**

   * Uses YouTube Transcript API to extract captions

2. **Text Splitting**

   * Splits transcript into overlapping chunks for better context

3. **Embedding**

   * Converts text into vector embeddings using HuggingFace

4. **Vector Storage**

   * Stores embeddings in FAISS for fast similarity search

5. **Retrieval**

   * Finds top relevant chunks based on the query

6. **Generation**

   * Passes retrieved context to Groq LLM for answering


## ⚠️ Limitations

* Only works if the video has **English transcripts available**
* Answers are limited strictly to transcript content
* No support for multi-language transcripts (yet)


## 💡 Future Improvements

* Add support for multiple languages
* Streamlit / web UI
* Support for multiple videos
* Persistent vector database
* Source citation for answers
