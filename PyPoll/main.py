#Nicolas Colon PyPoll HW3

import csv
import os

# join the path
election_data_csv = os.path.join('.', 'Resources', 'election_data.csv')

#read the csv file
with open(election_data_csv, 'r') as csvfile:

    #split the csv data by commas
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skip the header
    header = next(csvreader)

    #make dictionary to add unique candidate name to, and tally votes
    candidate_dict = {}
#check if dictionary already has candidate and add if not
    for row in csvreader:
        if row[2] in candidate_dict: 
            candidate_dict[row[2]] += 1
        else:
            candidate_dict[row[2]] = 1

#print everything
total_votes = sum(candidate_dict.values())
winner = max(candidate_dict, key = candidate_dict.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_dict:
    vote_percent = 100*(candidate_dict[candidate]/total_votes)
    print(f"{candidate}: {vote_percent}% ({candidate_dict[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")