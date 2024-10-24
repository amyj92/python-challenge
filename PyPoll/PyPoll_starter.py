# -*- coding: UTF-8 -*-
#"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os


# Files to load and output (update with correct file paths)
file_to_load = os.path.join('Resources/election_data.csv')  # Input file path
file_to_output = os.path.join('analysis/election_analysis.txt')  # Output file path


# Initialize variables to track the election data
total_votes = 0         # Track the total number of votes cast


# Define lists and dictionaries to track candidate names and vote counts
candidate_info = dict()


# Winning Candidate and Winning Count Tracker
candidate_winner = ""       # Tracks the candidate winner
winning_votes_count = 0           # Tracks the winning vote count


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")

    # Skip the header row
    header = next(reader, None) 

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (used for large datasets to show that the program is still running)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_info:
            candidate_info[candidate_name] = 1   # Will add the new candidate's name to the candidate_names dictionary if it doesn't already exist (able to use any number)

        else:    
            # Add a vote to the candidate's count
            candidate_info[candidate_name] = candidate_info[candidate_name] + 1
    
        #print(candidate_info)
        #print(total_votes)


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    

    print()
    print("Election Results")
    txt_file.write("Election Results\n")
    print("-------------------------")
    txt_file.write("-------------------------\n")


    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")


    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_info.items():
        
        # Get the vote count and calculate the percentage
        candidate_vote_percentage = (votes / total_votes) * 100


        # Update the winning candidate if this one has more votes
        if votes > winning_votes_count:
            winning_votes_count = votes
            candidate_winner = candidate
        

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {candidate_vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {candidate_vote_percentage:.3f}% ({votes})\n")


    print("-------------------------")
    txt_file.write("-------------------------\n")


    # Generate and print the winning candidate summary
    winning_candidate_summary = f"Winner: {candidate_winner}"
    print(winning_candidate_summary)
    txt_file.write(f"{winning_candidate_summary}\n")


    print("-------------------------")
    txt_file.write("-------------------------\n")




