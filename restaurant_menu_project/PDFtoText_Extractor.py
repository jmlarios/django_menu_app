import fitz  # PyMuPDF
import mysql.connector
from google.cloud import vision
from google.oauth2 import service_account
from mysql.connector import Error
import io
from PIL import Image


# Function to extract text from a PDF using PyMuPDF (for PDFs with selectable text)
def extract_text_from_pdf(pdf_file_path):
    try:
        # Open the PDF file using PyMuPDF
        doc = fitz.open(pdf_file_path)
        text = ""

        # Extract text from each page
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # Page is 0-indexed
            text += page.get_text("text")  # Extract text as plain text

        return text
    except Exception as e:
        print(f"An error occurred while extracting text from the PDF: {e}")
        return None


# Function to extract text from an image (using Google Vision API)
def extract_text_from_image(image_path):
    try:
        # Set up credentials for Google Cloud Vision API
        credentials = service_account.Credentials.from_service_account_file(r"C:\Users\User\Downloads\output-results_output-1-to-1.json")
        client = vision.ImageAnnotatorClient(credentials=credentials)

        # Read image into memory
        with open(image_path, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)  # Directly create the vision.Image object

        # Perform text detection on the image
        response = client.text_detection(image=image)
        texts = response.text_annotations

        if texts:
            return texts[0].description  # Return the full text detected by the API
        else:
            return "No text found."
    except Exception as e:
        print(f"An error occurred while extracting text from the image: {e}")
        return None

# Function to insert text into MySQL database
def insert_text_into_db(text):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host (e.g., 'localhost')
            user='root',  # Replace with your MySQL username (e.g., 'root')
            password='Mine-craft1',  # Replace with your MySQL password
            database='restaurantmenusystem'  # Replace with your MySQL database name
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query to insert extracted text into the table (adjust as needed)
            insert_query = """INSERT INTO extracted_text_table (text_column) VALUES (%s)"""

            # Insert the extracted text into the database
            cursor.execute(insert_query, (text,))
            connection.commit()

            print("Text successfully inserted into the database.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Main function to orchestrate the extraction and insertion
def main():
    pdf_file_path = r"C:\Users\User\Downloads\restaurante_2.pdf"  # Specify the path to your PDF file

    # Extract text from PDF (if it contains text)
    extracted_text = extract_text_from_pdf(pdf_file_path)

    if extracted_text:
        print("Extracted text from PDF (direct text extraction):")
        print(extracted_text)
        insert_text_into_db(extracted_text)  # Insert into DB if text found
    else:
        # If no text, extract text from images in the PDF using Google Vision API
        print("No text found in PDF. Attempting to extract text from images using Google Vision API.")

        # You may need to convert PDF pages to images for Google Vision API processing
        # For simplicity, let's assume we convert the first page to an image and send it to the Vision API
        extracted_image_text = extract_text_from_image('path_to_image_from_pdf.jpg')  # Replace with actual image path

        if extracted_image_text:
            print("Extracted text from image (Google Vision API):")
            print(extracted_image_text)
            insert_text_into_db(extracted_image_text)  # Insert into DB if text found from image
        else:
            print("No text could be extracted from the image.")


if __name__ == "__main__":
    main()
