import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Load Data
# Note: Ensure you have 'True.csv' and 'Fake.csv' in a folder named 'data'
true_df = pd.read_csv('data/True.csv')
fake_df = pd.read_csv('data/Fake.csv')

# Add labels: 0 for Real, 1 for Fake
true_df['label'] = 0 
fake_df['label'] = 1

# Combine and shuffle the data
df = pd.concat([true_df, fake_df]).sample(frac=1).reset_index(drop=True)

# 2. Preprocessing & Vectorization
# We convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 3. Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. Save Artifacts
# This allows 'app.py' to use the trained model without re-training
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model and Vectorizer saved successfully!")