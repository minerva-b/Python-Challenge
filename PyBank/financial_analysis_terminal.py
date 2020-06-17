import os
import csv

budget_csv = os.path.join ('Resources','budget_data.csv')

count = 0
with open(budget_csv , 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    for row in csvreader:
        count = count + 1

        

    print("Financial Analysis:")
    print("-----------------------------------")
    print(f"Total Months: {count}")
