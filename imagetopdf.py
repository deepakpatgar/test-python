import os
from tkinter import Tk, filedialog
from PIL import Image
from fpdf import FPDF

def select_images():
    root = Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)  # Bring the dialog to the front

    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    file_paths = filedialog.askopenfilenames(
        title="Select two image files",
        initialdir=downloads_path,
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
    )

    return file_paths

def merge_images(image1_path, image2_path, output_image_path):
    # Open the two images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Determine the size of the merged image
    width = max(image1.width, image2.width)
    height = image1.height + image2.height

    # Create a new image with a white background
    merged_image = Image.new('RGB', (width, height), (255, 255, 255))

    # Paste the images into the new image
    merged_image.paste(image1, (0, 0))
    merged_image.paste(image2, (0, image1.height))

    # Save the merged image
    merged_image.save(output_image_path)

def create_pdf(image_path, pdf_path):
    # Open the merged image
    image = Image.open(image_path)
    width, height = image.size

    # Convert pixel dimensions to mm (assuming 72 dpi for PDF)
    width_mm = width * 25.4 / 72
    height_mm = height * 25.4 / 72

    # Create instance of FPDF class
    pdf = FPDF(orientation='P', unit='mm', format=(width_mm, height_mm))

    # Add a page with the same size as the image
    pdf.add_page()

    # Insert the image in the page
    pdf.image(image_path, x=0, y=0, w=width_mm, h=height_mm)

    # Save the PDF to a file
    pdf.output(pdf_path)

# Allow the user to select two images
file_paths = select_images()
if len(file_paths) != 2:
    print("Please select exactly two images.")
else:
    # Paths to the output image and PDF in the Downloads directory
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    merged_image_path = os.path.join(downloads_path, 'merged_image.jpg')
    pdf_path = os.path.join(downloads_path, 'pdfoutput.pdf')

    # Merge the images and create a PDF
    merge_images(file_paths[0], file_paths[1], merged_image_path)
    create_pdf(merged_image_path, pdf_path)

    print(f"PDF created successfully: {pdf_path}")
