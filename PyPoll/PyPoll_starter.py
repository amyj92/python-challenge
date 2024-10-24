# -*- coding: UTF-8 -*-
#"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os


# Files to load and output (update with correct file paths)
file_to_load = os.path.join('Resources/election_data.csv')          # Input file path
file_to_output = os.path.join('analysis/election_analysis.txt')     # Output file path


# Initialize variables to track the election data
total_votes = 0                     # Track the total number of votes cast
CCS = "Charles Casper Stockham"     # Variable for Charles Casper Stockham
CCS_votes = 0                       # Tracks Charles Casper Stockham vote count
CCS_percentage = 0                  # Tracks Charles Casper Stockham vote percentage
DD = "Diana DeGette"                # Variable for Diana DeGette
DD_votes = 0                        # Tracks Diana DeGette vote count
DD_percentage = 0                   # Tracks Diana DeGette vote percentage
RAD = "Raymon Anthony Doane"        # Variable for Raymon Anthony Doane
RAD_votes = 0                       # Tracks Raymon Anthony Doane vote count
RAD_percentage = 0                  # Tracks Raymon Anthony Doane vote percentage
candidate_winner = 0                # Tracks the candidate winner


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

        # Use if statements to check to see if the row equals the candidate's name and add a vote to the candidate's count
        if row[2] == CCS:
            CCS_votes = CCS_votes + 1
        
        if row[2] == DD:
            DD_votes = DD_votes + 1
        
        if row[2] == RAD:
            RAD_votes = RAD_votes + 1


    # Calculate each candidates winning vote percent 
    CCS_percentage = CCS_votes/total_votes
    DD_percentage = DD_votes/total_votes
    RAD_percentage= RAD_votes/total_votes


    # Define lists and dictionaries to track candidate names and vote counts
    candidates_names = [CCS, DD, RAD]
    candidates_votes = [CCS_votes, DD_votes, RAD_votes]

    # Zip the candidates names and candidates votes lists into a dictionary
    candidates_dict = dict(zip(candidates_names, candidates_votes))

    # Determine the winner by finding the max votes
    candidate_winner = max(candidates_dict, key = candidates_dict.get)


    # Print summary table name
    print("Election Results")
    print("-------------------------")

    # Print the total vote count (to terminal)
    print(f'Total Votes: {total_votes}')    # Returns Total Votes: 369711
    print("-------------------------")

    # Print each candidates name: vote percentage (vote count) --> : .3% is used to format to % with 3 decimal places
    print(f'{CCS}: {CCS_percentage: .3%} ({CCS_votes})')    # Returns Charles Casper Stockham:  23.049% (85213)
    print(f'{DD}: {DD_percentage: .3%} ({DD_votes})')       # Returns Diana DeGette:  73.812% (272892)
    print(f'{RAD}: {RAD_percentage: .3%} ({RAD_votes})')    # Returns Raymon Anthony Doane:  3.139% (11606)
    print("-------------------------")

    # Print the candidate winner
    print(f'Winner: {candidate_winner}')
    print("-------------------------")


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Write summary table name to the text file
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")

    # Write the total vote count to the text file
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write("-------------------------\n")

    # Write each candidates name: vote percentage (vote count) to the text file --> : .3% is used to format to % with 3 decimal places
    txt_file.write(f'{CCS}: {CCS_percentage: .3%} ({CCS_votes})\n')
    txt_file.write(f'{DD}: {DD_percentage: .3%} ({DD_votes})\n')
    txt_file.write(f'{RAD}: {RAD_percentage: .3%} ({RAD_votes})\n')
    txt_file.write("-------------------------\n")

    # Write the candidate winner to the text file
    txt_file.write(f'Winner: {candidate_winner}\n')
    txt_file.write("-------------------------\n")
