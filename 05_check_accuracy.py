import pandas as pd

df = pd.read_csv('superstore_clean.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Month'] = df['Order Date'].dt.to_period('M').dt.to_timestamp()
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
monthly_sales.columns = ['ds', 'y']

avg_monthly = monthly_sales['y'].mean()
mae = 1394.50
accuracy = 100 - (mae / avg_monthly * 100)

print(f"Average Monthly Sales: {avg_monthly:.2f}")
print(f"Model Accuracy: {accuracy:.2f}%")