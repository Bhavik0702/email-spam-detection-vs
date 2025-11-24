import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import os

def train():
    # Load data
    data_path = "spam.csv"
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return

    try:
        # spam.csv typically uses latin-1 encoding
        df = pd.read_csv(data_path, encoding='latin-1')
        
        # Rename columns if necessary (assuming v1=label, v2=message based on inspection)
        if 'v1' in df.columns and 'v2' in df.columns:
            df = df.rename(columns={'v1': 'label', 'v2': 'message'})
        
        # Keep only necessary columns
        df = df[['label', 'message']]
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Basic preprocessing
    X = df['message']
    y = df['label']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', MultinomialNB()),
    ])

    # Train
    print("Training model...")
    pipeline.fit(X_train, y_train)

    # Evaluate
    print("Evaluating model...")
    predictions = pipeline.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")
    print("Classification Report:")
    print(classification_report(y_test, predictions))

    # Save model
    with open("spam_model.pkl", "wb") as f:
        pickle.dump(pipeline, f)
    print("Model saved to spam_model.pkl")

if __name__ == "__main__":
    train()
