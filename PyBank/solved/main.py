import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
outputpath = os.path.join('..', 'Solved', 'output.txt')
monthcount = 0
totalpnl = 0
maxpnl = 0
minpnl = 0
lastrowpnl = 0
change = 0
total_change = 0
minmonth = ""
maxmonth = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        
        thispnl = float(row[1])
        change = thispnl - lastrowpnl
        total_change = total_change + change
        if thispnl >= maxpnl: 
            maxpnl = change
            maxmonth = row[0]
        if thispnl <= minpnl:
            minpnl = change
            minmonth = row[0]
        monthcount += 1
        totalpnl = totalpnl + thispnl
        if lastrowpnl == 0 :
            total_change = 0 
        lastrowpnl = thispnl

avg_change = total_change/(monthcount-1)

# print the output 
def printResults(monthcount, totalpnl, avg_change, maxmonth, minmonth, maxpnl, minpnl):
    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(monthcount))
    print("Total PnL: ${:,}".format(totalpnl))
    print("Average Change: ${:,}".format(avg_change))
    print('Greatest Increase in Profits: ' + str(maxmonth) + " ${:,}".format(maxpnl))
    print('Greatest Decrease in Profits: ' + str(minmonth) + " ${:,}".format(minpnl))

printResults(monthcount,totalpnl, avg_change, maxmonth, minmonth, maxpnl, minpnl)

import sys
with open(outputpath, 'w') as f:
    sys.stdout = f
    printResults(monthcount,totalpnl, avg_change, maxmonth, minmonth, maxpnl, minpnl)
