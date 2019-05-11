import csv
#
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([100, 12, 5])
#     writer.writerow([120, 10, 7])


with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)