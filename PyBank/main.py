#Nicolas Colon PyBank HW3

import csv
import os

#path to collect data from Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

#initialize variables
profit_change_list = []
total_profit = 0.0
month_counter = 0
previous_profit = 0.0
greatest_profit = 0.0
greatest_loss = 0.0

#open and read csv file
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    #skip header
    header = next(csvreader)

    #loop through data
    for row in csvreader:
        total_profit += float(row[1])
        profit_change = float(row[1]) - previous_profit 
        profit_change_list.append(profit_change)

        if float(row[1]) > greatest_profit:
            greatest_profit = float(row[1])
            greatest_profit_month = row[0] 
        elif float(row[1]) < greatest_loss:
            greatest_loss = float(row[1])
            greatest_loss_month = row[0]
        
        previous_profit = float(row[1])
        month_counter += 1
    
del profit_change_list[0]
avg_change = sum(profit_change_list)/len(profit_change_list)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_counter}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit})")
print(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})")






