from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFPlumberLoader
from langchain.embeddings import HuggingFaceEmbeddings

# Load pdf file from data path
loader = DirectoryLoader('data', glob="*.pdf", loader_cls=PDFPlumberLoader)
documents = loader.load()

# Split the text from PDF into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Load embeddings model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})

# Build FAISS vector store
vector_store =  FAISS.from_documents(texts, embeddings)
vector_store.save_local('vectorstore/db_faiss')