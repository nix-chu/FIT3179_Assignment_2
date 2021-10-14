import csv

filelocation = "president_county_candidate.csv"
csv_file = open(filelocation, 'r')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader, None) # skip header

data = {}
candidates = ["Joe Biden", "Donald Trump"]

for row in csv_reader:
    if row[0] not in data.keys():
        # Add new state into dictionary and create new dictionary to store counties
        data[row[0]] = {}
    
    if row[1] not in data[row[0]].keys():
        # Add new county into state dictionary
        data[row[0]][row[1]] = {}
    
    if row[2] not in candidates:
        # Candidate is irrelevant
        if "Other" not in data[row[0]][row[1]].keys():
            # No record of irrelevant candidate
            data[row[0]][row[1]]["Other"] = int(row[4])
        else:
            data[row[0]][row[1]]["Other"] += int(row[4])
    else:
        # Store new item into dictionary
        data[row[0]][row[1]][row[2]] = row[4]

csv_file.close()
f = open("clean_county_data.csv", 'w', newline="")
csv_writer = csv.writer(f)
header_row = ["state", "county", "biden_votes", "trump_votes", "other_votes", "winner"]
csv_writer.writerow(header_row)

for state in data:
    for county in data[state]:
        # Determine county winner
        biden_votes = data[state][county]["Joe Biden"]
        trump_votes = data[state][county]["Donald Trump"]
        if biden_votes > trump_votes:
            winner = "Biden"
        else:
            winner = "Trump"

        new_row = [
            state,
            county,
            biden_votes,
            trump_votes,
            data[state][county]["Other"],
            winner
        ]
        print(new_row)
        csv_writer.writerow(new_row)

f.close()