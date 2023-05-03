import praw


reddit = praw.Reddit(
    client_id="ml3JKWrmbdnHChAxNziJjg",
    client_secret="2cXTppbxDoSnvOBLpnqvmm1XnMAZng",
    user_agent="my user agent",
)

print(reddit.read_only)

for subm in reddit.subreddit("politics").hot(limit=20):
    print(subm.title)