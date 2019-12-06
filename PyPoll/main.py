#pypoll homework

import os
import csv

# find file path to election_data.csv
csvpath = os.path.join("Resources", "election_data.csv")

# open csv file
with open(csvpath, 'r') as csvfile:

    # read in csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

    total_votes = 0 # set total votes to zero
    num_candidates = 0 # set number of candidats to zero
    candidates = [] # create list for candidates
    

    # read through csv file
    for row in csvreader:
        # increase total votes by one for each row in the file
        total_votes = total_votes + 1
        person = row[2]
        # check to see if candidate has already been voted for, and if not, add them to the list of candidates and increase candidate count by one
        if person not in candidates:
            candidates.append(row[2])
            num_candidates = num_candidates + 1

    votes = [0]*num_candidates # create list for vote tracking
# read through csv file again
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

    # now that the number of candidates has been established, count votes by candidate    
    for row in csvreader:
        for i in range(num_candidates):
            if row[2] == candidates[i]:
                votes[i] = votes[i] + 1
    
    percent_votes = [] # create list for percent of votes per candidate
    highest_win = 0 # variable to track the highest percentage
    position = 0
    count = 0

    # calculate percent votes for each candidate
    for people in votes:
        win_percent = float((people/total_votes)*100) # calculate win percentage
        percent_votes.append(win_percent) # add win percentage to list of percentages
        if win_percent > highest_win: # keep track of the highest percentage
            highest_win = win_percent
            position = count # find the position in the list that matches the highest percentage
        count = count + 1


print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(total_votes))
print("-----------------------------")

# loop through candidates and print their percentage and total votes
for i in range(num_candidates):
    print(str(candidates[i]) + ": " + str(format(percent_votes[i],'.3f')) + "% (" + str(votes[i]) + ")")
print("-----------------------------")
print("Winner: " + str(candidates[position]))
print("-----------------------------")

# establish path to output text file
output_path = os.path.join("output.txt")

# open path to output text file
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow(["Total Votes: " + str(total_votes)])
    csvwriter.writerow(["-----------------------------"])

# loop through candidates and print their percentage and total votes
    i = 0
    for i in range(num_candidates):
        csvwriter.writerow([(str(candidates[i]) + ": " + str(format(percent_votes[i],'.3f')) + "% (" + str(votes[i]) + ")")])

    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow(["Winner: " + str(candidates[position])])
    csvwriter.writerow(["-----------------------------"])

# what the output should look like (From readme file)

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
