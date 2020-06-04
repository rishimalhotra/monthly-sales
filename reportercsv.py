# reportercsv.py

import csv
#csv_filepath = "data/products.csv"
#csv_filepath = os.path.join(os.path.dirname(__file__), "..", "sales-201710.csv")
csv_file_path = "sales-201710.csv"

total_sale = 0



with open(csv_file_path,"r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row["sales price"])
        total_sale = total_sale + float(row["sales price"])
        #total_sale = to_usd(total_sale)

def to_usd(total_sale):
    # """
    # Converts a numeric value to usd-formatted string, for printing and display purposes.

    # Param: my_price (int or float) like 4000.444444
    
    # Example: to_usd(4000.444444)
    
    # Returns: $4,000.44
    # """
    return f"${total_sale:,.2f}" #> $12,000.71
    
print("GENERATING SALES REPORT FOR THE MONTH OF OCTOBER")
print(total_sale)