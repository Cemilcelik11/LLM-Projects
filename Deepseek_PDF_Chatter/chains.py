import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from dotenv import load_dotenv
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""

load_dotenv()


class Chain:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vector_store = InMemoryVectorStore(embedding=self.embeddings)
        self.llm = ChatGroq(
            temperature=0, 
            groq_api_key=os.getenv("GROQ_API_KEY"), 
            model_name="deepseek-r1-distill-llama-70b")
        self.prompt_template = ChatPromptTemplate.from_template(template)
        self.pdfs_directory = './pdfs/'

    def upload_pdf(self, file):
        os.makedirs(self.pdfs_directory, exist_ok=True)
        with open(os.path.join(self.pdfs_directory, file.name), "wb") as f:
            f.write(file.getbuffer())

    def load_pdf(self, file_name):
        loader = PDFPlumberLoader(os.path.join(self.pdfs_directory, file_name))
        documents = loader.load()

        return documents

    def split_text(self, documents):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
    )
    
        return text_splitter.split_documents(documents)

    def index_docs(self, documents):
        self.vector_store.add_documents(documents)

    def retrieve_docs(self, query):
        return self.vector_store.similarity_search(query)

    def answer_question(self, question, documents):
        context = "\n\n".join([doc.page_content for doc in documents])
        chain = self.prompt_template | self.llm

        return chain.invoke({"question": question, "context": context}).content


    
