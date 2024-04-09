import csv # Imports the csv library

totalCost = 0.0
totalQuantity = 0.0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file) 
 
  for row in reader: 
    totalCost += float(row["Cost"]) * float(row["Quantity"])
    totalQuantity += int(row["Quantity"])

print(f"\nTotal: ${round(totalCost,2)}")
print(f"\nTotal Quantity: {round(totalQuantity)}")

  

