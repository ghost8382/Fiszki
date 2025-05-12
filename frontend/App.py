import streamlit as st
import requests

st.title("Flashcard AI")
file = st.file_uploader("Upload a PDF", type=["pdf"])
if file:
    with st.spinner("Processing..."):
        response = requests.post("http://localhost:5000/upload", files={"file": file})
        flashcards = response.json()
    for card in flashcards:
        with st.expander(card['question']):
            st.write(card['answer'])