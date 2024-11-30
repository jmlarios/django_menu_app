##Database Project

# PDF and Image Text Extractor

This project extracts text from PDFs and images using PyMuPDF and Google Cloud Vision API. It saves the extracted text to a `.txt` file for further processing.

## Features

- Extract text from PDFs with selectable text using PyMuPDF.
- Extract text from images using the Google Cloud Vision API.
- Save the extracted text into a `.txt` file.

---

## Requirements

To run this project, ensure you have the following dependencies installed:

### Python Libraries

- `PyMuPDF` (`fitz`) – For extracting text from PDFs.
- `google-cloud-vision` – For using Google Vision API.
- `google-auth` – For handling Google service credentials.
- `Pillow` – For image handling.

### System Requirements

- Python 3.8 or later.
- A Google Cloud account with Vision API enabled.
- A valid service account key in JSON format for Google Cloud authentication.

---

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
2. **Install the Required Libraries (TEMPORARY-WILL PUT THEM IN REQUIREMENTS FILE)**:

pip install PyMuPDF
pip install mysql-connector-python
pip install google-cloud-vision
pip install google-auth

