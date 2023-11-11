import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def main():

    st.set_page_config(page_title='PDFchat')
    st.header("PDFChat ")
    st.text_input("Ask any Questions regarding your PDF")

    with st.sidebar:
     st.subheader("Only PDF files are supported")
     st.file_uploader("Upload your PDF's here")
     st.button("Process")


if __name__ == '__main__':
    main()
