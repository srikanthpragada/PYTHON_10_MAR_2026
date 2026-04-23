from datetime import *

players = []
with open("players.txt", "rt") as f:
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue  # Ignore line with insufficient data
        name = parts[0]
        try:
            dob = datetime.strptime(parts[1], "%d-%m-%Y")
            # Calculate age in years
            td = datetime.now() - dob
            years = td.days // 365
            players.append((years, name))
        except:
            pass

for player in sorted(players, reverse=True):
    print(f"{player[1]:20}  {player[0]:2}")
