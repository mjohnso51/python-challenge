import os
import csv

os.chdir(os.path.dirname(__file__))    
csv_path = os.path.join("Resources","budget_data.csv")

month = []
profit_loss = []

total_months = 0
net_profit_loss = 0
last_month_profit_loss = 0
this_month_profit_loss = 0
change_profit_loss = 0

with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
        total_months = total_months + 1
        this_month_profit_loss = int(row[1])
        net_profit_loss = net_profit_loss + this_month_profit_loss

        if (total_months == 1):
            last_month_profit_loss = this_month_profit_loss
            continue

        else:
            change_profit_loss = this_month_profit_loss - last_month_profit_loss
            month.append(row[0])
            profit_loss.append(change_profit_loss)
            last_month_profit_loss = this_month_profit_loss

    sum_profit_loss = sum(profit_loss)
    average_profit_loss = round(sum_profit_loss/(total_months -1), 2)

    greatestPos_change = max(profit_loss)
    greatestNeg_change = min(profit_loss)
    greatestPos_index = profit_loss.index(greatestPos_change)
    greatestNeg_index = profit_loss.index(greatestNeg_change)

    best = month[greatestPos_index]
    worst = month[greatestNeg_index]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best} (${greatestPos_change})")
print(f"Greatest Decrease in Losses:  {worst} (${greatestNeg_change})")
    
financialAnalysis_file = os.path.join("Analysis", "financial-analysis.txt")
f = open(financialAnalysis_file, "w")

f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total Months:  {total_months}\n")
f.write(f"Total:  ${net_profit_loss}\n")
f.write(f"Average Change:  ${average_profit_loss}\n")
f.write(f"Greatest Increase in Profits:  {best} (${greatestPos_change})\n")
f.write(f"Greatest Decrease in Losses:  {worst} (${greatestNeg_change})\n")