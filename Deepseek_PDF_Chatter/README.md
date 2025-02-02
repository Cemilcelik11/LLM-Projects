# 📄 PDF Chat Assistant

A conversational AI that answers questions about PDF documents using **deepseek-r1-distill-llama-70b**. DeepSeek-R1-Distill-Llama-70B is a  distilled version of the original model DeepSeek-R1, compressed into a 70-billion-parameter architecture based on Meta's Llama framework.  The distillation process involves training the smaller model to mimic the behavior and reasoning patterns of the larger DeepSeek-R1 model.

## 🚀 Features
- Upload & process PDF documents
- Natural language questioning
- Context-aware answers from document content
- Real-time responses

## 🛠 Tech Stack
| Tool | Purpose |
|------|---------|
| **Streamlit** | Web UI framework for rapid prototyping |
| **LangChain** | LLM orchestration & document processing |
| **Groq API** | Ultra-fast LLM inference engine (deepseek-r1-distill-llama-70b) |
| **Hugging Face** | Sentence transformers for text embeddings |
| **InMemoryVectorStore** | Instant vector similarity search |

## 🔍 How It Works

### PDF Processing Pipeline
1. **Upload** → PDF saved to `./pdfs/` directory
2. **Text Extraction** → `PDFPlumberLoader` parses content
3. **Chunking** → Recursive splitter creates 1000-char segments
4. **Embedding** → MiniLM-L6-v2 converts text to vectors
5. **Indexing** → Stored in in-memory vector store

### Question Answering Flow
1. User asks question
2. Vector store finds relevant text chunks
3. LLM generates answer using context
4. Streamlit displays formatted response

