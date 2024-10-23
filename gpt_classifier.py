# src/gpt_classifier.py
import os
import openai
import hashlib
import json
import requests
from src.config import Config

class GPTClassifier:
    def __init__(self, cache_path='cache.json'):
        self.cache_path = cache_path
        self.cache = self._load_cache()
        openai.api_key = Config.AZURE_API_KEY

    def _load_cache(self):
        if os.path.exists(self.cache_path):
            with open(self.cache_path, 'r') as f:
                return json.load(f)
        return {}

    def _save_cache(self):
        with open(self.cache_path, 'w') as f:
            json.dump(self.cache, f)

    def _hash_query(self, query):
        return hashlib.md5(query.encode()).hexdigest()

    def classify_transaction(self, transaction_description):
        query_hash = self._hash_query(transaction_description)

        if query_hash in self.cache:
            return self.cache[query_hash]

        system_prompt = "You are a transaction classifier. Classify the given transaction description into one category."
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": transaction_description}
        ]

        try:
            response = requests.post(
                f"{Config.AZURE_API_BASE}/openai/deployments/{Config.AZURE_DEPLOYMENT_NAME}/chat/completions?api-version={Config.AZURE_API_VERSION}",
                headers={"api-key": Config.AZURE_API_KEY},
                json={"model": Config.AZURE_DEPLOYMENT_NAME, "messages": messages}
            )
            response_json = response.json()
            category = response_json['choices'][0]['message']['content'].strip()
        except Exception as e:
            print(f"Error with Azure OpenAI API: {e}")
            category = "Unknown"

        self.cache[query_hash] = category
        self._save_cache()
        return category
