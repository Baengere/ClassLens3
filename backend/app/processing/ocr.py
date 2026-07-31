import pytesseract
from PIL import Image

def extract_text(image_path:str)-> str:
    """Extract text from an image using Tesseract OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()