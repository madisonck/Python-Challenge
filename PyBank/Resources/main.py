#Begin
import os
import csv

#Counters and Collectors
count = 0
net_rev_loss = 0 
last_rev_loss = 0
cur_rev_loss = 0
rev_change = 0

#Lists
months =[]
rev_chgs =[]

#path of csv file
budget_data = os.path.join("Resources", "budget_data.csv")

#open and read csv
with open(budget_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # read the header row first
    csv_header = next(csvfile)
            
    # read through each row of data after the header
    for row in csv_reader:

        count += 1
        cur_rev_loss = int(row[1])
        net_rev_loss += cur_rev_loss

        if (count == 1):
         
            last_rev_loss = cur_rev_loss
            
            continue

        else:

            rev_change = cur_rev_loss - last_rev_loss
            months.append(row[0])
            rev_chgs.append(rev_change)
            last_rev_loss = cur_rev_loss

    #calculations and analysis
    sum_rev = sum(rev_chgs)
    avg_rev = round(sum_rev/(count - 1), 2)
    max_rev = max(rev_chgs)
    min_rev = min(rev_chgs)
    max_month_index = rev_chgs.index(max_rev)
    min_month_index = rev_chgs.index(min_rev)
    best = months[max_month_index]
    worst = months[min_month_index]

#print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count}")
print(f"Total:  ${sum_rev}")
print(f"Average Change:  ${avg_rev}")
print(f"Greatest Increase in Profits:  {best} (${max_rev})")
print(f"Greatest Decrease in Losses:  {worst} (${min_rev})")


#export a text file with the results
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count}\n")
    outfile.write(f"Total:  ${sum_rev}\n")
    outfile.write(f"Average Change:  ${avg_rev}\n")
    outfile.write(f"Greatest Increase in Profits:  {best} (${max_rev})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst} (${min_rev})\n")