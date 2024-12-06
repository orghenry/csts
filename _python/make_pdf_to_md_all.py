import fitz  # PyMuPDF
import os


def detect_table_blocks(page):
    """
    Detect text blocks on a page that might correspond to a table.

    :param page: A PyMuPDF page object.
    :return: The bounding box (x0, y0, x1, y1) enclosing all detected blocks.
    """
    blocks = page.get_text("blocks")  # Get text blocks as (x0, y0, x1, y1, text, ...)
    if not blocks:
        return None

    # Initialize bounding box to the first block's coordinates
    x0, y0, x1, y1 = blocks[0][:4]

    # Expand bounding box to include all blocks
    for block in blocks:
        x0 = min(x0, block[0])
        y0 = min(y0, block[1])
        x1 = max(x1, block[2])
        y1 = max(y1, block[3])

    return (x0, y0, x1, y1)

def extract_tables_from_all_pages(pdf_path, output_folder):
    """
    Extracts table-like areas from all pages of a PDF and saves them as images.

    :param pdf_path: Path to the PDF file.
    :param output_folder: Folder to save the extracted table images.
    """
    doc = fitz.open(pdf_path)
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    for page_number in range(len(doc)):
        page = doc[page_number]  # Get the page object

        # Detect bounding box for the table
        bbox = detect_table_blocks(page)
        if bbox is None:
            print(f"No text blocks detected on page {page_number + 1}")
            continue

        print(f"Page {page_number + 1}: Detected table bounding box: {bbox}")

        # Render and save the image for the bounding box
        clip = fitz.Rect(bbox)
        pixmap = page.get_pixmap(clip=clip, dpi=300)  # Adjust DPI for quality
        image_path = os.path.join(output_folder, f"page_{page_number + 1}_table.png")
        pixmap.save(image_path)
        print(f"Table extracted and saved: {image_path}")

    print(f"Extraction complete. Images saved in: {output_folder}")


def extract_non_text_regions(pdf_path, output_folder):
    """
    Extracts non-text regions (such as tables, diagrams, images) from all pages of a PDF
    and saves them as images.

    :param pdf_path: Path to the PDF file.
    :param output_folder: Folder to save the extracted images.
    """
    doc = fitz.open(pdf_path)
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    for page_number in range(len(doc)):
        page = doc[page_number]  # Get the page object
        page_width, page_height = page.rect.width, page.rect.height

        # Get text blocks and filter out non-table/diagram blocks
        blocks = page.get_text("blocks")
        non_text_regions = []  # Store regions to be saved as images

        for block in blocks:
            x0, y0, x1, y1, text = block[:5]
            block_width = x1 - x0
            block_height = y1 - y0

            # Check if the block has no text (likely an image/diagram region)
            if not text.strip():
                non_text_regions.append((x0, y0, x1, y1))

        if not non_text_regions:
            print(f"No non-text regions detected on page {page_number + 1}")
            continue

        # Render and save the image for each non-text region (image/diagram/table)
        for bbox in non_text_regions:
            clip = fitz.Rect(bbox)
            pixmap = page.get_pixmap(clip=clip, dpi=300)  # Adjust DPI for quality
            image_path = os.path.join(output_folder, f"page_{page_number + 1}_region.png")
            pixmap.save(image_path)
            print(f"Non-text region extracted and saved: {image_path}")

    print(f"Extraction complete. Images saved in: {output_folder}")
    
def extract_images(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)  # Get all images on the page
        
        for img_index, img in enumerate(images, start=1):
            xref = img[0]  # Image reference number
            base_image = doc.extract_image(xref)  # Extract image
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]  # Image extension (e.g., png, jpeg)
            image_filename = f"page{page_num+1}_img{img_index}.{image_ext}"

            # Save the image
            with open(os.path.join(output_folder, image_filename), "wb") as img_file:
                img_file.write(image_bytes)
            print(f"Saved image: {image_filename}")

def extract_hyperlinks(pdf_path):
    doc = fitz.open(pdf_path)
    links = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        for link in page.get_links():
            if "uri" in link:  # Check if the link has a URI (external link)
                links.append({"page": page_num + 1, "uri": link["uri"]})
    
    for link in links:
        print(f"Page {link['page']}: {link['uri']}")
        
def extract_metadata(pdf_path):
    doc = fitz.open(pdf_path)
    metadata = doc.metadata

    print("PDF Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

def pdf_to_markdown(pdf_path, md_path):
    doc = fitz.open(pdf_path)
    with open(md_path, 'w', encoding='utf-8') as md_file:
        for page in doc:
            text = page.get_text()  # Extract text from each page
            md_file.write(text + "\n---\n")  # Add separators for Markdown
    print(f"Markdown saved to {md_path}")
        


def extract_tables_from_pdf(pdf_path, output_folder):
    """
    Detects tables in a PDF by analyzing text blocks, lines, and structure.

    :param pdf_path: Path to the PDF file.
    :param output_folder: Folder to save the extracted tables as images.
    """
    doc = fitz.open(pdf_path)
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    for page_number in range(len(doc)):
        page = doc[page_number]  # Get the page object

        # Step 1: Extract text blocks
        blocks = page.get_text("blocks")

        # Step 2: Detect horizontal and vertical lines (potential table borders)
        lines = page.get_lines()

        # Step 3: Identify table-like structures by analyzing text alignment and lines
        table_regions = []
        rows = []
        current_row = []
        last_y = None
        for block in blocks:
            x0, y0, x1, y1, text = block[:5]

            # Skip blocks with no text
            if not text.strip():
                continue

            # Check if the block is part of a new row based on vertical position (y0)
            if last_y is not None and y0 > last_y + 5:  # 5 is a threshold for row spacing
                rows.append(current_row)
                current_row = []  # Start a new row

            current_row.append((x0, y0, x1, y1, text))  # Add the block to the current row
            last_y = y0

        # Append the last row if it's not empty
        if current_row:
            rows.append(current_row)

        # Step 4: Create bounding boxes around table regions
        for row in rows:
            min_x = min(block[0] for block in row)
            max_x = max(block[2] for block in row)
            min_y = min(block[1] for block in row)
            max_y = max(block[3] for block in row)

            # Define the bounding box of the table
            bbox = (min_x, min_y, max_x, max_y)
            table_regions.append(bbox)

        # Step 5: Extract the table as an image
        if table_regions:
            for bbox in table_regions:
                clip = fitz.Rect(bbox)
                pixmap = page.get_pixmap(clip=clip, dpi=300)  # Render the table as an image
                image_path = os.path.join(output_folder, f"page_{page_number + 1}_table.png")
                pixmap.save(image_path)
                print(f"Table extracted and saved: {image_path}")
        else:
            print(f"No tables detected on page {page_number + 1}")

    print(f"Table extraction complete. Images saved in: {output_folder}")
    
def process_pdf(pdf_path, output_folder):
    
    os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist

    #extract_tables_from_all_pages(pdf_path, os.path.join(output_folder, "tables"))
    #extract_tables_from_pdf(pdf_path, os.path.join(output_folder, "tables"))

    # Extract text and save as Markdown
    pdf_to_markdown(pdf_path, os.path.join(output_folder, "output.md"))
    
    # Extract images
    #extract_images(pdf_path, os.path.join(output_folder, "images"))
    
    # Extract hyperlinks
    #print("\nExtracting Hyperlinks:")
    #extract_hyperlinks(pdf_path)

    # Extract metadata
    #print("\nExtracting Metadata:")
    #extract_metadata(pdf_path)

# Example usage
process_pdf("csts.pdf", "output")