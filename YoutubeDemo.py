#subreddit drop box in gui
#if else loop for keyword existing in content
#pichart

from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import praw 


user_agent = "Scraper 1.0 by /u/mustafafaysal"
reddit = praw.Reddit(client_id = "W3vT8epgjWSF6DhkudzmjA",
                     client_secret = "h8X2dVt37L6ZXHRKi2K_tYy1NAozHg", 
                     user_agent = user_agent)

headlines = set()

#we can print id, author, created_utc, score, upvote ratio, url
for submission in reddit.subreddit('politics').hot(limit = 100):
    print(submission.title)
    headlines.add(submission.title)

print(len(headlines))

df = pd.DataFrame(headlines)
df.head()

df.to_csv('headlines.csv', header= False, encoding= 'utf-8', index = False)


import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer 
#from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

results = {}

for line in headlines:
    pol_score = sia.polarity_scores(line) #will return a dictionary
    pol_score['headline'] = line
    # results.append(pol_score)
    results['pol_score'] = pol_score


pprint(results) #prints the first 3 results only

df = pd.DataFrame.from_records(results)
df.head()

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1 #if-else wali condition
df.loc[df['compound'] < -0.2, 'label'] = -1 #threshold set between 0.2 and -0.2
df.head()

df2 = df[['headline', 'label']]
df2.to_csv('reddit_headlines_labels.csv', encoding='utf-8', index= False)

df2.label.value_counts()

df.label.value_counts(normalize = True) *100 #gives value counts in percentage form

print("Positive headline:\n")
pprint(list(df[df['label'] == 1].headline)[:5], width=200)

print("\nNegative headlines:\n")
pprint(list(df[df['label'] == -1].headline)[:5], width=200)

fig, ax = plt.subplots(figsize = (8,8))
counts = df.label.value_counts(normalize=True) * 100
sns.barplot(x = counts.index, y = counts, ax = ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

plt.show()