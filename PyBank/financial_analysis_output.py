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
        
        for dates in data_results:
            if dates["Profit/Losses"] == max_profit:
                increase = dates["Date"], dates["Profit/Losses"]
            if dates["Profit/Losses"] == great_loss:
                decrease = dates["Date"], dates["Profit/Losses"]
   
output_data = os.path.join('Analysis','financial_analysis.txt')

with open(output_data, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["-------------------------------------------------------"])
    writer.writerow([" Financial Analysis:"])
    writer.writerow(["-------------------------------------------------------"])
    writer.writerow([f" Total Months: {count} "])
    writer.writerow([f" Total (Net): $ {total} "])
    writer.writerow([f" Average Change: $ {avg} "])
    writer.writerow([f" Greatest Increase in Profits: {increase} "])
    writer.writerow([f" Greatest Decrease in Losses: {decrease} "])
    writer.writerow(["--------------------------------------------------------"])