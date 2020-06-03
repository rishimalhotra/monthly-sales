# reporter.py

import os
import pandas
#csv_filepath = "data/products.csv"
#csv_filepath = os.path.join(os.path.dirname(__file__), "..", "sales-201710.csv")
sales = pandas.read_csv("sales-201710.csv")

#breakpoint()


df = pandas.read_csv(csv_filepath)
print(type(df)) #> <class 'pandas.core.frame.DataFrame'>
print(df.head()) #> prints first few rows
products = df.to_dict("records")

#def to_usd(my_price):
    # """
    # Converts a numeric value to usd-formatted string, for printing and display purposes.

    # Param: my_price (int or float) like 4000.444444
    
    # Example: to_usd(4000.444444)
    
    # Returns: $4,000.44
    # """
    # return f"${my_price:,.2f}" #> $12,000.71

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")