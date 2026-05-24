import pandas as pd
import matplotlib.pyplot as plt
import os

def create_visuals():
    print("📊 Generating Visual Insights...")
    
    # 1. Load the CLEAN data we made earlier
    file_path = 'data/cleaned_churn_data.csv'
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found. Please run clean_data.py first!")
        return
        
    df = pd.read_csv(file_path)
    
    # 2. Setup the chart look
    plt.figure(figsize=(10, 6))
    
    # 3. Create a Bar Chart
    churn_counts = df['Churn'].value_counts()
    churn_counts.plot(kind='bar', color=['#4CAF50', '#FF5722'], edgecolor='black')
    
    # 4. Add Professional Labels
    plt.title('Customer Retention: Stayed vs. Left', fontsize=14, fontweight='bold')
    plt.xlabel('Customer Status', fontsize=12)
    plt.ylabel('Number of Customers', fontsize=12)
    plt.xticks(ticks=[0, 1], labels=['Stayed (No)', 'Left (Yes)'], rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    # 5. Save the chart as an image
    if not os.path.exists('data'):
        os.makedirs('data')
    plt.savefig('data/churn_chart.png')
    print("✅ Chart saved to data/churn_chart.png")
    
    # 6. Pop up the window to show you the result
    print("🖼️  Opening chart preview window...")
    plt.show()

if __name__ == "__main__":
    create_visuals()