import praw
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer 

# in Order functions
#1. get_submission
#2. create_csv
#3. executeVader
#4. modified_csv
#5. MANDATORY TO RUN ABOVE 4 FUNCTIONS IN ORDER, ELSE CAN BE RUN ACCORDING TO THE OUTPUT WE WANT TO SHOW



sub_collect = set()
results = {}
df = pd.DataFrame()

def get_submission_WithKeyWord(sub,keyword):        #IF WE WANT TO USE KEYWORD TOO
    
        
   # reddit = praw.Reddit(                        #Moeen Credentials  # connection
    #    client_id="ml3JKWrmbdnHChAxNziJjg",
    #    client_secret="2cXTppbxDoSnvOBLpnqvmm1XnMAZng",
    #    user_agent="my user agent",
    #)

    reddit = praw.Reddit(                           #Mustafa credentials.
        client_id = "W3vT8epgjWSF6DhkudzmjA", 
        client_secret = "h8X2dVt37L6ZXHRKi2K_tYy1NAozHg", 
        user_agent = "My User Agent."
    )
    


    if reddit.read_only == True:  #Checks if api connected
        print("Connected Successfully")

    
    subreddit = reddit.subreddit(sub) #finds the subreddit given in the argument as sub
    # input of subreddit and keyword

    for submission in subreddit.hot(limit=None):  #prints the submission if keyword exists.
        if keyword.casefold() in submission.title.casefold() :    # to check if the keyword exists in the title
            print(submission.title)
            sub_collect.add(submission.title) #ADDED THIS HERE TO COLLECT THE SUBMISSIONS IN THE SET (SUB_COLLECT)
            # Output: the submission's title
            # print(submission.score) 
            # Output: the submission's score
            
def get_submission(sub):        #IF WE DONT WANT TO USE KEYWORD

     # reddit = praw.Reddit(                        #Moeen Credentials
    #    client_id="ml3JKWrmbdnHChAxNziJjg",
    #    client_secret="2cXTppbxDoSnvOBLpnqvmm1XnMAZng",
    #    user_agent="my user agent",
    #)

    reddit = praw.Reddit(                           #Mustafa credentials.
        client_id = "W3vT8epgjWSF6DhkudzmjA", 
        client_secret = "h8X2dVt37L6ZXHRKi2K_tYy1NAozHg", 
        user_agent = "My User Agent."
    )
    


    if reddit.read_only == True:  #Checks if api connected
        print("Connected Successfully")

    
    subreddit = reddit.subreddit(sub) #finds the subreddit given in the argument as sub
    # input of subreddit only
    for submission in subreddit.hot(limit=100):  #prints the submission if keyword exists.
        print(submission.title)
        sub_collect.add(submission.title)


def create_csv(): #creates csv of the submissions collected (NOT RUN ON VADER YET)
    df = pd.DataFrame(sub_collect)
    df.to_csv('Submissions Collected.csv', header= False, encoding= 'utf-8', index = False)


def executeVader():
    sia = SentimentIntensityAnalyzer()
    

    for line in sub_collect:
        polarity = sia.polarity_scores(line)
        polarity['Submission'] = line
        results['Polarity'] = polarity


def modified_CSV(): #contains csv with vader results
    
    df['Label'] = 0
    if 'compound' in results:
        df.loc[df['compound'] > 0.2, 'Label'] = 1 #if-else wali condition
        df.loc[df['compound'] < -0.2, 'Label'] = -1 #threshold set between 0.2 and -0.2
    else:
        print("Error: Compound key not found in results dictionary.")

    df2 = df[['Submission', 'Label']]
    df2.to_csv('Submissions_With_Vader.csv', encoding='utf-8', index= False)

def Label_Scores_by_count():
    df.label.value_counts()

def Label_Scores_by_percentage():
    df.label.value_counts(normalize = True) * 100

def print_Positive_Submission():
    print("Positive Submissions: \n")
    pprint(list(df[df['Label'] == 1].Submission)[:5], width=200)

def print_Negative_Submission():
    print("Negative Submissions:\n")
    pprint(list(df[df['Label'] == -1].Submission)[:5], width=200)

def print_All_Submissions():
    print("All Submissions:\n")
    pprint(list(df[df['Label']].Submission)[:5], width=200)

def plot_Sentiment_BarGraph():
    fig, ax = plt.subplots(figsize = (8,8))
    counts = df.label.value_counts(normalize=True) * 100
    sns.barplot(x = counts.index, y = counts, ax = ax)

    ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
    ax.set_ylabel("Percentage")
    plt.show()


get_submission("politics")
create_csv()

executeVader()
# df = pd.DataFrame(results).T
# df.head()

# modified_CSV()
# Label_Scores_by_count()
# Label_Scores_by_percentage()
# print_Positive_Submission()
# print_Negative_Submission()
# plot_Sentiment_BarGraph()
