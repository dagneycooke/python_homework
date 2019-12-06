#pybank homework

import os
import csv

# read the data file
csvpath = os.path.join("Resources", "budget_data.csv")

# create a function to calculate average from a list of numbers
def average(list):
    tally = 0
    count = 0
    for num in list:
        tally = tally + int(num)
        count = count + 1
    return round(tally/count,2)

with open(csvpath, 'r') as csvfile:

    # read the csvfile
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

    profit_loss = [] # create list to copy the data from the excel spreadsheet

    # holds the value of the greatest profit increase
    greatest_profit_increase = 0
    # holds the value of the greatest profit decrease
    greatest_profit_decrease = 0
    # holds the value for the total number of months
    months = []
    # holds the vaue for the profit change month by month
    change = []

    # read data from all rows in csv reader
    for row in csvreader: 
        months.append(row[0]) # add months to list
        profit_loss.append(int(row[1])) # add all profit/loss data to list

    # calculate the change in profit/loss month over month
    first_value = profit_loss[0]
    second_value = 0
    count = 0 # set value to 0 to loop through months
    for value in profit_loss:
        second_value = value
        profit_change = second_value - first_value
        change.append(profit_change)
        first_value = second_value

        # if the profit is greater than the already saved value, save over it, and save the month it's associate with
        if profit_change > greatest_profit_increase:
            greatest_profit_increase = profit_change
            greatest_increase = months[count]
        
        # if the loss is greater than the already saved value, save over it, and save the month it's associate with
        if profit_change < greatest_profit_decrease:
            greatest_profit_decrease = profit_change
            greatest_decrease = months[count]
        
        # increase month count
        count = count + 1

    # remove the first value from the list to compensate for the lack of change into the first month of the data set    
    change.pop(0)

# establish path to output text file
output_path = os.path.join("output.txt")

# open path to output text file
with open(output_path, 'w', newline='') as textfile: #csvfile:

    textfile.write('Financial Analysis' + '\n')
    textfile.write('-----------------' + '\n')
    textfile.write('Total Months: ' + str(len(months)) + '\n') # length of months list is number of months in file
    textfile.write('Total Profit: $' + str(sum(profit_loss)) + '\n') # sum the total net profit
    textfile.write('Average Change: $' + str(average(change)) + '\n') # average the list of change in profit for all months
    textfile.write('Greatest Increase in Profits: ' + str(greatest_increase) + " $(" + str(greatest_profit_increase) + ")" + '\n') # write the greatest increase in profits
    textfile.write('Greatest Decrease in Profits: ' + str(greatest_decrease) + " $(" +  str(greatest_profit_decrease) + ")" + '\n') # write the greatest decrease in profits
        
    # print financial analysis to terminal
    print("Financial Analysis")
    print("-----------------------------")
    print("Total Months: " + str(len(months)))
    print("Total: $" + str(sum(profit_loss)))
    print("Average Change: $" + str(average(change)))
    print("Greatest Increase in Profits: " + greatest_increase + " $(" + str(greatest_profit_increase) + ")")
    print("Greatest Decrease in Profits: " + greatest_decrease + " $(" + str(greatest_profit_decrease) + ")")

# what the output should look like (from the readme file)
#     Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
