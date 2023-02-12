import pandas as pd
import os

df = pd.read_csv('sales_data/Sales_April_2019.csv') 

files = [file for file in os.listdir('sales_data')]
all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv('sales_data/'+file)
    all_months_data = pd.concat([all_months_data, df])

    print(all_months_data.to_csv('all_Sales.csv', index=False))
    