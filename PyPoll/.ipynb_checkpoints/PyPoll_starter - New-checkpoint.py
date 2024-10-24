# -*- coding: UTF-8 -*-
#"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join('Resources/election_data.csv')  # Input file path
#file_to_output = os.path.join('analysis/election_analysis.txt')  # Output file path

# Initialize variables to track the election data
total_votes = 0                     # Track the total number of votes cast
CCS_votes = 0                       # Tracks Charles Casper Stockham vote count
CCS_percentage = 0                  # Tracks Charles Casper Stockham vote percentage
DD_votes = 0                        # Tracks Diana DeGette vote count
DD_percentage = 0                   # Tracks Diana DeGette vote percentage
RAD_votes = 0                       # Tracks Raymon Anthony Doane vote count
RAD_percentage = 0                  # Tracks Raymon Anthony Doane vote percentage
candidate_winner = 0                # Tracks the candidate winner


# Define lists and dictionaries to track candidate names and vote counts
candidate_info = dict()


# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")

    # Skip the header row
    header = next(reader, None)

    # Create a list for all the election data in the csv file
    election_data = list(reader)

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
            
            candidate_info[candidate_name] = 0   # Will add the new candidate's name to the candidate_names dictionary if it doesn't already exist (able to use any number)

            candidate_info[candidate_name] = candidate_info[candidate_name] + 1
    
    print(candidate_info)

    # Calculate each candidates winning vote percent 
    #CCS_percentage = CCS_votes/total_votes
    #DD_percentage = DD_votes/total_votes
    #RAD_percentage= RAD_votes/total_votes


    #candidate_winner = max(CCS_votes, DD_votes, RAD_votes)

    #for votes in reader:

        # Use if statements to check to see who has the most votes and is the candidate winner
        #if CCS_votes > DD_votes and CCS_votes > RAD_votes:
            #candidate_winner = CCS
        
        #if DD_votes > CCS_votes and DD_votes > RAD_votes:
            #candidate_winner = DD

        #if RAD_votes > CCS_votes and RAD_votes > DD_votes:
            #candidate_winner = RAD      


    # Print output
    print("Election Results")
    print("-------------------------")
    # Print the total vote count (to terminal)
    print(f'Total Votes: {total_votes}')    # Returns Total Votes: 369711
    print("-------------------------")
    # Print each candidates name: vote percentage (vote count) --> : .3% is used to format to % with 3 decimal places
    #print(f'{CCS}: {CCS_percentage: .3%} ({CCS_votes})')    # Returns Charles Casper Stockham:  23.049% (85213)
    #print(f'{DD}: {DD_percentage: .3%} ({DD_votes})')       # Returns Diana DeGette:  73.812% (272892)
    #print(f'{RAD}: {RAD_percentage: .3%} ({RAD_votes})')    # Returns Raymon Anthony Doane:  3.139% (11606)
    print("-------------------------")
    # Print the candidate winner
    #print(f'Winner: {candidate_winner}')
    print("-------------------------")


# Open a text file to save the output
#with open(file_to_output, "w") as txt_file:



    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
