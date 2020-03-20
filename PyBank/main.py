import os
import csv

total_months = 0
month_of_change = []
net_change = []
greatest_increase = ["",0]
greatest_decrease = ["", 99999999999]
total_net = 0

file_load = os.path.join("Resources","budget_data.csv")
with open (file_load) as data:
    reader = csv.reader(data)
    header = next (reader)
    first_data = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_data[1])
    previous_net = int(first_data[1])
    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change = net_change + [change]
        month_of_change = month_of_change + [row[0]]
        #calculate the greatest increase
        if change > greatest_increase [1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        if change < greatest_decrease [1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change
average_monthly_net = sum(net_change)/len(net_change)
print (total_months)
print(average_monthly_net)
print(greatest_increase)
print(greatest_decrease)
print(total_net)
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${average_monthly_net:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
output_path = os.path.join("Analysis", "RobertGiese_Py.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write(output)
