# NLP Test Task

This repository contains code for a PDF converter with simple tokenization `Pdf2text.py`, developed for solve a test task for industrial immersion at Gaspromneft.

## Installation

To use this PDF converter, follow these steps:

1. **Install Tesseract OCR engine:**
   
   You must install the Tesseract OCR engine from the official repository ([Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)). 
   For Windows users, the installer can be downloaded from a different source ([Tesseract Wiki](https://github.com/UB-Mannheim/tesseract/wiki)).

2. **Install Poppler:**
   
   Follow the installation steps provided in the official documentation of `pdf2image` ([pdf2image Installation](https://pdf2image.readthedocs.io/en/latest/installation.html)).
   
3. **Install additional language packs:**

   You may need to install additional language packs for Tesseract OCR. Refer to the [documentation](https://ocrmypdf.readthedocs.io/en/latest/languages.html) for instructions on how to install these packs.

4. **Install Required Libraries**

   To install the required libraries, you can use the `requirements.txt` file provided in this repository. Navigate to the directory containing the `requirements.txt` file and run the following command:

   ```bash
   pip install -r requirements.txt-r requirements.txt
   ```


## Functionality

The provided code includes the following functionalities:

- **Text Extraction from PDFs:** Use the `text_extracter()` function to extract text from PDF files.
- **Text Cleaning:** The `clean_text()` function removes non-alphanumeric characters, converts text to lowercase, and removes leading and trailing whitespaces.
- **Language Detection:** The `language_detector()` function detects the language of a given token.
- **Language Separation:** The `language_separator()` function separates text into Russian and English parts based on language detection.
- **Text Tokenization:** Use the `tokenize_text()` function to tokenize text into words, considering the language.
- **Stopwords Removal:** The `remove_stopwords()` function removes stopwords from a list of tokens, based on the language.


## Example Usage

For an example usage of the provided functionalities, please refer to the accompanying Jupyter Notebook file: [example_usage.ipynb](https://github.com/RattametB/NLP_test_task/blob/main/Example_of_usage.ipynb).

In the Jupyter Notebook, you can see how to use the functions for text extraction, cleaning, language detection, separation, tokenization, and stopwords removal on a sample PDF document.


