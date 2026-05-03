import pandas as pd
import numpy as np

# Data load karo
df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')

# Pehli 5 rows dekho
print(df.head())

# Shape dekho
print("\nRows aur Columns:", df.shape)

# Columns ke naam
print("\nColumns:", df.columns.tolist())

'''=========== Cleaning Data ==========='''
import pandas as pd
import numpy as np

# Data load karo
df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')

# 1. Missing values check karo
print("=== Missing Values ===")
print(df.isnull().sum())

# 2. Duplicate rows check karo
print("\n=== Duplicate Rows ===")
print("Duplicates:", df.duplicated().sum())

# 3. Data types dekho
print("\n=== Data Types ===")
print(df.dtypes)

# ============ ACTUAL CLEANING ============

# 1. Dates convert karo
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 2. Naye useful columns banao
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.strftime('%B')
df['Order Quarter'] = df['Order Date'].dt.quarter
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# 3. Profit Margin % nikalo
df['Profit Margin %'] = (df['Profit'] / df['Sales']) * 100

# 4. Loss wale orders flag karo
df['Is Loss'] = df['Profit'] < 0

# 5. Verify karo
print("=== Dates After Conversion ===")
print(df[['Order Date', 'Ship Date']].dtypes)

print("\n=== Naye Columns ===")
print(df[['Order Year', 'Order Month', 'Delivery Days', 'Profit Margin %', 'Is Loss']].head(10))

print("\n=== Final Shape ===")
print("Rows, Columns:", df.shape)

# 6. Clean data save karo
df.to_csv('superstore_clean.csv', index=False)
print("\nClean data save ho gaya! superstore_clean.csv")