from openai import OpenAI
from langchain_core.embeddings import Embeddings

client = OpenAI(base_url="http://127.0.0.1:5000/v1/", api_key="lm-studio")

class CustomEmbedding(Embeddings):
    def embed_documents(self, texts):
        embeddings = [get_embedding(text) for text in texts]
        return embeddings

    def embed_query(self, text):
        embedding = get_embedding(text)
        return embedding

def get_embedding(text, model="text-embedding-nomic-embed-text-v1.5"):
    return client.embeddings.create(input=[text], model=model).data[0].embedding