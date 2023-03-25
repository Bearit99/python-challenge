import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

#open and read csv file
with open(budget_data) as csvfile:
 file = csv.reader(csvfile, delimiter=',')
 header = next(file)

#Create empty lists
 dates = []
 profits = []
 
 #Add the two rows values into the lists, 2nd row as intergers for profit
 for row in file:
      dates.append(row[0])
      profits.append(int(row[1]))

#number of months by counting length of months list
months = len(dates)

#Total of profits by adding list together
total_profit = sum(profits)

#changes in profits over time
profit_change = []

for x in range(1, len(profits)):
    each_change = (profits[x] - profits[x-1])
    profit_change.append(each_change)

#average of changes
avg_change = sum(profit_change) / len(profit_change)

#greatest increase and decrease in profit changes
profit_increase = max(profit_change)
profit_decrease = min(profit_change)


print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {profit_increase}")
print(f"Greatest Decrease in Profits: {profit_decrease}")

with open("analysis.txt", "w") as f:
 f.write("Financial Analysis\n")
 f.write("---------------------------------\n")
 f.write(f"Total Months: {months}\n")
 f.write(f"Total: ${total_profit}\n")
 f.write(f"Average Change: ${avg_change:.2f}\n")
 f.write(f"Greatest Increase in Profits: {profit_increase}\n")
 f.write(f"Greatest Decrease in Profits: {profit_decrease}\n")

