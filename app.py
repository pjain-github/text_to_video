import streamlit as st
from typing import List
from blog_generator import blog_generator
import os
from dotenv import load_dotenv

load_dotenv()

# Get the API key and CSE ID from environment variables
allowed_password = os.getenv('APP_PASSWORD')

# Streamlit UI
st.title("Software Information Blog Generator")

# Login Page
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.subheader("Login")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if password==allowed_password:
            st.session_state["logged_in"] = True
            st.session_state["password"] = password
            st.rerun()
        else:
            st.error("Please enter correct password")
else:

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()

    # Creating layout
    col1, col2, col3 = st.columns([3, 1, 3])

    # Inputs
    with col1:
        software_name = st.text_input("Software Name", "")
    with col2:
        num_sites = st.selectbox("Number", list(range(2, 11)), index=3)
    with col3:
        websites_input = st.text_area("List of Websites (Comma-separated)", "")

    # Process websites input
    websites = [site.strip() for site in websites_input.split(",") if site.strip()]

    # Generate button
    if st.button("Generate Blog"):
        if not software_name:
            st.error("Please enter a software name.")
        else:
            blog_content = blog_generator(software_name, sites=websites, num=num_sites)
            st.markdown(blog_content, unsafe_allow_html=True)