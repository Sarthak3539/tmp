import streamlit as st
from main import fun  

st.title("Text2SQL")

qsn = st.text_input("Question: ")

if qsn:
    response=fun(qsn)
    st.header("answer")
    st.write(response)  
    
