# src/retriever.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class TfidfRetriever:
    def __init__(self, data):
        self.vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2), stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(data['transaction_description'])
        self.data = data

    def retrieve_similar(self, query, top_n=3):
        query_vec = self.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_indices = np.argsort(similarity)[::-1][:top_n]
        similar_items = self.data.iloc[top_indices]
        return similar_items[['transaction_description', 'category']].to_dict('records')
