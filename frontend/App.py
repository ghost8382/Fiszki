import streamlit as st
import requests

st.title("Flashcard AI")
file = st.file_uploader("Upload a PDF", type=["pdf"])

if file:
    with st.spinner("Processing..."):
        try:
            response = requests.post("http://localhost:5000/upload", files={"file": file})


            try:
                flashcards = response.json()
                for card in flashcards:
                    with st.expander(card['question']):
                        st.write(card['answer'])

            except Exception as e:
                st.error(f"❌ Błąd dekodowania JSON: {e}")
                flashcards = []
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Błąd połączenia: {e}")
