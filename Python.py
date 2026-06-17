import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('default')
df = pd.read_csv("C:\\Users\\naaga\\OneDrive\\Documents\\Documents\\Retail_Sales.csv")
df.head()
(df.isnull().sum()/len(df))*100
df.drop_duplicates(inplace = True)
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%d-%m-%Y')
## Outlier Detection
sns.boxplot(df['Revenue'])

## Profit Check
df['Calculated Profit'] = df['Revenue'] - df['Cost']
(df['Calculated Profit'] == df['Profit']).all()

## Year
df['Year'] = df['Order_Date'].dt.year

## Month
df['Month'] = df['Order_Date'].dt.month
## Quarter
df['Quarter'] = df['Order_Date'].dt.quarter

## Weekday
df['Weekday'] = df['Order_Date'].dt.day_name()

## Profit Margin
df['Profit Margin'] = (df['Profit'] / df['Revenue'])*100

## Average Order Value
AOV = (df['Revenue'].sum() / df['Order_ID'].nunique())

## Revenue Per Customer
RPC = (df['Revenue'].sum() / df['Customer_ID'].nunique())

## Total Revenue
Total_Revenue = df['Revenue'].sum()

## Total Profit
Total_Profit = df['Profit'].sum()

## Toatl Order
Total_Order = df['Order_ID'].nunique()

## Monthly Sales Trend
monthly_sales = df.groupby('Month')['Revenue'].sum()
monthly_sales.plot(kind = 'line',
                   figsize = (12,6)
                   )

## Top Customers
top_customers = (df.groupby('Customer_Name')['Revenue'].sum().sort_values(ascending=False).head(10))
top_customers.plot(kind='bar')

## Revenue by Segment
segment_sales = (df.groupby('Customer_Segment')['Revenue'].sum())

## Best Selling Products
best_products = (df.groupby('Product_Name')['Quantity'].sum().sort_values(ascending=False))

## Most Profitable Product
Profit_Products = (df.groupby('Product_Name')['Profit'].sum().sort_values(ascending=False))

## Revenue By Region
regional_sales = (df.groupby('Region')['Revenue'].sum())
regional_sales.plot(kind='bar')

## Pareto Analysis
pareto = (df.groupby('Product_Name')['Revenue'].sum().sort_values(ascending= False))
cum_prt = pareto.cumsum() / pareto.sum() * 100

## RFM Analysis
rfm = df.groupby('Customer_ID').agg({
    'Order_Date': 'max',
    'Order_ID' : 'count',
    'Revenue' : 'sum'})

## Cohort Analysis
df['OrderMonth'] = df['Order_Date'].dt.to_period('M')

## Correlation Heatmap
sns.heatmap(df[['Revenue','Cost','Profit',
                'Quantity','Unit_Price']]
                .corr(),
                annot= True)

## Sales Trend
sns.lineplot(x =monthly_sales.index,
             y = monthly_sales.values)

## Region Performance
sns.barplot(x = regional_sales.index,
            y = regional_sales.values)

## Boxplot
sns.boxplot(df['Profit'])

## Pairplot
sns.pairplot(df[['Revenue','Cost',
                 'Profit','Quantity']]
                 )
df.to_csv("cleaned_retail_sales.csv", index=False)