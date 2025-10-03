import streamlit as st

# Title and subtitle
st.title("🚀 My First Streamlit App")
st.header("Hello, Streamlit!")
st.write("This is my very first Streamlit program.")

# User input
name = st.text_input("Enter your name:")

# Button to display greeting
if st.button("Say Hello"):
    st.success(f"Hello, {name}! Welcome to Streamlit. 🎉")
