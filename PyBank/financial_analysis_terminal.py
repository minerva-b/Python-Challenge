import os
import csv

budget_csv = os.path.join ('Resources','budget_data.csv')

data_results = []

count = 0

with open(budget_csv , 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    for line in csvreader:
        count = count + 1

        date = line[0]
        profit_losses = int(line[1])
        

        data_results.append(
            {"Date": date,
            "Profit/Losses": profit_losses})
        total = sum([dates["Profit/Losses"] for dates in data_results])
        avg = round(total/count,2)
        max_profit = max([dates["Profit/Losses"] for dates in data_results])
        great_loss = min([dates["Profit/Losses"] for dates in data_results])
   
    print("-----------------------------------")
    print("Financial Analysis:")
    print("-----------------------------------")
    print(f"Total Months: {count}")
    print(f"Total (Net): $ {total}")
    print(f"Average Change: $ {avg}")
    for dates in data_results:
        if dates["Profit/Losses"] == max_profit:
            print("Greatest Increase in Profits: " + dates["Date"] + " ($" , dates["Profit/Losses"] , ")")
        if dates["Profit/Losses"] == great_loss:
            print("Greatest Decrease in Losses: " + dates["Date"] + " ($" , dates["Profit/Losses"] , ")")
    print("-----------------------------------")   