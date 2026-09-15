import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("SampleSuperstore.csv")
#analysis of sales according to sates
sales_by_state = df.groupby('State')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x=sales_by_state.values, y=sales_by_state.index)
plt.title("Total Sales by State")
plt.xlabel("Total Sales")
plt.ylabel("State")
plt.tight_layout()
plt.show()
#sales vs profit

totals = pd.Series({'Sales': df['Sales'].sum(), 'Profit': df['Profit'].sum()})
plt.figure(figsize=(6, 6))
sns.barplot(x=totals.index, y=totals.values)
plt.title("Total Sales vs Total Profit")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

#profit by categories

category_wise_profit=df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(x=category_wise_profit.values, y=category_wise_profit.index)
plt.title(" category wise profit")
plt.xlabel("category")
plt.ylabel("profit")
plt.tight_layout()
plt.show()

#state wise profit

state_wise_profit=df.groupby('State')['Profit'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(x=state_wise_profit.values, y=state_wise_profit.index)
plt.title(" state wise profit")
plt.xlabel("state")
plt.ylabel("profit")
plt.tight_layout()
plt.show()

#discountvsporfit

dicsount_vs_profit=pd.Series({'Discount':df['Discount'].sum(), 'Profit':df['Profit'].sum()})
plt.figure(figsize=(6, 6))
sns.barplot(x=dicsount_vs_profit.index, y=dicsount_vs_profit.values)
plt.title("Discount vs Profit")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

#sub-category wise profit

subcat_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 8))
sns.barplot(
    x=subcat_profit.values,
    y=subcat_profit.index,
    hue=subcat_profit.index,
    palette='RdYlGn',
    legend=False
)
plt.title("Sub-Category wise Profit")
plt.xlabel("Profit")
plt.ylabel("Sub-Category")
plt.axvline(0, color='red', linestyle='--', linewidth=1)
plt.tight_layout()
plt.show()

#segment wise sales
segment_wise_sales=df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(x=segment_wise_sales.values, y=segment_wise_sales.index)
plt.title(" segment wise sales")
plt.xlabel(" segment")
plt.ylabel("sales")
plt.tight_layout()
plt.show()

#shipMode wise profit
Shipmode_wise_porfit=df.groupby('Ship Mode')['Profit'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(x=Shipmode_wise_porfit.values, y=Shipmode_wise_porfit.index)
plt.title(" ShipMode wise profit")
plt.xlabel("ShipMode")
plt.ylabel("profit")
plt.tight_layout()
plt.show()
#Quantity vs Profit
tot=pd.Series({'Quantity':df['Quantity'].sum(), 'Profit':df['Profit'].sum()})
plt.figure(figsize=(6, 6))
sns.barplot(x=tot.index, y=tot.values)
plt.title("Quantity vs Profit")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()
#Sales, Quantity, Discount, Profit numeric correlations.
numeric_cols = ['Sales', 'Quantity', 'Discount', 'Profit']
corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,  # show correlation values on the cells
    fmt=".2f",  # round to 2 decimal places
    cmap='coolwarm',  # red = positive, blue = negative
    vmin=-1, vmax=1,  # fix lower bound and upper bound  scale so colors are comparable
    square=True,
    linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()