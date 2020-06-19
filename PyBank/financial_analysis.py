# 1-Import modules:
import os
import csv

# 2-Set a path to the file we are going to read and pull data from:
budget_csv = os.path.join ('Resources','budget_data.csv')

# 6-Create a list to store the lists within the columns (aka row[0],row[1]):
data_results = []

# 5-To help count total months you must set it to start counting at 0:
count = 0

# 3-Open, read the data in the csv file, and store and print the header row: 
with open(budget_csv , 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    print(f"CSV Header Row: {header}")

    # 4-To count the total months by line (or row) I set a counter (since total months is essentially the total lines in the file):    
    for line in csvreader:
        count = count + 1

        # 7-Linking the columns to a readable variable:
        date = line[0]
        profit_losses = int(line[1])
        
        # 8-I appended the list from the columns to the new list so that I can link up the date with the profit/loss:
        data_results.append(
            {"Date": date,
            "Profit/Losses": profit_losses})
        
        # 9-Now I can use the actual values (now identified as integers from the 2nd column) to run calculations:
        total = sum([dates["Profit/Losses"] for dates in data_results])
        avg = round(total/count,2)
        max_profit = max([dates["Profit/Losses"] for dates in data_results])
        great_loss = min([dates["Profit/Losses"] for dates in data_results])

    # 10-I need this for loop w/ conditional so I can match/link up the profit/losses with the greatest increase (max_profit) and the greatest decrease (great_loss):
    for dates in data_results:
        if dates["Profit/Losses"] == max_profit:
            max_date = dates["Date"]

        if dates["Profit/Losses"] == great_loss:
            loss_date = dates["Date"]

# 11-Set a path for the new file that will contain the final analysis/report:
output_data = os.path.join('Analysis','financial_analysis.txt')

# 12-Now print it all out in the terminal and write it in an output file:
with open(output_data, 'w') as datafile:
    output_string = ("------------------------------------------------\n"
                    f"Financial Analysis: \n"
                     "------------------------------------------------\n"
                     f"Total Months: {count}\n"
                     f"Total (Net): ${total}\n"
                     f"Average Change: $ {avg}\n"
                     f"Greatest Increase in Profits: {max_date} ${max_profit}\n"
                     f"Greatest Increase in Losses: {loss_date} ${great_loss}\n"
                     "------------------------------------------------\n")

    datafile.write(output_string)
    print(output_string)