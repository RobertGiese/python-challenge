import os
import csv

candidate_votes = {}

file_load = os.path.join("Resources","election_data.csv")
with open (file_load) as data:
    reader = csv.reader(data)
    header = next (reader)
    for row in reader:
        candidate = row[2]
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
total_votes = sum(candidate_votes.values())
percent = []
output = (
    f"\nElection Results\n"
    f"----------------------------\n")
print (total_votes)
for i in candidate_votes:
    percent = round((float(candidate_votes[i])/total_votes)*100,0)
    print(f" {i} : {percent}% ({candidate_votes[i]})")
    output +=  f" {i} : {percent}% ({candidate_votes[i]})\n"
for key in candidate_votes.keys():
    if candidate_votes[key] == max(candidate_votes.values()):
        winner = key
print(f" The winner is : {winner}")
output += (
    f" The winner is : {winner}")

output_path = os.path.join("Analysis", "RobertGiese2_Py.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write(output)