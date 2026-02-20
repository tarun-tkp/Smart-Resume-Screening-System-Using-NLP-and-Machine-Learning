"""
Text Extractor Module
Handles extraction of text from PDF and DOCX files
"""

import pdfplumber
from docx import Document
import re


def extract_text_from_pdf(file):
    """
    Extract text from PDF file using pdfplumber
    
    Args:
        file: Uploaded PDF file object
        
    Returns:
        str: Extracted text content
    """
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        raise Exception(f"Error extracting PDF: {str(e)}")
    
    return text.strip()


def extract_text_from_docx(file):
    """
    Extract text from DOCX file using python-docx
    
    Args:
        file: Uploaded DOCX file object
        
    Returns:
        str: Extracted text content
    """
    text = ""
    try:
        doc = Document(file)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        raise Exception(f"Error extracting DOCX: {str(e)}")
    
    return text.strip()


def clean_text(text):
    """
    Clean and normalize extracted text
    
    Args:
        text: Raw text string
        
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters but keep alphanumeric and common punctuation
    text = re.sub(r'[^\w\s\.\,\-\+\#]', '', text)
    
    return text.strip()
