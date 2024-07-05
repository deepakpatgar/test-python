import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def compress_image(input_image_path, output_image_path, quality):
    image = Image.open(input_image_path)
    image.save(output_image_path, "PDF", optimize=True, quality=quality)

def convert_image_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.jpg")])
    if not file_path:
        return

    # Convert image to PDF
    pdf_path = os.path.splitext(file_path)[0] + ".pdf"
    quality = 95
    compress_image(file_path, pdf_path, quality)

    # Check if the PDF size is below 200 KB
    while os.path.getsize(pdf_path) > 200 * 1024 and quality > 10:
        quality -= 5
        compress_image(file_path, pdf_path, quality)

    if os.path.getsize(pdf_path) > 200 * 1024:
        print("Unable to compress the PDF to below 200 KB. The quality may be too low.")
    else:
        print(f"PDF saved successfully at {pdf_path} with size {os.path.getsize(pdf_path) / 1024:.2f} KB")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    convert_image_to_pdf()
