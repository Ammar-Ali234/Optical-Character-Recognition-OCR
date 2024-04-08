# OCR using Python  & OpenCV

This Python script performs Optical Character Recognition (OCR) on an image using the EasyOCR library. It reads text from the specified image, draws bounding boxes around detected text, and displays the image with the recognized text and bounding boxes using OpenCV and Matplotlib.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Matplotlib (`matplotlib`)
- EasyOCR (`easyocr`)

## Installation

1. Install Python (if not already installed): [Python Official Website](https://www.python.org/downloads/)
2. Install required Python packages:
    ```bash
    pip install opencv-python
    pip install matplotlib
    pip install easyocr
    ```

## Usage

1. Place the image file (`tt3.jpg`) you want to perform OCR on in the same directory as the script.
2. Run the OCR script:
    ```bash
    python char.py
    ```
3. The script will display the image with recognized text and bounding boxes using Matplotlib.

## Script Explanation

- The script uses OpenCV to read the image.
- It initializes the EasyOCR reader with English language support.
- It performs OCR on the image and retrieves the recognized text and bounding boxes.
- It draws bounding boxes around the detected text and displays the image using Matplotlib.

## Example Output

The output will be an image displayed using Matplotlib, with recognized text highlighted by bounding boxes. See the Result and Demo Folder for that.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
