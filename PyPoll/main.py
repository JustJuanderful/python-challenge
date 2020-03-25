import os
import csv

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

pollData_csv = os.path.join("..", "PyPoll", "election_data.csv")

candidateList = []

percentVotesWon = []

totalVotesWon = []
 
numVotes = 0

with open(pollData_csv, newline = "") as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)

    for row in csv_reader:
         
        numVotes += 1 

        if row[2] not in candidateList:

            candidateList.append(row[2])
            index = candidateList.index(row[2])
            totalVotesWon.append(1)

        else:

            index = candidateList.index(row[2])
            totalVotesWon[index] += 1
    
    for votes in totalVotesWon:

        percentage = (votes / numVotes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentVotesWon.append(percentage)
    
    win = max(totalVotesWon)
    index = totalVotesWon.index(win)
    winnerCandidate = candidateList[index]


print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(numVotes)}")
print("-------------------------")

for i in range(len(candidateList)):
    
    print(f"{candidateList[i]}: {str(percentVotesWon[i])} ({str(totalVotesWon[i])})")

print("-------------------------")
print(f"Winner: {winnerCandidate}")
print("-------------------------")

output = open("output.txt", "w")
line1 = "Election Results"
line2 = "-------------------------"
line3 = str(f"Total Votes: {str(numVotes)}")
line4 = str("-------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))

for i in range(len(candidateList)):

    line = str(f"{candidateList[i]}: {str(percentVotesWon[i])} ({str(totalVotesWon[i])})")
    output.write('{}\n'.format(line))

line5 = "-------------------------"
line6 = str(f"Winner: {winnerCandidate}")
line7 = "-------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))