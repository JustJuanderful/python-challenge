import os
import csv

budgetData_csv = os.path.join("..", "PyBank", "budget_data.csv")

with open(budgetData_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    totalMonths = 0
    totalProfitLoss = 0
    val = 0
    delta = 0
    dates = []
    profits = []

    csv_header = next(csv_reader)

    row1 = next(csv_reader)
    totalMonths += 1
    totalProfitLoss += int(row1[1])
    val = int(row1[1])
     
    for row in csv_reader:
        
        dates.append(row[0])
        
        delta = int(row[1])-val
        profits.append(delta)
        val = int(row[1])
        
        totalMonths += 1

        totalProfitLoss = totalProfitLoss + int(row[1])

    greatestProfInc = max(profits)
    greatestProfIndex = profits.index(greatestProfInc)
    greatestProfDate = dates[greatestProfIndex]
 
    greatestProfDec = min(profits)
    greatestLossIndex = profits.index(greatestProfDec)
    greatestLossDate = dates[greatestLossIndex]

    avgProfChange = sum(profits)/len(profits)
    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: ${str(totalProfitLoss)}")
print(f"Average Change: ${str(round(avgProfChange,2))}")
print(f"Greatest Increase in Profits: {greatestProfDate} (${str(greatestProfInc)})")
print(f"Greatest Decrease in Profits: {greatestLossDate} (${str(greatestProfDec)})")

output = open("financialAnalysis.txt", "w")

line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = str(f"Total Months: {str(totalMonths)}")
line4 = str(f"Total: ${str(totalProfitLoss)}")
line5 = str(f"Average Change: ${str(round(avgProfChange,2))}")
line6 = str(f"Greatest Increase in Profits: {greatestProfDate} (${str(greatestProfInc)})")
line7 = str(f"Greatest Decrease in Profits: {greatestLossDate} (${str(greatestProfDec)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))