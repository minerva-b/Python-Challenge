# 1-Import modules:
import os
import csv

# 2-Set a path to the file we are going to read and pull data from:
budget_csv = os.path.join ('Resources','budget_data.csv')

# 6-Create lists to store the contents (aka lists) within the column 1 & 2:
dates = []
values = []

# 9-Create list to carry out my calculations:
delta = []

# 5-To help count total months you must set it to start counting at 0:
count = 0

# 3-Open, read the data in the csv file, and store and print the header row: 
with open(budget_csv , 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    # print(f"CSV Header Row: {header}")

    # 4-To count the total months by line (or row) I set a counter 
    # (since total months is essentially the total lines in the file):    
    for line in csvreader:
        count = count + 1

        # 7-Appending the columns to the new lists:
        dates.append(line[0])
        values.append(int(line[1]))

    # 8-Running a 'for loop in range' to calculate the delta (average changes), 
    # max profit (greatest increase), and great loss (greatest decrease):
    for i in range(0, len(values) - 1):
        delta.append(values[i + 1] - values[i])

    # 10-Calculations for total, delta/avg_changes, and max_profit/great_loss(aka gr increase/decrease):
    total = sum(values)
    avg_changes = round((sum(delta)) / (len(delta)), 2)
    max_profit = max(delta)
    great_loss = min(delta)

    ## (*Note: These indexes will help assign the dates to the greatest increase/decrease)
    gr_inc_index = delta.index(max_profit) + 1
    gr_dec_index = delta.index(great_loss) + 1
    ## (*Sub-note: Identifying the dates belonging to the indexes for max and min)
    max_date = dates[gr_inc_index]
    loss_date = dates[gr_dec_index]

# 11-Set a path for the new file that will contain the final analysis/report:
output_data = os.path.join('Analysis','financial_analysis.txt')

# 12-Now print it all out in the terminal and write it in an output file:
with open(output_data, 'w') as datafile:
    output_string = ("------------------------------------------------\n"
                    f"Financial Analysis: \n"
                     "------------------------------------------------\n"
                     f"Total Months: {count}\n"
                     f"Total (Net): ${total:,}\n"
                     f"Average Change: $ {avg_changes:,}\n"
                     f"Greatest Increase in Profits: {max_date} ${max_profit:,}\n"
                     f"Greatest Increase in Losses: {loss_date} ${great_loss:,}\n"
                     "------------------------------------------------\n")

    datafile.write(output_string)
    print(output_string)
    
csvfile.close()