import fitz  # PyMuPDF

def pdf_to_markdown(pdf_path, md_path):
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)

        # Create or overwrite the Markdown file
        with open(md_path, 'w', encoding='utf-8') as md_file:
            for page_num, page in enumerate(doc, start=1):
                text = page.get_text()  # Extract text from the page
                md_file.write(f"# Page {page_num}\n\n{text}\n\n---\n")
        
        print(f"Markdown file created successfully: {md_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
pdf_to_markdown("csts.pdf", "output.md")