import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

def build_ai():
    print("🧠 Starting AI Training...")
    
    # 1. Load the cleaned data you prepared
    file_path = 'data/cleaned_churn_data.csv'
    if not os.path.exists(file_path):
        print("❌ Error: cleaned_churn_data.csv not found! Run clean_data.py first.")
        return
        
    df = pd.read_csv(file_path)
    
    # 2. Select Features (What the AI looks at)
    # We are teaching it to look at Tenure and Monthly Charges
    X = df[['tenure', 'MonthlyCharges']] 
    
    # The AI needs numbers. We convert Churn 'Yes'/'No' to 1 and 0
    y = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    # 3. Split the data
    # 80% to study, 20% to test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Initialize the AI Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # 5. The Learning Phase
    print("🎓 The AI is studying the patterns...")
    model.fit(X_train, y_train)
    
    # 6. The Testing Phase
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print("\n✨ Training Complete!")
    print(f"🎯 AI Accuracy Score: {accuracy * 100:.2f}%")
    print("--------------------------------------------------")
    print("This score shows how well the AI predicts churn.")

if __name__ == "__main__":
    build_ai()
    