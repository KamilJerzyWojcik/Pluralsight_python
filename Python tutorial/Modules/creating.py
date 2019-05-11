import sys
from ecommerce.shopping import sales

print(sys.path[2])

sales.calc_tax()
sales.calc_shipping()

print("----start-----")
#print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)
