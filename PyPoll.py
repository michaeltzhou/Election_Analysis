import csv
import os
#The Data we need to retrieve
#Assign file + file path
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
#1: The total number of votes cast
#2: A complete list of candidates who recieved votes
#3: The percentage of votes each candidate won
#4: The total number of votes each candidate won
#5: The winner of the election based on popular vote