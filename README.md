# pdf-page-shortener [![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
✂️ PDF Page Extractor
Extract a specific number of pages or a page range from multiple PDFs in a folder with just a few lines of code.

This script offers a user-friendly solution for anyone who needs to frequently manipulate PDF pages.

Prerequisites

Python 3.x (see badge above)
PyPDF2 library: pip install PyPDF2
How to Use

Clone or download the repository.
Navigate to the script's directory. You can use a terminal or command prompt for this.
Replace the placeholders in the example_usage section of the script with your actual file paths.
# Example usage (replace with your actual paths and desired number of pages)
input_folder = "path/to/your/folder/containing/pdfs"
output_folder = "path/to/your/output/folder"
num_pages = 3  # Number of pages to extract (or specify a page range as a list: [start_page, end_page])
Run the script. Use the command python pdf_page_extractor.py (replace with your script's actual filename).
Example:

Successfully extracted 3 pages from /path/to/your/pdf/file.pdf to /path/to/your/output/folder/file_extracted.pdf.
Additional Notes

The script handles potential errors like missing files or invalid input by printing informative messages to the console.
You can customize the output filenames by modifying the script's logic for generating them (refer to the code for details).
