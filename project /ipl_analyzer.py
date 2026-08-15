import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Season": [
        2021, 2021, 2021, 2021,
        2022, 2022, 2022, 2022,
        2023, 2023, 2023, 2023,
        2024, 2024, 2024, 2024
    ],

    "Team1": [
        "CSK", "RCB", "DC", "MI",
        "CSK", "RCB", "GT", "LSG",
        "CSK", "MI", "KKR", "RR",
        "CSK", "MI", "SRH", "GT"
    ],

    "Team2": [
        "MI", "KKR", "SRH", "KKR",
        "KKR", "PBKS", "RR", "DC",
        "GT", "RCB", "SRH", "LSG",
        "RCB", "KKR", "RR", "CSK"
    ],

    "Winner": [
        "CSK", "RCB", "DC", "MI",
        "KKR", "PBKS", "GT", "LSG",
        "CSK", "RCB", "KKR", "RR",
        "RCB", "KKR", "SRH", "GT"
    ],

    "Toss Winner": [
        "MI", "RCB", "DC", "KKR",
        "KKR", "PBKS", "RR", "LSG",
        "GT", "RCB", "KKR", "RR",
        "RCB", "KKR", "RR", "GT"
    ],

    "Toss Decision": [
        "field", "bat", "field", "field",
        "field", "field", "field", "bat",
        "field", "field", "bat", "field",
        "field", "field", "field", "bat"
    ],

    "Venue": [
        "Wankhede", "Chinnaswamy", "Delhi", "Wankhede",
        "Wankhede", "Mumbai", "Ahmedabad", "Mumbai",
        "Ahmedabad", "Mumbai", "Kolkata", "Jaipur",
        "Chennai", "Mumbai", "Hyderabad", "Ahmedabad"
    ]
}


df = pd.DataFrame(data)


print("\n========== IPL DATA ANALYZER ==========\n")

print("Total Matches:", len(df))


# Team wins
team_wins = df["Winner"].value_counts()

print("\nTeam Wins:")
print(team_wins)


# Most successful team
best_team = team_wins.idxmax()

print("\nMost Successful Team:", best_team)
print("Total Wins:", team_wins.max())


# Matches played in each season
season_matches = df["Season"].value_counts().sort_index()

print("\nMatches by Season:")
print(season_matches)


# Toss analysis
toss_wins = df["Toss Winner"].value_counts()

print("\nToss Wins:")
print(toss_wins)


# Toss decisions
toss_decisions = df["Toss Decision"].value_counts()

print("\nToss Decisions:")
print(toss_decisions)


# Toss winner vs match winner
same_winner = (df["Toss Winner"] == df["Winner"]).sum()

percentage = (same_winner / len(df)) * 100

print(
    "\nToss winner also won the match:",
    round(percentage, 2),
    "%"
)


# Venue analysis
venue_count = df["Venue"].value_counts()

print("\nMatches by Venue:")
print(venue_count)


# Team wins chart
plt.figure(figsize=(9, 5))

team_wins.plot(kind="bar")

plt.title("IPL Team Wins")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# Season chart
plt.figure(figsize=(8, 5))

season_matches.plot(kind="bar")

plt.title("IPL Matches by Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")

plt.tight_layout()
plt.show()


# Toss decision chart
plt.figure(figsize=(6, 6))

toss_decisions.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Toss Decisions")
plt.ylabel("")

plt.tight_layout()
plt.show()




# Install:
# pip install pandas matplotlib

# Run:
# python ipl_analyzer.py
