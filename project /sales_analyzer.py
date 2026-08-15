import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Laptop", "Mouse", "Monitor", "Keyboard",
        "Laptop", "Mouse", "Monitor", "Keyboard", "Laptop"
    ],

    "Quantity": [
        2, 10, 6, 3,
        1, 15, 4, 8,
        2, 20, 5, 12, 3
    ],

    "Price": [
        55000, 800, 1500, 12000,
        55000, 800, 12000, 1500,
        55000, 800, 12000, 1500, 55000
    ],

    "Region": [
        "North", "South", "East", "West",
        "East", "North", "South", "West",
        "South", "East", "North", "South", "West"
    ]
}


df = pd.DataFrame(data)

# Calculate total sales
df["Total Sales"] = df["Quantity"] * df["Price"]


print("\n========== SALES DATA ANALYZER ==========\n")

print(df)


# Total revenue
total_revenue = df["Total Sales"].sum()

print("\nTotal Revenue:", total_revenue)


# Best selling product
product_quantity = df.groupby("Product")["Quantity"].sum()

print("\nQuantity Sold:")
print(product_quantity)

best_product = product_quantity.idxmax()

print("\nBest Selling Product:", best_product)


# Revenue by product
product_revenue = df.groupby("Product")["Total Sales"].sum()

print("\nRevenue by Product:")
print(product_revenue)


# Revenue by region
region_revenue = df.groupby("Region")["Total Sales"].sum()

print("\nRevenue by Region:")
print(region_revenue)


# Product revenue chart
plt.figure(figsize=(8, 5))

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# Region revenue chart
plt.figure(figsize=(8, 5))

region_revenue.plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# install this for run your code 
# pip install pandas matplotlib
# use this for run 
# python sales_analyzer.py
