
import streamlit as st
from pypdf import PdfWriter
merger = PdfWriter()
pdfs=[]
st.set_page_config(page_title="PDF Uploader", page_icon="📄")

st.title("📄 Drag & Drop PDF")
st.write("Upload a PDF file using drag and drop.")

uploaded_files = st.file_uploader("Upload PDF", type="pdf",accept_multiple_files=True)

if uploaded_files:  # Check if files are uploaded
    for uploaded_file in uploaded_files:
        if not uploaded_file.name.endswith(".pdf"):
            file_name = f"{uploaded_file.name}.pdf"
        else:
            file_name = uploaded_file.name
        pdfs.append(uploaded_file)

for pdf in pdfs:
    merger.append(pdf)
if st.button("Merge PDFs"):
    if pdfs:
        merger.write("merged-pdf.pdf")
        merger.close()
        st.success("PDFs merged successfully! Download the merged PDF below.")
        st.download_button(
            label="Download Merged PDF",
            data=open("merged-pdf.pdf", "rb").read(),
            file_name="merged-pdf.pdf",
            mime="application/pdf"
        )
    else:
        st.error("No PDFs to merge.")








