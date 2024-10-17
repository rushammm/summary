import streamlit as st
from transformers import pipeline

# Load the Hugging Face summarization model
model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=model_name)

# Streamlit UI
st.title("Text Summarization App")
st.write("Enter the text you want to summarize:")

# Input text area
input_text = st.text_area("Text", height=300)

# Button to generate summary
if st.button("Summarize"):
    if input_text:
        # Generate summary
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        st.write("### Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
