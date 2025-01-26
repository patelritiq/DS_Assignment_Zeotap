import pandas as pd
import matplotlib.pyplot as plt


cust = pd.read_csv('Customers.csv')
prod = pd.read_csv('Products.csv')
trans = pd.read_csv('Transactions.csv')

#Head
print("Customers Data Head:")
print()
print(cust.head())
print("\n\n")

print("Products Data Head:")
print()
print(prod.head())
print("\n\n")

print("Transactions Data Head:")
print()
print(trans.head())
print("\n\n")

#Cleaning
cust['SignupDate'] = pd.to_datetime(cust['SignupDate'])
trans['TransactionDate'] = pd.to_datetime(trans['TransactionDate'])

#Combine
data = trans.merge(cust, on='CustomerID').merge(prod, on='ProductID')
data = data.drop(columns=['Price_y'])
data.rename(columns={'Price_x': 'Price'}, inplace=True)

#Summary
print("Data Summary:")
print()
print(data.describe())
print("\n\n")

print("Data Info:")
print()
print(data.info())
print("\n\n")

#Most purchased products
prod_sales = data.groupby('ProductName')['Quantity'].sum().sort_values(ascending=False)
print("Most Purchased Products:")
print()
print(prod_sales.head())
print("\n\n")

#Revenue by region
region_rev = data.groupby('Region')['TotalValue'].sum()
print("Revenue by Region:")
print()
print(region_rev)
print("\n\n")

#Customer signup trend
signup_trend = cust['SignupDate'].dt.to_period('M').value_counts().sort_index()
print("Customer Signup Trend:")
print()
print(signup_trend)
print("\n\n")

#Top customers by spend
top_cust = data.groupby('CustomerName')['TotalValue'].sum().sort_values(ascending=False)
print("Top Customers by Spend:")
print()
print(top_cust.head())
print("\n\n")

#Category sales
cat_sales = data.groupby('Category')['Quantity'].sum()
print("Category Sales:")
print()
print(cat_sales)
print("\n\n")

#Avg transaction value by product
avg_trans_val = data.groupby('ProductName')['TotalValue'].mean().sort_values(ascending=False)
print("Average Transaction Value by Product:")
print()
print(avg_trans_val.head())
print("\n\n")

#Monthly revenue trend
month_rev = data.groupby(data['TransactionDate'].dt.to_period('M'))['TotalValue'].sum()
print("Monthly Revenue Trend:")
print()
print(month_rev)
print("\n\n")

#Sales
plt.figure(figsize=(10, 6))
prod_sales.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Purchased Products')
plt.xlabel('Product Name')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.show()

#Revenue by region
plt.figure(figsize=(10, 6))
region_rev.plot(kind='bar', color='orange')
plt.title('Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Revenue(USD)')
plt.xticks(rotation=45)
plt.show()

#Signup trend
plt.figure(figsize=(10, 6))
signup_trend.plot(kind='line', marker='o', color='green')
plt.title('Customer Signup Trend')
plt.xlabel('Month')
plt.ylabel('Number of Signups')
plt.grid()
plt.show()

#Category sales
plt.figure(figsize=(10, 6))
cat_sales.plot(kind='bar', color='purple')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.show()

#Avg transaction value by product
plt.figure(figsize=(10, 6))
avg_trans_val.head(10).plot(kind='bar', color='teal')
plt.title('Top 10 Products by Avg Transaction Value')
plt.xlabel('Product Name')
plt.ylabel('Avg Transaction Value (USD)')
plt.xticks(rotation=45)
plt.show()

#Monthly revenue trend
plt.figure(figsize=(10, 6))
month_rev.plot(kind='line', marker='o', color='red')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Revenue(USD)')
plt.grid()
plt.show()
