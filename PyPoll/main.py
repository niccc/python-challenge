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

    for row in csvreader:
        if row[2] in candidate_dict: #might need to change to candidate_dict.keys
            candidate_dict[row[2]] += 1
        else:
            candidate_dict[row[2]] = 1
print(candidate_dict)
