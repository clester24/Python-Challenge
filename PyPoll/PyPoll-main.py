# First import os module
import os
import csv

# Set path for file
csvpath = os.path.join('.', 'PyPoll', 'election_data.csv')

# Variables
total_election_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0

#Open csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header
    csv_header = next(csvreader)

    # Read each row
    for row in csvreader:

        # Find the total number of votes in the election
        total_election_votes += 1

        # Find the total number of votes for each candidate
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif (row[2] == "Correy"):
            Correy_votes += 1
        elif (row[2] == "Li"):
            Li_votes += 1
        else:
            Otooley_votes += 1
    
    # Find the vote percentage for each candidate
    Vote_Percentage_Khan = Khan_votes / total_election_votes
    Vote_Percentage_Correy = Correy_votes / total_election_votes
    Vote_Percentage_Li = Li_votes / total_election_votes
    Vote_Percentage_Otooley = Otooley_votes / total_election_votes

    Winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)

    if Winner == Khan_votes:
        election_winner = "Khan"
    elif Winner == Correy_votes:
        election_winner = "Correy"
    elif Winner == Li_votes:
        election_winner = "Li"
    else:
        election_winner = "O'Tooley"

# Print
print("Election Results")
print("-------------------------")
print("Total Votes :" + str(total_election_votes))
print("-------------------------")
print("Khan: " + str(round(Vote_Percentage_Khan * 100)) +"% (" + str(Khan_votes)+ ")")
print("Correy: " + str(round(Vote_Percentage_Correy * 100)) +"% (" + str(Correy_votes)+ ")")
print("Li: " + str(round(Vote_Percentage_Li * 100)) +"% (" + str(Li_votes)+ ")")
print("O'Tooley: " + str(round(Vote_Percentage_Otooley * 100)) +"% (" + str(Otooley_votes)+ ")")
print("-------------------------")
print("Winner: " + election_winner)
print("-------------------------")

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("--------------------------\n")
    text.write("Total Vote: " + str(total_election_votes) + "\n")
    text.write("-------------------------\n")
    text.write("Khan: " + str(round(Vote_Percentage_Khan * 100)) +"% (" + str(Khan_votes)+ ")\n")
    text.write("Correy: " + str(round(Vote_Percentage_Correy * 100)) +"% (" + str(Correy_votes)+ ")\n")
    text.write("Li: " + str(round(Vote_Percentage_Li * 100)) +"% (" + str(Li_votes)+ ")\n")
    text.write("O'Tooley: " + str(round(Vote_Percentage_Otooley * 100)) +"% (" + str(Otooley_votes)+ ")\n")
    text.write("-------------------------\n")
    text.write("Winner: " + election_winner + "\n")
    text.write("-------------------------\n")