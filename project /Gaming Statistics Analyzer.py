import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("gaming_data.csv")

data["kd_ratio"] = data["kills"] / data["deaths"]

data["win"] = data["result"].apply(lambda x: 1 if x == "Win" else 0)

players = data.groupby("player").agg({
    "kills": "sum",
    "deaths": "sum",
    "win": "sum",
    "score": "mean"
})

players["win_rate"] = (players["win"] / data.groupby("player").size()) * 100
players["kd_ratio"] = players["kills"] / players["deaths"]

print("\nPlayer Statistics:")
print(players)

best_player = players["score"].idxmax()
print("\nBest Player:", best_player)

print("\nHighest Kills:")
print(players["kills"].idxmax())

players["win_rate"].sort_values().plot(kind="barh")

plt.title("Player Win Rate")
plt.xlabel("Win Rate (%)")
plt.ylabel("Player")
plt.tight_layout()
plt.show()



# player,game,kills,deaths,score,result
# Alex,Valorant,25,10,250,Win
# John,Valorant,18,15,190,Win
# Mike,Valorant,10,20,120,Lose
# Alex,Valorant,30,12,280,Win
# John,Valorant,15,18,160,Lose
# Mike,Valorant,22,14,210,Win
