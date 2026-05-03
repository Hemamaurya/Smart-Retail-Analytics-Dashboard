import pandas as pd
import mysql.connector

# MySQL se connect karo
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="retail_db"
)

cursor = conn.cursor()

# Clean data load karo
df = pd.read_csv('superstore_clean.csv')

# Date columns fix karo
df['Order Date'] = pd.to_datetime(df['Order Date']).dt.strftime('%Y-%m-%d')
df['Ship Date'] = pd.to_datetime(df['Ship Date']).dt.strftime('%Y-%m-%d')

# Sirf original 21 columns lo
df = df[['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
         'Customer ID', 'Customer Name', 'Segment', 'Country', 'City',
         'State', 'Postal Code', 'Region', 'Product ID', 'Category',
         'Sub-Category', 'Product Name', 'Sales', 'Quantity',
         'Discount', 'Profit']]

# Row by row insert karo
insert_query = """
INSERT INTO orders VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

count = 0
for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))
    count += 1
    if count % 1000 == 0:
        print(f"{count} rows insert ho gayi...")

# Save karo
conn.commit()
print(f"\nTotal {count} rows successfully MySQL mein import ho gayi!")

# Verify karo
cursor.execute("SELECT COUNT(*) FROM orders")
result = cursor.fetchone()
print(f"Database mein total rows: {result[0]}")

cursor.close()
conn.close()
print("Connection closed!")