#import os and csv files
import os
import csv

# initialize variables
# names = list of candidates
# VotePerct = list of percents of each candidate's results
# VoteCounts = List of total of each candidates results
# VoteSum = value of all votes placed in election
names = []
VotePerct = []
VoteCounts = []
VoteSum = 0

#set path to election_csv file
csvpath = os.path.join("Resources", "election_data.csv")

#open the file and load the reader 
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    #read the header row
    row = next(csvreader,None)

    #analyze each line in csvreader
    for row in csvreader:

        #advance vote counter
        VoteSum += 1

        #read the first name of candidate 
        name = row[2]

        #determine if candidate has other votes  
        if name in names:
            NameID = names.index(name)
            VoteCounts[NameID] += 1

        #otherwise add candidate name and vote total to count
        else:
            names.append(name)
            VoteCounts.append(1)

#set up new variable
VoteOne = VoteCounts[0]

#counter for if statement = 0
VoteTwo = 0

#calculate percentages
for count in range(len(names)):
    
    #for each value in count to max range of names calculate percentage
    Vote_Perct = VoteCounts[count]/VoteSum*100
    
    #add value of percent to list VotePerct
    VotePerct.append(Vote_Perct)

    #determine which name has the largest count of votes
    if VoteCounts[count] > VoteOne:
        VoteOne = VoteCounts[count]
        
        #print(VoteOne)
        VoteTwo = count

#Declare winneer
winner = names[VoteTwo]

#print results to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {VoteSum}")

#rotate through range of name and print lists
for count in range(len(names)):
    print(f"{names[count]}: {VotePerct[count]}% ({VoteCounts[count]})")

#print winner name to terminal
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#set path for output file
output_file = f"Output/election_results.txt"

#call filewrite to open file above
filewriter = open(output_file, mode = 'w')

#print results to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {VoteSum}\n")

#rotate through range of names
for count in range(len(names)):
    filewriter.write(f"{names[count]}: {VotePerct[count]}% ({VoteCounts[count]})\n")

#Print to file
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()