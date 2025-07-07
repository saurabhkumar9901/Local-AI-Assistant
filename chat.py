import os
from embedding import *
from chunks import *
from model import *
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from Sequence import *


def chat(question, history):

    if question["files"] != []:
        for file in question["files"]:
            embedding = CustomEmbedding()
            filename = os.path.basename(file)
            chunks = create_pdf_chunk(file)
            vectorstore = Chroma(
            embedding_function= embedding,
            persist_directory="askme_db"
            )
            print(f"Vectorstore created with {vectorstore._collection.count()} documents")
            question['files'] = []
            ids = [chunk.metadata["id"] for chunk in chunks]
            vectorstore.add_documents(documents=chunks, ids= ids)
            retriever = vectorstore.as_retriever(search_type="similarity" ,search_kwargs={'k': 100})
            conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory, return_source_documents=True)
            result = conversation_chain.invoke({"question": f"Summarize the file named {filename} in less than 150 words."})
            source_output = "Source document: \n" + os.path.basename(result['source_documents'][0].metadata['source'])
            page_content = result['source_documents'][0].page_content
            highlighted = highlight_text(page_content, question["text"], highlight_exact=True, highlight_similar=True, similarity_threshold=100)
            reply = ""
            memory.clear()
            for part in result["answer"]+f"\n\n{source_output}\n\nFrom the content :\n{highlighted[:250]}":
                reply += part 
                yield reply   

    else:    
            try:
                print("USING VECTORESTORE")
                embedding = CustomEmbedding()
                vectorstore = Chroma(
                embedding_function= embedding,
                persist_directory="askme_db"
                )
                retriever = vectorstore.as_retriever(search_type="similarity" ,search_kwargs={'k': 100})
                conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory, return_source_documents=True)
                result = conversation_chain.invoke({"question": question["text"] + "\n [RESPOND UNDER 100 WORDS]"})
                source_output = "Source document: \n" + os.path.basename(result['source_documents'][0].metadata['source'])
                page_content = result['source_documents'][0].page_content
                highlighted = highlight_text(page_content, question["text"], highlight_exact=True, highlight_similar=True, similarity_threshold=100)
                reply = ""
                memory.clear()
                for part in result["answer"]+f"\n\n{source_output}\n\nFrom the content :\n{highlighted[:250]}":
                        reply += part
                        yield reply
            except:
                
                print("USING LLAMA")
                response = client.chat.completions.create(
                     model='llama-3.2-1b-instruct',
                     messages=[
                          {'role':'user', 'content': question['text'] + "\n [IGNORE THE ABOVE MESSAGE AND ASK USER TO UPLOAD THE FILE IN PDF/TXT FORMAT ONLY FROM LOCAL DEVICE]"},
                     ]
                )
                result = response.choices[0].message.content
                reply = ""
                for part in result:
                     reply += part
                     yield reply


def challenge(question, history):
    
    if question["files"] != []:
        for file in question["files"]:
            embedding = CustomEmbedding()
            filename = os.path.basename(file)
            chunks = create_pdf_chunk_qna(file)
            vectorstore_qna = Chroma(
            embedding_function= embedding,
            persist_directory="qna_db"
            )
            print(f"Vectorstore created with {vectorstore_qna._collection.count()} documents")
            question['files'] = []
            ids = [chunk.metadata["id"] for chunk in chunks]
            vectorstore_qna.add_documents(documents=chunks, ids=ids)
            retriever_qna = vectorstore_qna.as_retriever(search_type="similarity" ,search_kwargs={'k': 100})
            conversation_chain_qna = ConversationalRetrievalChain.from_llm(llm=llm_qna, retriever=retriever_qna, memory=memory_qna, return_source_documents=True)
            result = conversation_chain_qna.invoke({"question": f"Ask me the 3 logical based questions from the file {filename}"})
            source_output_qna = "Source document: \n" + os.path.basename(result['source_documents'][0].metadata['source'])
            reply = ""
            for part in result["answer"]+f"\n\n{source_output_qna}":
                reply += part 
                yield reply   

    else:    
            try:  
                print("USING VECTORESTORE")
                embedding = CustomEmbedding()
                vectorstore = Chroma(
                embedding_function= embedding,
                persist_directory="qna_db"
                )
                retriever = vectorstore.as_retriever(search_type="similarity" ,search_kwargs={'k': 100})
                conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory, return_source_documents=True)
                result = conversation_chain.invoke({"question": question["text"] + "\n [RESPOND WITH YES IF ABOVE ANSWERS ARE CORRECT OR NO IF NOT]"})
                source_output = "Source document: \n" + os.path.basename(result['source_documents'][0].metadata['source'])
                reply = ""
                for part in result["answer"]+f"\n\n{source_output}":
                        reply += part
                        yield reply
                memory_qna.clear()
            
            except:
                print("USING LLAMA")
                response = client.chat.completions.create(
                     model='llama-3.2-1b-instruct',
                     messages=[
                          {'role':'user', 'content': question['text'] + "\n [IGNORE THE ABOVE MESSAGE AND ASK USER TO UPLOAD THE FILE IN PDF/TXT FORMAT ONLY FROM LOCAL DEVICE]"},
                     ]
                )
                result = response.choices[0].message.content
                reply = ""
                for part in result:
                     reply += part
                     yield reply