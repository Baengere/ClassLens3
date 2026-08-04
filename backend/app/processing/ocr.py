import cv2
import pytesseract
import tempfile
import os
from PIL import Image

def preprocess_image(image_path:str):
    """Prepare image for OCR"""

    # Read image

    image = cv2.imread(image_path)

    # Convert to grayscale

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Remove noise

    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Convert to pure black and white

    _, thresh = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    return thresh




def extract_text(image_path:str)-> str:
    """Extract text from an image using tesseract after preprocessing."""

    processed = preprocess_image(image_path)

    with tempfile.NamedTemporaryFile(
        suffix=".png",
        delete=False,
    )as temp:
        cv2.imwrite(temp.name, processed)

        text = pytesseract.image_to_string(
            Image.open(temp.name),
            config="--oem 3 --psm 6"
        )
        os.unlink(temp.name)
    return text.strip()