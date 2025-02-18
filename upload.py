import streamlit as st
import os

# File upload directory
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Streamlit UI
title = "Odyssey File Upload System"
st.set_page_config(page_title=title, layout="wide")

# Custom styling
st.markdown("""
    <style>
        body { font-family: 'Roboto', sans-serif; background-color: #f3f4f6; }
        .main-header { background-color: #1e3a8a; padding: 20px; color: white; text-align: center; }
        .container { max-width: 600px; margin: auto; padding: 20px; background-color: white; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); }
        .button { background-color: #1e3a8a; color: white; padding: 10px 15px; border: none; border-radius: 5px; }
        .button:hover { background-color: #2563eb; }
    </style>
""", unsafe_allow_html=True)

st.markdown(f'<div class="main-header"><h1>{title}</h1></div>', unsafe_allow_html=True)

st.subheader("Upload and Manage Your Files")

# File Upload UI
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

# Display uploaded files
st.subheader("Uploaded Files")
uploaded_files = os.listdir(UPLOAD_DIR)
if uploaded_files:
    for file_name in uploaded_files:
        file_path = os.path.join(UPLOAD_DIR, file_name)
        st.write(f"📂 {file_name}")
        with open(file_path, "rb") as file_data:
            st.download_button(label=f"Download {file_name}", data=file_data, file_name=file_name, mime="application/pdf")
else:
    st.info("No files uploaded yet.")
