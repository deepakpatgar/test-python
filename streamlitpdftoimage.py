import fitz
import os
import streamlit as st
import tempfile

def convert_pdf_to_images(pdf_content, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(pdf_content.getvalue())

    pdf_document = fitz.open(temp_pdf.name)

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        image = page.get_pixmap()
        image_path = os.path.join(output_folder, f"page_{page_number + 1}.png")
        image.save(image_path)

    pdf_document.close()
    os.unlink(temp_pdf.name)

def main():
    st.title("PDF to Images Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file:
        output_folder = st.text_input("Enter the output folder path:", "")
        if st.button("Convert to Images"):
            if output_folder:
                convert_pdf_to_images(uploaded_file, output_folder)
                st.success("Conversion complete. Check the output folder.")
            else:
                st.error("Please enter the output folder path.")

if __name__ == "__main__":
    main()
