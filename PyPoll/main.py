


fp = open("PyPoll\Resources\\election_data.csv")
lines = [entry.strip().split(',') for entry in fp.readlines()][1:]
total_votes = len(lines)
total = 0

votes = dict()
ballot_ids = []

for line in lines:
    Ballot_ID, County, Candidate = line
    ballot_ids.append(Ballot_ID)

    if Candidate not in votes:
        votes[Candidate] = 0
    votes[Candidate] += 1 




print(f"""Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------""")
winner = ""


if len(set(ballot_ids)) != len(ballot_ids):
    print("Election Fraud has happend")
else:  
    max_votes = 0
    for Canidate, vote_count in votes.items():
        print(f"{Canidate} {vote_count/ total_votes * 100: .4f}% ({vote_count})")    
        if(max_votes < vote_count):
            max_votes = vote_count
            winner = Canidate

print(f"""-------------------------
Winner: {winner}
-------------------------""")