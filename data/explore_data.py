import pandas as pd
import os

# The link to the real-world telecom churn data
DATA_URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"

def load_and_explore():
    print("🚀 Starting Data Handshake...")
    
    try:
        # Load the data directly from the internet
        df = pd.read_csv(DATA_URL)
        print("✅ Data loaded successfully!")
        
        # This shows us the first 5 rows
        print("\n--- A Glimpse at the Data ---")
        print(df.head())
        
        # This lists all the columns available
        print("\n--- Columns we can use to predict Churn ---")
        for col in df.columns:
            print(f"- {col}")
        
        # Save a local copy
        if not os.path.exists('data'):
            os.makedirs('data')
        df.to_csv('data/raw_churn_data.csv', index=False)
        print("\n💾 Local copy saved to: data/raw_churn_data.csv")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTip: Run 'pip install pandas' in your terminal if you see a 'ModuleNotFoundError'.")

if __name__ == "__main__":
    load_and_explore()