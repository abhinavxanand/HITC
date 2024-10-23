# scripts/main.py
from src.data_loader import DatasetLoader
from src.retriever import TfidfRetriever
from src.gpt_classifier import GPTClassifier
from src.classifier import RAGTransactionClassifier

# Load and prepare data
dataset_loader = DatasetLoader('data/transactions.csv')
df = dataset_loader.load_data()

# Instantiate models
tfidf_retriever = TfidfRetriever(df)
gpt_classifier = GPTClassifier()

# Create combined RAG-based classifier
rag_classifier = RAGTransactionClassifier(tfidf_retriever, gpt_classifier)

# Example classification
transaction = "Starbucks coffee purchase"
result = rag_classifier.classify_transaction(transaction)

print(f"Classification Result: {result}")
