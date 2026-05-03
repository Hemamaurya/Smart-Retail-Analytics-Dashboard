import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Data load karo
df = pd.read_csv('superstore_clean.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ============ 1. Prophet ke liye data prepare karo ============
# Prophet ko sirf 2 columns chahiye: ds (date) aur y (value)
df['Month'] = df['Order Date'].dt.to_period('M').dt.to_timestamp()
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
monthly_sales.columns = ['ds', 'y']
monthly_sales = monthly_sales.sort_values('ds')

print("=== Data Prophet ke liye ready ===")
print(monthly_sales.head())
print(f"Total data points: {len(monthly_sales)}")

# ============ 2. Model banao ============
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    seasonality_mode='multiplicative'
)

model.fit(monthly_sales)
print("\nModel training complete!")

# ============ 3. Future 90 days predict karo ============
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

print("\n=== Agle 90 Days ki Prediction ===")
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))

# ============ 4. Forecast Graph ============
fig1 = model.plot(forecast)
plt.title('Sales Forecast - Agle 90 Din')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('sales_forecast.png')
plt.show()
print("Forecast graph save ho gaya!")

# ============ 5. Seasonality Graph ============
fig2 = model.plot_components(forecast)
plt.tight_layout()
plt.savefig('seasonality.png')
plt.show()
print("Seasonality graph save ho gaya!")

# ============ 6. Model Accuracy check karo ============
# Actual vs Predicted compare karo
merged = forecast[['ds', 'yhat']].merge(monthly_sales, on='ds')
mae = mean_absolute_error(merged['y'], merged['yhat'])
rmse = np.sqrt(mean_squared_error(merged['y'], merged['yhat']))

print(f"\n=== Model Accuracy ===")
print(f"MAE  (Mean Absolute Error): {mae:.2f}")
print(f"RMSE (Root Mean Sq Error) : {rmse:.2f}")
print(f"\nModel training complete - forecast ready!")