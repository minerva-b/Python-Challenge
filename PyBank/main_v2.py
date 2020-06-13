#Adding my dependencies
import os
import csv
from csv import writer
from itertools import count

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

#Assigning my num_rows to count total_months
num_rows = 0

#Formats for results (use this if the formating in the loop doesn't work - maybe)
##formatted_float = "${:,.2f}".format(net_total)
##formatted_float1 = "${:,.2f}".format(average_change)
##formatted_float2 = "${:,.2f}".format(greatest_increase)
##formatted_float3 = "${:,.2f}".format(greatest_decrease)

#Opening the csv file and identifying items
with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for item in csvreader:

        total_months.append(count(num_rows))
        for rows in csvreader:
            num_rows += 1

        net_total.append('${:.0f}'.format(sum(int(item[1]))))
        
        #Attempting to calc the average_change
        average_change = '${:.0f}'.format(float(sum(item[1])) / ((item[1])), 2)
        print("Financial Analysis" +
              "------------------------" +
              "Total Months: " + total_months +
              "Net Total: " + net_total + 
              "Average Change: " + average_change )

        #Attempting to calc the greatest_increase
        greatest_increase = '${:.0f}'.format(round(int(max(item[1]))))

        #Attempting to calc the greatest_decrease
        greatest_decrease = '${:.0f}'.format(round(int(min(item[1]))))
        
        #Changed to insert combined operation right here for print into terminal
        for item in csvreader:
            if item[0] == greatest_increase and item[0] == greatest_decrease:
                print("Greatest Increase in Profits: " + item[0] + " (" + greatest_increase + ")" +
                      "Greatest Decrease in Losses: " + item[0] + " (" + greatest_decrease + ")")
                break

#Creating a new file for results
##new_csv = zip(total_months, net_total, average_change, greatest_increase, greatest_decrease)

##output_file = os.path.join("financial_analysis.txt")
##with open(output_file, 'w') as datafile:
    #writer.writerow(["Financial Analysis",
                    #"----------------------",
                    #"Total Months: " + total_months +
                    #"Net Total: " + net_total + 
                    #"Average Change: " + average_change +
                    #"Greatest Increase in Profits: " + " (" + greatest_increase + ") " +
                    #"Greatest Decrease in Losses: " + " (" + greatest_decrease + ") "])
                    
                    ## Return to add dates to both Increase and Decrease (right above here)