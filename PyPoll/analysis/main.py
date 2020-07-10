# import os module
import os
# import CSV
import csv

# csv path
csvpath = os.path.abspath("../Resources/PyPoll_Resources_election_data.csv")
# open with reader
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip  header
    csv_header = next(csvfile)

    # defining variables
    row_count = 0
    candidates = {}
    percent_votes = 0
    num_votes = 0
    winner = 0
    highest_num = 0

    for row in csvreader:
        # uniqify with the use of a list, but checking if the string is "in" it or not.
        name = row[2]
        if name not in candidates:
            candidates[name] = [1]
        else:
            candidates[name][0] = candidates[name][0] + 1
        # counting number of votes
        num_votes = num_votes + 1
    # printing output to terminal
    print('Election Results')
    print('--------------------------')
    print(f'Total Votes:{num_votes}')
    print('--------------------------')

    # writing output to txt file
    file = open('Pypoll.txt', 'w')
    file.write('Election Results\n')
    file.write('--------------------------\n')
    file.write('Total Votes:{num_votes}\n')
    file.write('--------------------------\n')

    # percentage of votes
    for key, value in candidates.items():
        # calulating percent of votes each candidate won
        percent_votes = round((value[0]/num_votes)*100, 1)
        candidates[key].append(percent_votes)

    for key, value in candidates.items():

        # Get winning candidate:
        winner = max(candidates.values())
        results = [key for key, value in candidates.items() if value == winner]
        # printing output to terminal
        print(f'{key} {value[1]} % ({value[0]})')
    # printing to txt file
    file.write(f'{key} {value[1]} % ({value[0]})\n')
    file.write('-------------------------\n')
    file.write(f'Winner: {results}\n')
    file.write('-------------------------\n')

# printing output to terminal
print('-------------------------')
print(f'Winner: {results}')
print('-------------------------')

# closing txt file
file.close()
