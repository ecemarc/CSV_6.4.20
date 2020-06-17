import csv
import itertools
import operator
from operator import itemgetter
import os


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"  # > $12,000.71


print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2018")

rows = []
csv_file_path = "sales-201710.csv"  # a relative filepath
total_price = 0
with open(csv_file_path, "r") as csv_file:  # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file)  # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers

    for row in reader:
        total_price = total_price + float(row["sales price"])
        # print(row["unit price"], row["sales price"])
        # converting rows to dictionaries to be able to iterate
        rows.append(dict(row))

product_sales = []
# sales_price1 = [float(row["sales price"]) for row in rows]


sorted_rows = sorted(rows, key=itemgetter("product"))

group_by_product = itertools.groupby(sorted_rows, key=itemgetter("product"))

for product, product_by_row in group_by_product:
    monthly_sales = sum([float(row["sales price"])
                         for row in product_by_row])  # adding same item sales
    # creating a new list that has each item once with total sales
    product_sales.append({"name": product, "monthly_sales": monthly_sales})


sorted_by_sale = sorted(product_sales, key=itemgetter(
    "monthly_sales"), reverse=True)  # sorting the items by sale and taking top 3

top_seller = sorted_by_sale[0:3]


def to_usd(total_price):
    return f"${total_price:,.2f}"


for ts in top_seller:
    top_seller_name = ts["name"]
    top_seller_sales = to_usd(ts["monthly_sales"])
    print(top_seller_name + top_seller_sales)


print("TOTAL SALES: " + to_usd(total_price))
# sales = pd.read_csv(csv_filepath)
# sales.groupby(level="sales price").max
# print(sales)


# def by_sales(sales):
#     return sales["sales price"]


# sorted_by_sales = sorted(to_float, key=by_sales)
