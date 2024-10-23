# src/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    AZURE_API_KEY = os.getenv('AZURE_API_KEY')
    AZURE_API_VERSION = os.getenv('AZURE_API_VERSION')
    AZURE_API_BASE = os.getenv('AZURE_API_BASE')
    AZURE_DEPLOYMENT_NAME = os.getenv('AZURE_DEPLOYMENT_NAME')
