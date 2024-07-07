import os
import PyPDF2

def extract_pages_from_file(pdf_path, output_file, num_pages):
    """
    Extracts a specified number of pages from a single PDF and creates a new PDF.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_file (str): Path to the output PDF file.
        num_pages (int): Number of pages to extract.
    """

    with open(pdf_path, 'rb') as pdf_in, open(output_file, 'wb') as pdf_out:
        pdf_reader = PyPDF2.PdfReader(pdf_in)
        pdf_writer = PyPDF2.PdfWriter()

        # Get the number of pages in the input PDF (using the new method)
        total_pages = len(pdf_reader.pages)

        # Ensure num_pages is within valid range (1 to total_pages)
        if num_pages < 1 or num_pages > total_pages:
            print(f"Error: Invalid number of pages. Please enter a value between 1 and {total_pages}.")
            return

        # Extract and add desired pages to the new PDF
        for page_num in range(num_pages):
            pdf_writer.addPage(pdf_reader.pages[page_num])

        # Write the extracted pages to the output PDF
        pdf_writer.write(pdf_out)
        print(f"Successfully extracted {num_pages} pages from {pdf_path} to {output_file}.")

def extract_pages(input_folder, output_folder, num_pages):
    """
    Extracts a specified number of pages (num_pages) from all PDFs within a folder
    (input_folder) and creates new PDFs with extracted pages in the output folder.

    Args:
        input_folder (str): Path to the folder containing PDF files.
        output_folder (str): Path to the folder for storing extracted pages PDFs.
        num_pages (int): Number of pages to extract from each PDF.
    """

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):  # Check for PDF files
            pdf_path = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + "_extracted.pdf")  # Generate unique output filenames

            try:
                extract_pages_from_file(pdf_path, output_file, num_pages)  # Call the nested function
            except FileNotFoundError:
                print(f"Error: File not found: {pdf_path}")

    print("Finished processing all PDFs in the input folder.")

# Example usage (replace with your actual paths and desired number of pages)
# input_folder = "Input_PDFs"
# output_folder = "Extracted_Pages"
# num_pages = 5
