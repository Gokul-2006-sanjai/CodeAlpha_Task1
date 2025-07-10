import pandas as pd

file_path = r"C:\Users\gokul\OneDrive\Documents\task1\tech_products.csv.csv"

try:
    df = pd.read_csv(file_path)
    print("✅ File loaded successfully!\n")
    print(df.head())  # shows first 5 rows
except FileNotFoundError:
    print(f"❌ File not found at: {file_path}")
    print("👉 Make sure the file name and folder path are correct.")
