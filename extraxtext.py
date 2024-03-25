import pdfplumber
from PyPDF2 import PdfWriter, PdfReader

def split_pdf_on_word_occurrence(pdf_file, output_prefix, split_word):
    # Open the PDF file
    with pdfplumber.open(pdf_file) as pdf:
        # Iterate over each page in the PDF
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            # Check if the split word occurs in the page text
            if split_word in text:
                # Create a new PDF containing pages up to the current page
                with open(pdf_file, "rb") as f:
                    reader = PdfReader(f)
                    # Create a new PDF writer object
                    writer = PdfWriter()
                    count = len(reader.pages)
                    # Iterate through pages up to the current page
                    for j in range(i + 1):
                        # Get the page from the reader and add it to the writer
                        writer.add_page(reader.pages[j])
                    output_file = f"{output_prefix}_{i + 1}.pdf"
                    with open(output_file, "wb") as out_f:
                        writer.write(out_f)
                    print(f"PDF split at page {i + 1}. Output saved as {output_file}")

# Example usage:
pdf_file = "Formal_Letters.pdf"  # Specify the path to your input PDF file
output_prefix = "output_"  # Specify the prefix for output files
split_word = "Subject:"  # Specify the word to split on

split_pdf_on_word_occurrence(pdf_file, output_prefix, split_word)
