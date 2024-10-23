# src/data_loader.py
import pandas as pd
import re

class DatasetLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def preprocess(self, text):
        # Basic text normalization
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text

    def load_data(self):
        df = pd.read_csv(self.file_path)
        df['transaction_description'] = df['transaction_description'].apply(self.preprocess)
        return df
