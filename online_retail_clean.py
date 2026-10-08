
# PART-3

import pandas as pd
df=pd.read_csv(r"C:\Users\HP\Desktop\Arunproject2\online_retail_project.csv")
print(df)
df['Revenue'] = df['Quantity'] * df['UnitPrice']
print(df)

total_revenue = df['Revenue'].sum()
print("Total Revenue:", total_revenue)

total_quantity = df['Quantity'].sum()
print("Total Quantity Sold:", total_quantity)

total_orders = df['InvoiceNo'].nunique()
print("Total Orders:", total_orders)

unique_customers = df['CustomerID'].nunique()
print("Unique Customers:", unique_customers)

unique_products = df['ProductName'].nunique()
print("Unique Products:", unique_products)

average_unit_price = df['UnitPrice'].mean()
print("Average Unit Price:", average_unit_price)

average_order_value = total_revenue / total_orders
print("Average Order Value:", average_order_value)

highest_transaction = df['Revenue'].max()
print("Highest Single Transaction:", highest_transaction)

lowest_transaction = df['Revenue'].min()
print("Lowest Valid Transaction:", lowest_transaction)

total_countries = df['Country'].nunique()
print("Total Countries:", total_countries)

# PART-- 4
# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# Fill missing dates
df['InvoiceDate'] = df['InvoiceDate'].ffill()
# Feature columns

df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['Hour'] = df['InvoiceDate'].dt.hour
print(df[["InvoiceDate","Year","Month","Hour"]].head())

# Monthly Revenue
monthly_revenue = df.groupby(
    df['InvoiceDate'].dt.to_period('M')
)['Revenue'].sum()
print("MONTHLY REVENUE")
print(monthly_revenue)

# Highest Month
print("\nHIGHEST REVENUE MONTH")
print(monthly_revenue.idxmax(), monthly_revenue.max())

# Lowest Month
print("\nLOWEST REVENUE MONTH")
print(monthly_revenue.idxmin(), monthly_revenue.min())

# Month-to-month change
print("\nMONTHLY CHANGE")
print(monthly_revenue.diff())

# Growth %
print("\nMONTHLY GROWTH %")
print(monthly_revenue.pct_change() * 100)

# Sales Trend
if monthly_revenue.iloc[-1] > monthly_revenue.iloc[0]:
    print("\nSales are increasing")
elif monthly_revenue.iloc[-1] < monthly_revenue.iloc[0]:
    print("\nSales are decreasing")
else:
    print("\nSales are stable")

# Hour-wise Revenue
hourly_revenue = df.groupby('Hour')['Revenue'].sum()

print("\nHOUR-WISE REVENUE")
print(hourly_revenue)

# Year-wise Revenue
yearly_revenue = df.groupby('Year')['Revenue'].sum()

print("\nYEAR-WISE REVENUE")
print(yearly_revenue)

# PART--6

# Top 10 Products by Quantity
top_10_products_quantity = (
    df.groupby('ProductName')['Quantity'].sum()
    .sort_values(ascending=False).head(10))
print("Top 10 Products by Quantity:")
print(top_10_products_quantity)

# Top 10 Products by Revenue
top_10_products_revenue = (df.groupby('ProductName')
    ['Revenue'].sum().sort_values(ascending=False).head(10))
print("\nTop 10 Products by Revenue:")
print(top_10_products_revenue)

# Bottom 10 Products by Revenue
bottom_10_products_revenue = (df.groupby('ProductName')
    ['Revenue'].sum().sort_values(ascending=True).head(10))
print("\nBottom 10 Products by Revenue:")
print(bottom_10_products_revenue)

# Average Selling Price per Product
average_selling_price = (df.groupby('ProductName')
    ['UnitPrice'].mean().sort_values(ascending=False))
print("\nAverage Selling Price per Product:")
print(average_selling_price)


# PART-7

# Customer-wise Total Spending
customer_total_spending = (df.groupby('CustomerID')
    ['Revenue'].sum().sort_values(ascending=False))
print("Customer-wise Total Spending:")
print(customer_total_spending)

# Customer-wise Order Count
customer_order_count = (df.groupby('CustomerID')
    ['InvoiceNo'].nunique())
print("\nCustomer-wise Order Count:")
print(customer_order_count)

# Customer-wise Quantity Purchased
customer_quantity = (df.groupby('CustomerID')
    ['Quantity'].sum().sort_values(ascending=False))

print("\nCustomer-wise Quantity Purchased:")
print(customer_quantity)

# Customer-wise Average Order Value
customer_average_order_value = (df.groupby('CustomerID').agg(TotalRevenue=('Revenue', 'sum'),
    OrderCount=('InvoiceNo', 'nunique')))

customer_average_order_value['AverageOrderValue'] = (customer_average_order_value['TotalRevenue'] /
    customer_average_order_value['OrderCount'])

print("\nCustomer-wise Average Order Value:")
print(customer_average_order_value[['AverageOrderValue']])


# Top 10 Customers by Revenue
top_10_customers = (df.groupby('CustomerID')
    ['Revenue'].sum().sort_values(ascending=False).head(10))

print("\nTop 10 Customers by Revenue:")
print(top_10_customers)


# PART-8

# Country-wise Revenue
country_revenue = (df.groupby('Country')
    ['Revenue'].sum().sort_values(ascending=False))

print("Country-wise Revenue:")
print(country_revenue)

# Country-wise Orders
country_orders = (df.groupby('Country')
    ['InvoiceNo'].nunique().sort_values(ascending=False))

print("\nCountry-wise Orders:")
print(country_orders)

# Country-wise Customers
country_customers = (df.groupby('Country')
    ['CustomerID'].nunique().sort_values(ascending=False))

print("\nCountry-wise Customers:")
print(country_customers)

# Country-wise Quantity
country_quantity = (df.groupby('Country')
    ['Quantity'].sum().sort_values(ascending=False))

print("\nCountry-wise Quantity:")
print(country_quantity)

# Country-wise Average Order Value
country_average_order_value = (df.groupby('Country').agg(TotalRevenue=('Revenue', 'sum'),
        OrderCount=('InvoiceNo', 'nunique')))

country_average_order_value['AverageOrderValue'] = (
    country_average_order_value['TotalRevenue'] /
    country_average_order_value['OrderCount'])

print("\nCountry-wise Average Order Value:")
print(country_average_order_value[['AverageOrderValue']])

from sqlalchemy import create_engine
from urllib.parse import quote_plus
# password=quote_plus("Root@123")
engine=create_engine(f"mysql+pymysql://root:@localhost:3306/project2")

df.to_sql(name="retail_sales_data",con=engine,if_exists="replace",index=False)
