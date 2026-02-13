import pandas as pd
import numpy as np
import os

file_path = 'sales.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    df['Total'] = df['Quantity'] * df['Price']

    daily_sales = df.groupby('Date')['Total'].sum().values

    total_sales = np.sum(df['Total'])
    avg_daily_sales = np.mean(daily_sales)
    std_daily_sales = np.std(daily_sales)
    best_selling_product = df.groupby('Product')['Quantity'].sum().idxmax()

    print("--- Processed Data ---")
    print(df)
    print("\n--- Summary Statistics ---")
    print(f"Total Revenue:      {total_sales}")
    print(f"Avg Daily Sales:    {avg_daily_sales:.2f}")
    print(f"Std Dev of Sales:   {std_daily_sales:.2f}")
    print(f"Best-seller (Qty):  {best_selling_product}")
else:
    print(f"Error: {file_path} not found. Please check the directory.")