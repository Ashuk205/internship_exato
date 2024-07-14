import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    try:
        # Open the PDF file
        pdf_document = fitz.open(r"C:\Users\ashut\Downloads\AAYUSHI.pdf")
        
        # Initialize an empty string for the text
        text = ""
        
        # Iterate over each page
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# Example usage
file_path = r"C:\path\to\your\pdf_file.pdf"  # Use raw string to avoid unicode errors
pdf_text = extract_text_from_pdf(file_path)
print(pdf_text)
