#import modules to view paths and csv files
import os 
import csv

#navigate to csv file
os.chdir(os.path.dirname(__file__))
csv_path = os.path.join("Resources","election_data.csv")

#tools to be used in next section of code
totalVotes = 0
    #will be used to count number of rows(not including header)
candidateVotes = {}
    #dictionary that will be used to track number of votes per candidate

#open and read csv
with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    #cycle through data counting rows
    for row in csv_reader:
        totalVotes = totalVotes + 1

        #reading and depositing data into dictionary
        if row[2] not in candidateVotes:
            candidateVotes[row[2]] = 1
        else:
            candidateVotes[row[2]] += 1

#print into terminal       
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

#navigate to output file
election_file = os.path.join("Analysis", "election-results.txt")
output = open(election_file, "w")

output.write("Election Results")
output.write('\n')
output.write("-------------------------")
output.write('\n')
output.write("Total Votes: " + str(totalVotes))
output.write('\n')
output.write("-------------------------")
output.write('\n')

for candidate, votes in candidateVotes.items():
    output.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    output.write('\n')
  
output.write("-------------------------") 
output.write('\n')
output.write(f"Winner: {winner}")
output.write('\n')
output.write("-------------------------")