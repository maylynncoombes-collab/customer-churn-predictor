import pandas as pd

def clean_churn_data():
    print("🧹 Starting the Data Clean-up...")
    
    # 1. Load the local data we saved earlier
    df = pd.read_csv('data/raw_churn_data.csv')
    
    # 2. Check for missing values (The "Null Hunt")
    print("\n🔍 Checking for missing values:")
    print(df.isnull().sum())
    
    # 3. Fix the "TotalCharges" column
    # Sometimes it has empty spaces which breaks the math. We'll turn them into 0.
    print("\n⚙️  Converting TotalCharges to numbers...")
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    
    # 4. Fill any new empty spots with 0
    df['TotalCharges'] = df['TotalCharges'].fillna(0)
    
    # 5. Summarize the numbers (Math without doing math!)
    print("\n📈 Financial Summary:")
    print(df[['tenure', 'MonthlyCharges', 'TotalCharges']].describe())
    
    # 6. Save the "Clean" version
    df.to_csv('data/cleaned_churn_data.csv', index=False)
    print("\n✨ Success! Cleaned data saved to: data/cleaned_churn_data.csv")

if __name__ == "__main__":
    clean_churn_data()