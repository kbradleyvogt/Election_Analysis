# Add our dependencies. 
import csv
import os
#assign a variable for the file and load the path
file_to_load = os.path.join('Resouces','election_results.csv')
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#. Initialize a total vote counter.
total_votes = 0

#Candidate Options
candidate_options = []
#Declare the empty dictionary 
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row,
    headers = next(file_reader)

    #Print each row in the CSV file"
    for row in file_reader:
        #Add to the total count.
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

print(candidate_options)

#  To do: print out the winning candidate, vote count and percentage to
#   terminal
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
        f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)
