import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

def fetch_transcript(video_id):
    api = YouTubeTranscriptApi()
    transcript_list = api.fetch(video_id, languages=["en"])

    # Convert to plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)

    return transcript


def create_vector_store(transcript):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])

    vector_store = FAISS.from_documents(chunks, embeddings)

    return vector_store


video_id=input("Enter video id: ")

transcript=fetch_transcript(video_id)

vector_store=create_vector_store(transcript)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2)

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

while True:
    ques=input("Enter question to ask: ")

    if ques != "":
      result=main_chain.invoke(ques)
      print(result,"\n\n-------------------------------------------------------------------")
    else:
       break