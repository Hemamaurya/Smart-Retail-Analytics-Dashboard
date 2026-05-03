import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Clean data load karo
df = pd.read_csv('superstore_clean.csv')

# Style set karo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 5)

# ============ 1. Region wise Sales aur Profit ============
print("=== Region wise Sales & Profit ===")
region_data = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
print(region_data)

region_data.plot(x='Region', kind='bar', color=['steelblue', 'coral'])
plt.title('Region wise Sales & Profit')
plt.xlabel('Region')
plt.ylabel('Amount')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('region_sales.png')
plt.show()

# ============ 2. Category wise Profit ============
print("\n=== Category wise Profit ===")
cat_data = df.groupby('Category')['Profit'].sum().reset_index()
print(cat_data)

sns.barplot(data=cat_data, x='Category', y='Profit', palette='Set2')
plt.title('Category wise Profit')
plt.tight_layout()
plt.savefig('category_profit.png')
plt.show()

# ============ 3. Monthly Sales Trend ============
print("\n=== Monthly Sales Trend ===")
monthly = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()
monthly['Date'] = pd.to_datetime(dict(year=monthly['Order Year'], month=monthly['Order Month'], day=1))
monthly = monthly.sort_values('Date')

plt.figure(figsize=(14, 5))
plt.plot(monthly['Date'], monthly['Sales'], color='steelblue', linewidth=2)
plt.title('Monthly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('monthly_trend.png')
plt.show()

# ============ 4. Segment wise Sales ============
print("\n=== Segment wise Sales ===")
seg_data = df.groupby('Segment')['Sales'].sum().reset_index()
print(seg_data)

plt.pie(seg_data['Sales'], labels=seg_data['Segment'],
        autopct='%1.1f%%', colors=['steelblue','coral','mediumseagreen'])
plt.title('Segment wise Sales')
plt.tight_layout()
plt.savefig('segment_sales.png')
plt.show()

# ============ 5. Top 10 Loss Making Products ============
print("\n=== Top 10 Loss Products ===")
loss_products = df[df['Profit'] < 0].groupby('Product Name')['Profit'].sum()
loss_products = loss_products.sort_values().head(10).reset_index()
print(loss_products)

sns.barplot(data=loss_products, x='Profit', y='Product Name', palette='Reds_r')
plt.title('Top 10 Loss Making Products')
plt.tight_layout()
plt.savefig('loss_products.png')
plt.show()

print("\nSaare graphs save ho gaye retail_project folder mein!")