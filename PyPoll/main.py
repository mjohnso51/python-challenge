import os 
import csv

os.chdir(os.path.dirname(__file__))
csv_path = os.path.join("Resources","election_data.csv")

totalVotes = 0
candidateVotes = {}

with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
        totalVotes = totalVotes + 1

        if row[2] not in candidateVotes:
            candidateVotes[row[2]] = 1
        else:
            candidateVotes[row[2]] += 1
        
print("Election Results")
print("-------------------------")
print("Total Votes:  " + str(totalVotes))
print("-------------------------")

for candidate, votes in candidateVotes.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")

print("-------------------------")

winner = max(candidateVotes, key=candidateVotes.get)

print(f"Winner:  {winner}")
print("-------------------------")

election_file = os.path.join("Analysis", "election-results.txt")
f = open(election_file, "w")

f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(totalVotes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in candidateVotes.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
f.write("-------------------------")