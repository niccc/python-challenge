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
        #update total 
        total_profit += float(row[1])
        #calculate change in profit
        profit_change = float(row[1]) - previous_profit 
        #store change in progit
        profit_change_list.append(profit_change)

        #determine the greatest profit/loss
        if float(row[1]) > greatest_profit:
            greatest_profit = float(row[1])
            greatest_profit_month = row[0] 
        elif float(row[1]) < greatest_loss:
            greatest_loss = float(row[1])
            greatest_loss_month = row[0]
        
        #save current profit value for use in next iteration as previous profit
        previous_profit = float(row[1])
        
        #countin months 
        month_counter += 1
#getting rid of bogus first value in the profit change list    
del profit_change_list[0]
avg_change = sum(profit_change_list)/len(profit_change_list)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_counter}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit})")
print(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})")

#write to file
output_path = os.path.join('.', 'output_file.txt')
with open(output_path, 'w') as output_file:
    print("Financial Analysis", file = output_file)
    print("----------------------------", file = output_file)
    print(f"Total Months: {month_counter}", file = output_file)
    print(f"Total: ${total_profit}", file = output_file)
    print(f"Average Change: ${avg_change}", file = output_file)
    print(f"Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit})", file = output_file)
    print(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss})", file = output_file)        




