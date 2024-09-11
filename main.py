import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path


def pdf_to_text(pdf_path):
  """
  Convert a PDF to text using OCR.

  Parameters:
  - pdf_path (str): Path to the PDF file.
  - output_dir (str): Directory where image files will be saved (optional).

  Returns:
  - str: Extracted text from the PDF.
  """
  try:
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)

    # Initialize a text accumulator
    full_text = ''

    # Process each image
    for i, image in enumerate(images):
      # Save the image if needed (optional)
      image_path = f'./page_{i+1}.png'
      image.save(image_path, 'PNG')

      # Use pytesseract to do OCR on the image
      text = pytesseract.image_to_string(image, lang='chi_sim')
      full_text += text + '\n'

    return full_text

  except Exception as e:
    print(f"An error occurred: {e}")
    return None


def recognize_pdf(pdf_path):
  results = []
  if os.path.exists(pdf_path):
    text = pdf_to_text(pdf_path)
    results.append(text)
  return results
    

# 主函数
if __name__ == '__main__':
  results = recognize_pdf("./0.pdf")
  for result in results:
    print(result)  # Print recognized text