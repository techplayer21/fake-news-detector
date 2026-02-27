import streamlit as st
import joblib

# Load the saved model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# UI Setup
st.set_page_config(page_title="Fake News Detector", page_icon="🛡️")
st.title("🛡️ Fake News Detection System")
st.markdown("Enter the news article text below to check if it's **Real** or **Fake**.")

# User input
user_input = st.text_area("Paste the news article here:", height=250)

if st.button("Analyze News"):
    if user_input.strip() != "":
        # Process the input text
        data = vectorizer.transform([user_input])
        prediction = model.predict(data)
        
        # MATCHING YOUR NOTEBOOK LOGIC:
        if prediction[0] == 1: 
            st.success("✅ This news article appears to be REAL.")
        else:
            st.error("🚨 Warning: This news article appears to be FAKE.")
    else:
        st.warning("Please enter some text to analyze.")
st.sidebar.info("This project uses Natural Language Processing (NLP) and Logistic Regression to detect misinformation.")