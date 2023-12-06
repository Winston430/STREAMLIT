import streamlit as st
from app.db import DB

def register_page():
    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if username and password:
            # Send data to backend for user creation
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            st.success("Registration successful!")
        else:
            st.error("Please fill in all fields.")

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username and password:
            # Send data to backend for user authentication
            # Implement login logic here
            st.success("Login successful!")
        else:
            st.error("Please fill in all fields.")

page = st.sidebar.selectbox("Page", ["Register", "Login"])

if page == "Register":
    register_page()
elif page == "Login":
    login_page()
