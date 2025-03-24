# Import required modules
import pandas as pd
import sqlite3
 
# load data
df = pd.read_csv('retail_store_inventory.csv')
# print(df.head())
# print(df.info())

# Creating SQLite database
conn = sqlite3.connect('retail.db')
cursor = conn.cursor()

# create table
create_table_query = '''CREATE TABLE IF NOT EXISTS inventory(
                date DATE NOT NULL,
                store_id VARCHAR(4) NOT NULL,
                product_id VARCHAR(5) NOT NULL,
                category VARCHAR(20) NOT NULL,
                region VARCHAR(5) NOT NULL,
                inventory_level INTEGER NOT NULL,
                units_sold INTEGER NOT NULL,
                units_ordered INTEGER NOT NULL,
                demand_forecast DECIMAL(5, 2) NOT NULL,
                price DECIMAL(5, 2) NOT NULL,
                discount INTEGER(3) NOT NULL,
                weather_condition VARCHAR(6) NOT NULL,
                holiday_promotion BOOLEAN NOT NULL,
                competitor_pricing DECIMAL(5, 2) NOT NULL,
                seasonality VARCHAR(6) NOT NULL);
                '''

# # Creating the table into our database
cursor.execute(create_table_query)

# transform csv to sql table
# df.to_sql('inventory', conn, if_exists='append', index = False)

# import using terminal
# sqlite> .mode csv
# sqlite> .import --csv --skip 1 retail_store_inventory.csv inventory

conn.commit()
conn.close()