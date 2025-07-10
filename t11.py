import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\gokul\OneDrive\Documents\task1\tech_products.csv.csv"

try:
    df = pd.read_csv(file_path)
    print("✅ File loaded successfully!\n")
    print(df.head())  # Show first 5 rows

    # --- Visualization 1: Price Bar Chart ---
    plt.figure(figsize=(10, 5))
    plt.bar(df['Product'], df['Price'], color='skyblue')
    plt.title('Product Prices')
    plt.xlabel('Product')
    plt.ylabel('Price (₹)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("product_prices.png")
    plt.show()

    # --- Visualization 2: Rating Bar Chart ---
    plt.figure(figsize=(10, 5))
    plt.bar(df['Product'], df['Rating'], color='orange')
    plt.title('Product Ratings')
    plt.xlabel('Product')
    plt.ylabel('Rating')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("product_ratings.png")
    plt.show()

except FileNotFoundError:
    print(f"❌ File not found at: {file_path}")
    print("👉 Make sure the file name and folder path are correct.")

