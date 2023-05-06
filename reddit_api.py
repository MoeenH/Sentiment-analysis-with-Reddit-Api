import praw
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer 


sub_collect = set()
results = list()
polarity2 = list()
df = pd.DataFrame()


def get_submission_WithKeyWord(sub,keyword):                        #FUNCTION TO GET SUBMIISSIONS IF YOU WANT TO USE KEYWORD TOO
    
        
#    reddit = praw.Reddit(                                          #Moeen Credentials 
    #    client_id="ml3JKWrmbdnHChAxNziJjg",
    #    client_secret="2cXTppbxDoSnvOBLpnqvmm1XnMAZng",
    #    user_agent="my user agent",
    #)

    reddit = praw.Reddit(                                           #Mustafa credentials.
        client_id = "W3vT8epgjWSF6DhkudzmjA", 
        client_secret = "h8X2dVt37L6ZXHRKi2K_tYy1NAozHg", 
        user_agent = "My User Agent."
    )
    

    if reddit.read_only == True:                                    #CHECKS IF API IS CONNECTED
        print("API Connected Successfully")


    subreddit = reddit.subreddit(sub)                               #FINDS THE SUBREDDIT GIVEN IN THE ARGUMENT 'SUB'

    for submission in subreddit.hot(limit=None):                    #SEARCHES THE SUBREDDIT IN THE HOT CATEGORY
        if keyword.casefold() in submission.title.casefold() :      #IF CONDITION TO CHECK IF THE 'KEYWORD' EXISTS IN THE SUBMISSION
            sub_collect.add(submission.title)                       #COLLECTS THE SUBMISSIONS IN THE SET (SUB_COLLECT)
            

def get_submission(sub):                                            #FUNCTION TO GET SUBMISSION IF YOU DONT WANT TO USE ANY KEYWORD


     # reddit = praw.Reddit(                                        #Moeen Credentials
    #    client_id="ml3JKWrmbdnHChAxNziJjg",
    #    client_secret="2cXTppbxDoSnvOBLpnqvmm1XnMAZng",
    #    user_agent="my user agent",
    #)

    reddit = praw.Reddit(                                           #Mustafa credentials.
        client_id = "W3vT8epgjWSF6DhkudzmjA", 
        client_secret = "h8X2dVt37L6ZXHRKi2K_tYy1NAozHg", 
        user_agent = "My User Agent."
    )
    

    if reddit.read_only == True:                                    #CHECKS IF API IS CONNECTED
        print("API Connected Successfully")

    
    subreddit = reddit.subreddit(sub)                               #FINDS THE SUBREDDIT GIVEN IN THE ARGUMENT 'SUB'
    for submission in subreddit.hot(limit=None):                    
        sub_collect.add(submission.title)                           #COLLECTS THE SUBMISSIONS IN THE SET (SUB_COLLECT) 


def create_csv():                                                   #CREATES A CSV FILE OF THE DATA COLLECTED IN SUB_COLLECT
    df = pd.DataFrame(sub_collect)
    df.to_csv('Submissions Collected.csv', header= False, encoding= 'utf-8', index = False)


def executeVader():                                                 #FUNCTION TO EXECUTE VADER MODEL
    
    sia = SentimentIntensityAnalyzer()

    for line in sub_collect:
        polarity = sia.polarity_scores(line)                        #CREATES A DICTIONARY NAMED POLARITY WHICH SCORES POLARITY OF ALL THE SUBMISSIONS
        polarity2.append(line)                                      #LIST IN WHICH ALL THE SUBMISSIONS ARE STORED
        results.append(polarity)                                    #LIST IN WHICH THE POLARITY FOR EACH SUBMISSION IS STORED


def modified_CSV():                                                 #FUNCTION TO CREATE A MODIFIED MERGED CSV FILE (SUBMISSIONS WITH THEIR LABELS RESPECTIVELY)
  
    df['Submission'] = polarity2                                    #CREATES A NEW COLUMN 'SUBMISSION' AND ASSIGNS THE VALUES OF THE SET 'POLARITY2' INTO IT
    df['Label'] = 0                                                 #CREATES A NEW COLUMN 'LABEL' AND ASSIGNS THE VALUE '0' TO THE COLUMN

    for i, (result, submission) in enumerate(zip(results, polarity2)):     #MOEEN WRITE DESCRIPTION HERE FOR THIS 'FOR' LOOP
        
        if result['compound'] > 0.25:                                #MOEEN WRITE DESCRIPTION HERE FOR THIS 'IF' CONDITION        
            df.loc[i, 'Label'] = 1

        elif result['compound'] < -0.25:                             #MOEEN WRITE DESCRIPTION HERE FOR THIS 'ELSE' CONDITION
            df.loc[i, 'Label'] = -1
        
        df.loc[i, 'Submission'] = submission                         #MOEEN WRITE DESCRIPTION HERE
    
    df.to_csv('Submissions_With_Vader.csv', encoding='utf-8', index=False) 


def Label_Scores_by_count():                                        #FUNCTION TO PRINT THE 'LABEL' SCORES BY COUNT
    
    count = df.Label.value_counts()
    print(count)


def Label_Scores_by_percentage():                                   #FUNCTION TO PRINT THE 'LABEL' COUNT BY PERCENTAGE
   
    pcntage = df.Label.value_counts(normalize = True) * 100
    print(pcntage)


def print_Positive_Submission():                                    #FUNCTION TO PRINT ALL POSITIVE SUBMISSIONS (WHERE LABEL == 1)
  
    print("Positive Submissions: \n")
    pprint(list(df[df['Label'] == 1].Submission), width=200)


def print_Negative_Submission():                                    #FUNCTION TO PRINT ALL NEGATIVE SUBMISSIONS (WHERE LABEL == -1) 
  
    print("Negative Submissions:\n")
    pprint(list(df[df['Label'] == -1].Submission), width=200)


def plot_Sentiment_BarGraph():                                      #FUNCTION TO PLOT THE BARGRAPH BY LABEL

    fig, ax = plt.subplots(figsize = (8,8))
    counts = df.Label.value_counts(normalize=True) * 100
    sns.barplot(x = counts.index, y = counts, ax = ax)

    ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
    ax.set_ylabel("Percentage")
    plt.show()
