# 🧠 Local AI Assistant with Context-Aware Summarization and Snippet Highlighting

A lightweight, locally-hosted GenAI assistant built to run under **4GB VRAM**, powered by **LLaMA 3.1 1B Instruct**, **Chroma**, and **Nomic Text Embeddings**. Supports intelligent document understanding, contextual memory, auto-summarization, and snippet highlighting — all without sending your data to the cloud.

Demo Video Link : ```https://youtu.be/w4jVvcEBtjU```

---

## 🚀 Features

- 🔗 **Text Generation:** Powered by **LLaMA 3.2 1B Instruct**, hosted locally via **LM Studio**
- 📚 **Vector Store:** Uses **Chroma** for efficient retrieval of relevant document chunks
- 🔍 **Embeddings:** Utilizes **Nomic-Embedding v1.5** model for high-quality semantic similarity
- 📄 **Auto Summary:** Automatically generates a summary when a document is uploaded
- 💬 **Context Memory:** Maintains conversational context across interactions
- ✨ **Snippet Highlighting:** Shows the most relevant parts of the documents in the responses
- 🖥️ **Low Resource Friendly:** Optimized to run on setups with **< 4GB VRAM**
- 🛡️ **Privacy First:** All models and vector DB are hosted **locally**

---

## 📁 Installation

- 🔹 Clone this repository:
  ```
  git clone https://github.com/your-username/local-ai-assistant.git
  cd local-ai-assistant
  ```
- 🔹 Run the following commands:
  ```
  python -m venv venv
  venv\Scripts\activate
  pip install --no-deps -r requirements.txt
  ```
  
- 🔹 Download and Install LM Studio:
  1.  Download LM studio: ```https://installers.lmstudio.ai/win32/x64/0.3.17-11/LM-Studio-0.3.17-11-x64.exe```
  2.  Download and load these models in LM Studio in server mode and make sure the server is running. For example: ```http://127.0.0.1:5000```
     
      ```
      nomic-embed-text-v1.5
      llama-3.2-1b-instruct
      ```
  3. Load these models

- 🔹 To execute the program:
  ```
  python app.py
  ```

---

## 🏛️ Architecture

```mermaid
graph TD

%% Nodes
AskMe["Ask me Anything"]
Gradio["Gradio"]
Langchain["Langchain"]
Nomic["Nomic Text Embed"]
Chroma["ChromaDB"]
LLaMA["LLAMA 3.2 1B<br>Instruct"]
Challenge["Challenge Me"]

%% Edges
Gradio <--> AskMe
Langchain <--> Gradio
Nomic <--> Langchain
Chroma <--> Langchain
Langchain <--> LLaMA
Gradio <--> Challenge
