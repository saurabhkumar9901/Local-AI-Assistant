import os
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyMuPDFLoader, TextLoader

def create_pdf_chunk(file):
        filename = os.path.basename(file)
        if filename.endswith(".pdf"):
            text_splitter = CharacterTextSplitter(chunk_size = 2000, chunk_overlap = 500)
            loader = PyMuPDFLoader(file)
            docs = loader.load()
            chunks = text_splitter.split_documents(docs)

            for idx, chunk in enumerate(chunks):
                chunk.metadata["id"] = f"{filename}_{idx}"

            return chunks
        
        elif filename.endswith(".txt"):
            text_splitter = CharacterTextSplitter(chunk_size = 2000, chunk_overlap = 500)
            loader = TextLoader(file)
            docs = loader.load()
            chunks = text_splitter.split_documents(docs)
            
            for idx, chunk in enumerate(chunks):
               chunk.metadata["id"] = f"{filename}_{idx}"
            
            return chunks
        
def create_pdf_chunk_qna(file):
        filename = os.path.basename(file)
        if filename.endswith(".pdf"):
            text_splitter = CharacterTextSplitter(chunk_size = 2000, chunk_overlap = 500)
            loader = PyMuPDFLoader(file)
            docs = loader.load()
            chunks = text_splitter.split_documents(docs)

            for idx, chunk in enumerate(chunks):
                chunk.metadata["id"] = f"{filename}_{idx}"

            return chunks
        
        elif filename.endswith(".txt"):
            text_splitter = CharacterTextSplitter(chunk_size = 2000, chunk_overlap = 500)
            loader = TextLoader(file)
            docs = loader.load()
            chunks = text_splitter.split_documents(docs)

            for idx, chunk in enumerate(chunks):
              chunk.metadata["id"] = f"{filename}_{idx}"
              
            return chunks