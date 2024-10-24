# -*- coding: UTF-8 -*-

# Dependencies
import csv
import os


# Files to load and output
file_to_load = os.path.join('Resources/budget_data.csv')        # Input file path
file_to_output = os.path.join('analysis/budget_analysis.txt')   # Output file path


# Define variables to track the financial data
total_months = 0        # The total number of months included in the dataset
net_total = 0           # The net total amount of "Profit/Losses" over the entire period


# Open and read the csv
with open(file_to_load) as financial_data:                  # Opens the budget_data.csv file and gives it the variable financial_data (used in the rest of the code)
    reader = csv.reader(financial_data, delimiter=",")      # Reader variable is set which will hold the financial_data (csv file) contents and specifies the delimiter


    # Skip the header row
    header = next(reader)     # When are we supposed to use None?

    # Extract first row to avoid appending to net_change_list
    first_data_row = next(reader)
    
    # Variable for the value of the first row of Profit/Losses to add back into calculations later
    first_data_row_value = int(first_data_row[1])

    # Variable for track the previous net change to subtract
    prev_net_change = first_data_row_value

    # Create lists to hold the two columns in the csv file (date and Profit/Losses)
    net_change_list = []
    date_list = []


    # Process each row of data
    for row in reader:

        # Track the date and append to the date list
        date = row[0]
        date_list.append(date)
        
        # Calculate the total number of months
        total_months = total_months + 1
        
        # Track the net total
        net_total = net_total + int(row[1])          # Adds the "Profit/Losses" amount at the current row in the loop to the net_total

        # Track the net change of the current row amount and the previous row amount
        net_change = int(row[1]) - prev_net_change  # Subtracts the previous row amount from the current row amount
        prev_net_change = int(row[1])               # Sets the previous row amount to the current row amount
        net_change_list.append(net_change)          # Adds the new row's net change to the net change list       


# Add back the first row to the total months and net total calculations
total_months = total_months + 1
net_total = net_total + first_data_row_value


# Zip the lists together into a dictionary
greatest_dict = dict(zip(date_list, net_change_list))

# Calculate the greatest increase in profits (month and amount)
greatest_increase_month = max(greatest_dict, key = greatest_dict.get)   # Searches for the max value and returns the key
greatest_increase_amount = greatest_dict[greatest_increase_month]       # Returns the value of the key

# Calculate the greatest decrease in losses (month and amount)
greatest_decrease_month = min(greatest_dict, key = greatest_dict.get)   # Searches for the max value and returns the key
greatest_decrease_amount = greatest_dict[greatest_decrease_month]       # Returns the value of the key


# Calculate the average net change across the months
net_change_list_sum = sum(net_change_list)                                  # Summation of all the values in the net change lis
net_change_list_count = len(net_change_list)                                # Counts the length of the net change list
average_change = round((sum(net_change_list) / len(net_change_list)), 2)    # Calculates the average of the net change list


# Print the output
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
#print(f'Net Change: ${net_change}')
#print(f'Net Change List Count: {net_change_list_count}')
#print(f'Net Change List Sum: {net_change_list_sum}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})')


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f'Total Months: {total_months}\n')
    txt_file.write(f'Total: ${net_total}\n')
    txt_file.write(f'Average Change: ${average_change}\n')
    txt_file.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})\n')
    txt_file.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})')


#print(net_change_list)