# First import os module
import os
import csv 

# Set path for file
csvpath = os.path.join('.', 'budget_data.csv')

# variables
monthly_changes = []
total_months = 0
month_count = []
net_pnl = 0
greatest_increase = 0
greatest_month_increase = 0
greatest_decrease = 0
greatest_month_decrease = 0

# Open csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read header
    csv_header = next(csvreader)
    row = next(csvreader)

    # Define each variable
    previous_row = int(row[1])
    total_months += 1
    net_pnl += int(row[1])
    greatest_increase = int(row[1])
    greatest_month_increase = row[0]
    
    # Read each row
    for row in csvreader:

        # Find the total number of months
        total_months += 1

        # Find Net pnl
        net_pnl += int(row[1])

        # Find change from month to month
        pnl_change = int(row[1]) - previous_row
        monthly_changes.append(pnl_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        # Find greatest increase/decrease
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_month_increase = row[0]

        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_month_decrease = row[0]

    highest_change = max(monthly_changes)
    lowest_change = min(monthly_changes)
    
    # Find average change
    average_change = sum(monthly_changes)/ len(monthly_changes)

# Print
print("Financial Analysis")
print("---------------------------------")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(net_pnl))
print("Average Change: " + "$" + str(int(average_change)))
print("Greatest Increase in Profits: " + str(greatest_month_increase) + " ($" + str(highest_change)+ ")")
print("Greatest Decrease in Profits: " + str(greatest_month_decrease) + " ($" + str(lowest_change)+ ")")

with open('financial_analysis.txt', 'w') as text:
    text.write(" Financial Analysis"+ "\n")
    text.write("---------------------------------\n")
    text.write(" Total Months: " + str(total_months) + "\n")
    text.write(" Total Profits: " + str(net_pnl) + "\n")
    text.write(" Average Change: " + str(int(average_change)) + "\n")
    text.write(" Greatest Increase in Profits: " + str(greatest_month_increase) + " ($" + str(highest_change) + ")\n")
    text.write(" Greatest Decrease in Profits: " + str(greatest_month_increase) + " ($" + str(lowest_change) + ")\n")
