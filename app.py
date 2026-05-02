import streamlit as st
from summarizer import summarize_text

st.title("🧠 AI Text Summarizer")

text = st.text_area("Enter your text here")

if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)