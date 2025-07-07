from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(temperature=0.1, model_name = "llama-3.2-1b-instruct", base_url= "http://127.0.0.1:5000/v1/", api_key="lm-studio",max_completion_tokens=500)
memory = ConversationBufferMemory(memory_key='chat_history',input_key="question", output_key="answer", return_messages=True) 

llm_qna = ChatOpenAI(temperature=0.1, model_name = "llama-3.2-1b-instruct", base_url= "http://127.0.0.1:5000/v1/", api_key="lm-studio", max_completion_tokens=500)
memory_qna = ConversationBufferMemory(memory_key='chat_history', input_key="question", output_key="answer", return_messages=True) 