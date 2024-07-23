import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder,FewShotChatMessagePromptTemplate,PromptTemplate
from langchain.chains import create_sql_query_chain
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from operator import itemgetter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
import streamlit as st
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base



def fun(qsn,messages):
    url = "https://2c973bea-6822-482e-bf52-28a6d940865e.us-east4-0.gcp.cloud.qdrant.io"
    api_key = "1Yz0UmYsyshSCbiaecoeFPkN5LMd3H43B172CjegPVTfBfb6F9AG6w"
    collection_name = "text2sql-fewshorts"
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    os.environ["GOOGLE_API_KEY"] = "AIzaSyB3agIfT4SIYKO42VPIiJ8_M5ANlEY2eq0"
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = "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"
    os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'Bearer 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'



    def gemini():
        return ChatGoogleGenerativeAI(model="gemini-pro")

    def connect_db():
        db=SQLDatabase.from_uri("sqlite:///database.db")
        return db 

    def process_query(query):
        tmp=query.replace("```", "").strip()
        idx=tmp.find("SELECT")
        str=tmp[idx:]
        return str

    def ans_prompt():
        x=PromptTemplate.from_template(
        """Given the following user question, corresponding SQL query, and SQL result, answer the user question.
        Question: {question}
        SQL Query: {query}
        SQL Result: {result}
        Answer: """
        )
        return x;

    def fs_prompt():
        x=ChatPromptTemplate.from_messages(
        [
            ("human", "{input}\nSQLQuery:"),
            ("ai", "{query}"),
        ]
        )
        return x
    
    def create_history(messages):
        history=ChatMessageHistory()
        for message in messages:
            if message["role"]=="user":
                history.add_user_message(message["content"])
            else :
                history.add_ai_message(message["content"])
        return history




    llm = gemini()
    db = connect_db()





    answer_prompt = ans_prompt()
    example_prompt =fs_prompt()



   
    client = QdrantClient(url=url, api_key=api_key)
    qdrant = Qdrant(client, collection_name, embeddings)
    example_selector = qdrant.similarity_search(qsn,k=5)


    formatted_examples = [
        {"input": example.metadata["input"], "query": example.metadata["query"]}
        for example in example_selector
    ]



    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=example_prompt,
        examples=formatted_examples,
        input_variables=["input","top_k","table_info"]
    )


    system_msg="You are a MySQL expert. Given an input question, create a syntactically correct MySQL query to run. Unless otherwise specificed.\n\nHere is the relevant table info: {table_info}\n\nBelow are a number of examples of questions and their corresponding SQL queries."

    history =create_history(messages)



    final_prompt = ChatPromptTemplate.from_messages(
        [
            few_shot_prompt,
            MessagesPlaceholder(variable_name="messages"),
            ("human", system_msg+"{input}"),

        ]
    )

    


    generate_query = create_sql_query_chain(llm, db,final_prompt)
    execute_query = QuerySQLDataBaseTool(db=db)

    rephrase_answer = answer_prompt | llm | StrOutputParser()

    chain = (
        RunnablePassthrough.assign(query=generate_query)
        .assign(query=lambda d: {"query": process_query(d["query"])})
        .assign(result=itemgetter("query") | execute_query)
        | rephrase_answer
    )
    
   
      
    suf="and in your first query response  give me just sql query i don't want title or other because this query directly exclued on database without any preprosesing that's way"
    response = chain.invoke({"question":qsn+"."+suf,"messages":history.messages})
    history.add_user_message(qsn)
    history.add_ai_message(response)

    return response

def create_tables():
    Base = declarative_base()
    engine = create_engine("sqlite:///database.db")
    Base.metadata.create_all(engine)




if __name__ == '__main__':
    create_tables()
    
    if "messages" not in st.session_state:
        st.session_state.messages=[]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
        

    if prompt:=st.chat_input("what's up"):

        st.session_state.messages.append({"role":"user",
                                          "content":prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Generating response..."):
            with st.chat_message("assistant"):
                response=fun(prompt,st.session_state.messages)
                st.markdown(response)
        st.session_state.messages.append({"role":"assistant","content":response})
