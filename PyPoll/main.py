import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

with open(election_data) as csvfile:
 file = csv.reader(csvfile, delimiter=',')
 header = next(file)

 Candidate = []

 for row in file:
      Candidate.append(row[2])

#The total number of votes cast
Total_Votes = len(Candidate)

#The percentage of votes each candidate won
Degette_Counter = 0
Doane_Counter = 0
Stockham_Counter = 0

for i in Candidate:
   if i == 'Diana DeGette':
      Degette_Counter = Degette_Counter + 1
   elif i == 'Raymon Anthony Doane':
      Doane_Counter = Doane_Counter + 1
   elif i == 'Charles Casper Stockham':
      Stockham_Counter = Stockham_Counter + 1

Degette_Percentege = (int(Degette_Counter) / int(Total_Votes)) * 100
Doane_Percentege = (int(Doane_Counter) / int(Total_Votes)) * 100
Stockham_Percentege = (int(Stockham_Counter) / int(Total_Votes)) * 100

#The winner of the election based on popular vote

Percentage_list = [Degette_Percentege, Doane_Percentege, Stockham_Percentege]
Winner = max(Percentage_list)

if Winner == Degette_Percentege:
   Winner_Name = "Diana DeGette"
elif Winner == Doane_Percentege:
   Winner_Name = "Raymon Anthony Doane"
elif Winner == Stockham_Percentege:
   Winner_Name = "Charles Casper Stockham"


print("Election Results")
print("------------------------------------")
print(f"Total Votes: {Total_Votes}")
print("------------------------------------")
print(f"Charles Casper Stockham: {Stockham_Percentege:.3f} ({Stockham_Counter})")
print(f"Diana DeGette: {Degette_Percentege:.3f} ({Degette_Counter})")
print(f"Raymon Anthony Doane: {Doane_Percentege:.3f} ({Doane_Counter})")
print(f"Winner: {Winner_Name}")


with open("analysis.txt", "w") as f:
 f.write("Election Results\n")
 f.write("------------------------------------\n")
 f.write(f"Total Votes: {Total_Votes}\n")
 f.write("------------------------------------\n")
 f.write(f"Charles Casper Stockham: {Stockham_Percentege:.3f} ({Stockham_Counter})\n")
 f.write(f"Diana DeGette: {Degette_Percentege:.3f} ({Degette_Counter})\n")
 f.write(f"Raymon Anthony Doane: {Doane_Percentege:.3f} ({Doane_Counter})\n")
 f.write(f"Winner: {Winner_Name}\n")
