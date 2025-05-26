# predict.py
import pandas as pd
from joblib import load

# Load the trained model
try:
    model = load('model/heart_model.pkl')
except FileNotFoundError:
    print("❌ Error: Trained model file not found. Make sure 'heart_model.pkl' exists in the 'model/' directory.")
    exit()

# Feature details (keys must match training column names exactly)
feature_info = {
    'age': 'Age (in years)',
    'sex': 'Sex (1 = male, 0 = female)',
    'cp': 'Chest Pain Type (0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic)',
    'trestbps': 'Resting Blood Pressure (in mm Hg)',
    'chol': 'Serum Cholesterol (in mg/dl)',
    'fbs': 'Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)',
    'restecg': 'Resting ECG Results (0 = normal, 1 = ST-T abnormality, 2 = left ventricular hypertrophy)',
    'thalach': 'Maximum Heart Rate Achieved',
    'exang': 'Exercise Induced Angina (1 = yes, 0 = no)',
    'oldpeak': 'ST Depression Induced by Exercise (e.g., 1.4)',
    'slope': 'Slope of ST Segment (0 = up, 1 = flat, 2 = down)',
    'ca': 'Number of Major Vessels Colored by Fluoroscopy (0-3)',
    'thal': 'Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)'
}

def get_user_input():
    """Collect and validate user input for each feature."""
    user_data = []
    print("🔍 Please enter the following health details:\n")
    for feat, desc in feature_info.items():
        while True:
            try:
                val = float(input(f"{feat} ({desc}): "))
                user_data.append(val)
                break
            except ValueError:
                print("⚠️ Invalid input. Please enter a numeric value.")
    return pd.DataFrame([user_data], columns=feature_info.keys())

def make_prediction(input_df):
    """Make prediction using the trained model."""
    prediction = model.predict(input_df)
    return prediction[0]

def main():
    while True:
        user_df = get_user_input()
        result = make_prediction(user_df)

        print("\n🔎 Prediction Result:")
        if result == 1:
            print("⚠️ The model predicts: **Possible Heart Disease.** Please consult a doctor.")
        else:
            print("✅ The model predicts: **No Heart Disease.** Stay healthy!")

        again = input("\n🔁 Do you want to test another case? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Exiting the prediction tool. Take care!")
            break

if __name__ == "__main__":
    main()
