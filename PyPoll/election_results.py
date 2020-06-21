# 1-Import modules:
import os
import csv

# 2-Set a path to the file we are going to read and pull data from:
election_csv = os.path.join('Resources','election_data.csv')

# 6-Create a list to store the unique names:
candidate_names = []

# 5-To help count total votes you must set it to start counting at 0:
count = 0

# 9-To help count and keep track of the total votes per candidate:
total_votes_0 = 0
total_votes_1 = 0
total_votes_2 = 0
total_votes_3 = 0

# 3-Open and read the data in the csv file: 
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    print(f"CSV Header Row: {header}")

    # 4-To count the total votes by line (or row); set counter:
    for line in csvreader:
        count = count + 1

        # 7-Find out the unique names of candidates:
        if line[2] not in candidate_names:
            candidate_names.append(line[2])

        # 8-I created this new list (of unique candidate names found) so that I can use the list for further calculations:
        name_list = [
            "Khan",
            "Correy",
            "Li",
            "O'Tooley"]
        
        # 10-Find the lines (or rows) that match ea candidate so we can calc the total votes per name & percent won per name:
        if line[2] == name_list[0]:
            total_votes_0 = total_votes_0 + 1
        percent_won_0 = round((total_votes_0 / count), 3)

        if line[2] == name_list[1]:
            total_votes_1 = total_votes_1 + 1
        percent_won_1 = round((total_votes_1 / count), 3)

        if line[2] == name_list[2]:
            total_votes_2 = total_votes_2 + 1
        percent_won_2 = round((total_votes_2 / count), 3)
        
        if line[2] == name_list[3]:
            total_votes_3 = total_votes_3 + 1
        percent_won_3 = round((total_votes_3 / count), 3)
        
        # 11-Find the max votes by combining the total_votes[0-3] and find who the max_votes belongs to:
        max_votes = max(total_votes_0, total_votes_1, total_votes_2, total_votes_3)

        if total_votes_0 == max_votes:
            winner = name_list[0]
        elif total_votes_1 == max_votes:
            winner = name_list[1]
            pass
        elif total_votes_2 == max_votes:
            winner = name_list[2]
            pass
        elif total_votes_3 == max_votes:
            winner = name_list[3]
            pass

# 12-Set a path to create a new file for the poll results:
output_results = os.path.join('Analysis','poll_results.txt')

# 13-Now print it all out in the terminal and write it in an output file:
with open(output_results, 'w') as datafile:
    output_string = ("------------------------------------------------\n"
                    "Election Results: \n"
                    "------------------------------------------------\n"
                    f"Total Votes: {count:,}\n"
                    "------------------------------------------------\n"
                    f"{name_list[0]}: {percent_won_0:.3%} ({total_votes_0:,})\n"
                    f"{name_list[1]}: {percent_won_1:.3%} ({total_votes_1:,})\n"
                    f"{name_list[2]}: {percent_won_2:.3%} ({total_votes_2:,})\n"
                    f"{name_list[3]}: {percent_won_3:.3%} ({total_votes_3:,})\n"
                    "------------------------------------------------\n"
                    f"Winner: {winner}\n"
                    "------------------------------------------------\n")
    datafile.write(output_string)
    print(output_string)

csvfile.close()