import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
outputpath = os.path.join('..', 'Solved', 'output.txt')

Voters = []
Counties = []
Candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader: 
        Voters.append(row[0])
        Counties.append(row[1])
        Candidates.append(row[2]) 

def printOutput(Voters, Counties, Candidates):
    khanVotes = Candidates.count("Khan")
    correyVotes = Candidates.count("Correy")
    liVotes = Candidates.count("Li")
    otooleyVotes = Candidates.count("O'Tooley")
    resultsDict = {"Khan": khanVotes, "Correy": correyVotes, "Li": liVotes, }
    totalvotes = len(Voters)
    khanpct = round((khanVotes/totalvotes)*100, 3)
    correypct = round((correyVotes/totalvotes)*100, 3)
    otpct = round((otooleyVotes/totalvotes)*100, 3)
    lipct = round((liVotes/totalvotes)*100, 3)
    winner = max(resultsDict, key=resultsDict.get)
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(totalvotes))
    print("-------------------------")
    print('Khan: ' + str(khanpct) + '% (' + str(khanVotes) + ')')
    print("Correy: " + str(correypct) + '% (' + str(correyVotes) + ')')
    print('Li: ' + str(lipct) + '% (' + str(liVotes) + ')')
    print("O'Tooley: " + str(otpct) + '% (' + str(otooleyVotes) + ')')
    print("-------------------------")
    print("Winner: " + winner)

# print to terminal
printOutput(Voters, Counties, Candidates)

# print to txt
import sys
with open(outputpath, 'w') as f:
    sys.stdout = f
    printOutput(Voters, Counties, Candidates)