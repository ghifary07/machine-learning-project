# Import required modules
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Connect to SQLite database
conn = sqlite3.connect('retail.db')
cursor = conn.cursor()

# Printing table data
# print(pd.read_sql('''SELECT * FROM inventory
#                   LIMIT 10''', conn))

# function for sum of units per categories
def sum_units(table_name, quantity):
    df = pd.read_sql(f'''SELECT category, SUM({quantity}) AS total, SUM(inventory_level) AS stock
                     FROM {table_name} GROUP BY category ORDER BY total DESC''', conn)
    return df

# function for average price per categories
def avg_price(table_name, price, priceComp):
    df = pd.read_sql(f'''SELECT category, AVG({price}) AS avg_price, AVG({priceComp}) AS avg_priceComp
                     FROM {table_name} GROUP BY category''', conn)
    return df

def units_per_day(table_name, cat, quantity):
    df = pd.read_sql(f'''SELECT category, SUM({quantity}) AS total, date
                     FROM {table_name} WHERE category="{cat}"
                     GROUP BY date ORDER BY date ASC''', conn)
    return df

def inventory_analysis(table_name, store):
    df = pd.read_sql(f'''SELECT category, AVG(demand_forecast) AS demands, inventory_level
                     FROM {table_name} WHERE store_id="{store}"
                     GROUP BY category ORDER BY category ASC''', conn)
    return df

# total units sold per categories
df_total_sold = sum_units('inventory', 'units_sold')
print(df_total_sold)

# total units ordered per categories
df_total_ordered = sum_units('inventory', 'units_ordered')
print(df_total_ordered)

# average price compared to competitor
df_avg_price = avg_price('inventory', 'price', 'competitor_pricing')
print(df_avg_price)

# total furniture sold per day
df_furniture_sold = units_per_day('inventory', 'Furniture', 'units_sold')
print(df_furniture_sold)

# total clothing sold per day
df_clothing_sold = units_per_day('inventory', 'Clothing', 'units_sold')
print(df_clothing_sold)

# total toys sold per day
df_toys_sold = units_per_day('inventory', 'Toys', 'units_sold')
print(df_toys_sold)

# total groceries sold per day
df_groceries_sold = units_per_day('inventory', 'Groceries', 'units_sold')
print(df_groceries_sold)

# total electronics sold per day
df_electronics_sold = units_per_day('inventory', 'Electronics', 'units_sold')
print(df_electronics_sold)

# product inventory and demand of store 1
df_store_1_inventory = inventory_analysis('inventory', 'S001')
print(df_store_1_inventory)

# product inventory and demand of store 2
df_store_2_inventory = inventory_analysis('inventory', 'S002')
print(df_store_2_inventory)

# product inventory and demand of store 3
df_store_3_inventory = inventory_analysis('inventory', 'S003')
print(df_store_3_inventory)

# product inventory and demand of store 4
df_store_4_inventory = inventory_analysis('inventory', 'S004')
print(df_store_4_inventory)

# product inventory and demand of store 5
df_store_5_inventory = inventory_analysis('inventory', 'S005')
print(df_store_5_inventory)

## Visualization
def total_vis(category, values, title):
    plt.barh(category, values, color='green')

    # Adjust x-axis limits for better spacing
    plt.xlim(0, max(values) + 5)

    # Add labels, aligning them inside the bars
    for i, v in enumerate(values):
        plt.text(v - 3, i, f'{v:.0f}', va='center', ha='right', color='white', fontsize=12, fontweight='bold')

    # Add labels
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title(title)
    plt.legend()
    plt.show()

def price_comparison(category, value1, value2):
    x = np.arange(len(df_avg_price))  # X positions for bars
    width = 0.4  # Bar width
    plt.bar(x - width/2, value1, width=width, label='average price', color='blue')
    plt.bar(x + width/2, value2, width=width, label='competitor average price', color='orange')

    # Add labels
    plt.xticks(x, category)
    plt.xlabel('Categories')
    plt.ylabel('Average price')
    plt.title('Average price comparison')
    plt.legend()
    plt.show()

def unit_sold_date(category, date, value):
    # value smoothing
    value = value.rolling(window=7).mean() 

    plt.figure(figsize=(10, 5))
    plt.plot(date, value, marker='o', linestyle='-', color='blue', label='total units sold per day')

    # Formatting
    # Show every 5th date label
    plt.xticks(date[::30], rotation=45)

    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(f'total {category[1]} sold per day')
    plt.xticks(rotation=45)  # Rotate dates for readability
    plt.grid(True)
    plt.legend()

    plt.show()

# total units sold per categories
total_vis(df_total_sold['category'], df_total_sold['total'], 'total units sold per categories')

# total units ordered per categories
total_vis(df_total_ordered['category'], df_total_ordered['total'], 'total units ordered per categories')

# average price comparison
price_comparison(df_avg_price['category'], df_avg_price['avg_price'], df_avg_price['avg_priceComp'])

# total furniture sold per day
unit_sold_date(df_furniture_sold['category'], df_furniture_sold['date'], df_furniture_sold['total'])

# total clothing sold per day
unit_sold_date(df_clothing_sold['category'], df_clothing_sold['date'], df_clothing_sold['total'])

# total toys sold per day
unit_sold_date(df_toys_sold['category'], df_toys_sold['date'], df_toys_sold['total'])

# total groceries sold per day
unit_sold_date(df_groceries_sold['category'], df_groceries_sold['date'], df_groceries_sold['total'])

# total electronics sold per day
unit_sold_date(df_electronics_sold['category'], df_electronics_sold['date'], df_electronics_sold['total'])

conn.commit()
conn.close()