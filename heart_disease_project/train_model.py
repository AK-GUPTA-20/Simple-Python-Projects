# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump

# Load dataset
df = pd.read_csv('data/heart.csv')

#  columns to match ML expectations
df.columns = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
    'restecg', 'thalach', 'exang', 'oldpeak',
    'slope', 'ca', 'thal', 'target'  # Assuming 'target' is the last column
]

X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
dump(model, 'model/heart_model.pkl')
print("✅ Model trained and saved successfully!")
