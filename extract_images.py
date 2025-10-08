#!/usr/bin/env python3
import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_dir="images"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    image_count = 0

    # Iterate through pages
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]

        # Get images on the page
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]

            # Extract the image
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # Save the image
            image_filename = f"{output_dir}/page{page_num + 1}_img{img_index + 1}.{image_ext}"

            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)

            image_count += 1
            print(f"Extracted: {image_filename}")

    pdf_document.close()
    print(f"\nTotal images extracted: {image_count}")
    return image_count

if __name__ == "__main__":
    pdf_path = "status-report.pdf"
    extract_images_from_pdf(pdf_path)
