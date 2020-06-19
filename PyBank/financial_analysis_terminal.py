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
            max_date = dates["Date"]

        if dates["Profit/Losses"] == great_loss:
            loss_date = dates["Date"]


output_data = os.path.join('Analysis','financial_analysis.txt')

with open(output_data, 'w') as datafile:
    output_string = (f"Financial Analysis: \n"
                     "--------------------------------------------\n"
                     f"Total Months: {count}\n"
                     f"Total (Net): ${count}\n"
                     f"Average Change: $ {avg}\n"
                     f"Greatest Increase in Profits: {max_date} ${max_profit}\n"
                     f"Greatest Increase in Losses: {loss_date} ${great_loss}\n")

    datafile.write(output_string)
    print(output_string)