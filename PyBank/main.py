#import modules to view paths and read csv files
import os
import csv

#navigate to csv file
os.chdir(os.path.dirname(__file__))    
csv_path = os.path.join("Resources","budget_data.csv")

#define variables
month = []
profit_loss = []

total_months = 0
net_profit_loss = 0
last_month_profit_loss = 0
this_month_profit_loss = 0
change_profit_loss = 0

#open and read csv file
with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    #cycle through data, excluding header, and count rows
    for row in csv_reader:
        total_months = total_months + 1
        #add the total profits and losses over the whole time period
        this_month_profit_loss = int(row[1])
        net_profit_loss = net_profit_loss + this_month_profit_loss

        #make the value of last month the value of this month
        if (total_months == 1):
            last_month_profit_loss = this_month_profit_loss
            continue

        #find change in profit/loss
        else:
            change_profit_loss = this_month_profit_loss - last_month_profit_loss
            month.append(row[0])
            profit_loss.append(change_profit_loss)
            #make the value of this month the value of next month
            last_month_profit_loss = this_month_profit_loss

    #find required values for assignment
    sum_profit_loss = sum(profit_loss)
    average_profit_loss = round(sum_profit_loss/(total_months -1), 2)
    greatestPos_change = max(profit_loss)
    greatestNeg_change = min(profit_loss)

    #finds the index value of best and worst changes over the time frame
    greatestPos_index = profit_loss.index(greatestPos_change)
    greatestNeg_index = profit_loss.index(greatestNeg_change)

    #assign best and worst months
    best = month[greatestPos_index]
    worst = month[greatestNeg_index]

#print to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best} (${greatestPos_change})")
print(f"Greatest Decrease in Losses:  {worst} (${greatestNeg_change})")
    
#find output file
financialAnalysis_file = os.path.join("Analysis", "financial-analysis.txt")
output = open(financialAnalysis_file, "w")

#write into output file
output.write("Financial Analysis\n")
output.write("----------------------------\n")
output.write(f"Total Months:  {total_months}\n")
output.write(f"Total:  ${net_profit_loss}\n")
output.write(f"Average Change:  ${average_profit_loss}\n")
output.write(f"Greatest Increase in Profits:  {best} (${greatestPos_change})\n")
output.write(f"Greatest Decrease in Losses:  {worst} (${greatestNeg_change})\n")