# Importing my modules - they will help me by using their built-in functions
import os
import csv


# Creating a file path to the CSV file (where we will collect the data for our analysis)
csvpath = os.path.join ('Resources','budget_data.csv')


# Therefore, we need to define the function (budget_data) so its our sole parameter
def print_calculations(budget_data):

    # Creating lists to identify and read given the data from budget_data.csv
    #date = str(budget_data[0]) <--- original attempt at pulling date
    
    date = str(budget_data[0])
    profit_losses = int(budget_data[1])

#    total_months = str(budget_data[0])
#    net_total = float(budget_data[1])
#    average_change = float(budget_data[1])
#    greatest_increase = float(budget_data[1])
#    greatest_decrease = float(budget_data[1])

    # Creating my calculations for the dataset
    
    lines = 0

    with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
#        for lines in open(csvpath):
#            lines += 1
    #for lines in csvreader: <--- original attempt at counting rows/lines of lists of date
    #    lines = len(list(date))
    #    count += len(list(date)) <--- original attempt at counting...
#            print(f'TESTING---Total Months: {lines}')
    #    break

    net_total = sum(profit_losses)
    average_change = round(sum(profit_losses) / len(profit_losses), 2)
    greatest_increase = round(max(profit_losses), 2)
    greatest_decrease = round(min(profit_losses), 2)

    # Find a way to link the date that matches profit/losses for greatest_increase & greatest_decrease
    # [Insert calculation here]
                
    print("Financial Analysis: ")
    print("----------------------")
#    print(f'Total Months: {total_months}')
    print(f'Net Total: {float(net_total)}')
    print(f'Average Change: {float(average_change)}')
    print(f'Greatest Increase in Profits: {float(greatest_increase)}')
    print(f'Greatest Decrease in Losses: {float(greatest_decrease)}')


# Now create loop(s) to read the lists in budget_data.csv
#with open(csvpath , 'r') as csvfile:
#    csvreader = csv.reader(csvfile, delimiter = ',')
    
#    header = next(csvreader)
    
#    for lines in csvreader:
#        print_calculations(lines)


## Writing a path for the new CSV file (aka financial_analysis.txt)
#output_path = os.path.join('Analysis','financial_analysis.txt')


## Creating the loop for the calculations to write into the new file
#with open(output_path, 'w') as datafile:
    #output_path.write(["Financial Analysis",
                    #"----------------------",
                    #"Total Months: " + total_months +
                    #"Net Total: " + net_total + 
                    #"Average Change: " + average_change +
                    #"Greatest Increase in Profits: " + " (" + greatest_increase + ") " +
                    #"Greatest Decrease in Losses: " + " (" + greatest_decrease + ") "])
                    ## Return to add dates to both Increase and Decrease (right above here)