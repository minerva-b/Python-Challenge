#Adding my dependencies
import os
import csv
from csv import writer

#Create file path
csvpath = os.path.join('..','Resources','budget_data.csv')

#Create my lists
total_months = []
net_total = []
average_change = []
greatest_increase = []
greatest_decrease = []
#Attempt to add month-year to results
increase_date = []
decrease_date = []

#Opening the csv file and identifying items
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for item in csvreader:
        total_months.append(sum(item[0]))
        net_total.append(sum(item[1]))
        
        #Attempting to calc the average_change
        average_change = round(int(sum(item[1])) / len(item[1]), 2)

        #Attempting to calc the greatest_increase
        greatest_increase = round(int(max(item[1])), 2)
        #Insert here the formula to attach date associated with the max value

        #Attempting to calc the greatest_decrease
        greatest_decrease = round(int(min(item[1])), 2)
        #Insert here the formula to attach date associated with min value

#Creating a new file for results
new_csv = zip(total_months, net_total, average_change, greatest_increase, greatest_decrease)

output_file = os.path.join("financial_analysis.txt")
with open(output_file, 'w') as datafile:
    writer.writerow(["Financial Analysis",
                    "----------------------",
                    "Total Months: " + total_months +
                    "Net Total: " + net_total + 
                    "Average Change: " + average_change +
                    "Greatest Increase in Profits: " + greatest_increase +
                    "Greatest Decrease in Losses: " + greatest_decrease ])
                    ## Return to add dates to both Increase and Decrease (right above here)