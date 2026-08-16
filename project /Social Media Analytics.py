import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("social_media.csv")

data["engagement"] = data["likes"] + data["comments"] + data["shares"]

print("Total Posts:", len(data))
print("Total Likes:", data["likes"].sum())
print("Total Comments:", data["comments"].sum())
print("Total Shares:", data["shares"].sum())

best_post = data.loc[data["engagement"].idxmax()]
print("\nBest Performing Post:")
print(best_post)

print("\nPosts by Platform:")
print(data["platform"].value_counts())

platform_engagement = data.groupby("platform")["engagement"].sum()

platform_engagement.plot(kind="bar")
plt.title("Platform Engagement")
plt.xlabel("Platform")
plt.ylabel("Engagement")
plt.tight_layout()
plt.show()




# platform,likes,comments,shares
# Instagram,1200,150,80
# Instagram,950,100,60
# YouTube,2000,250,180
# Facebook,700,80,40
# YouTube,1800,200,120
# Twitter,600,70,30
