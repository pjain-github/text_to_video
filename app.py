import streamlit as st
from typing import List
from blog_generator import blog_generator

# Streamlit UI
st.title("Software Information Blog Generator")

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