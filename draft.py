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
results = list()
polarity2 = list()
df = pd.DataFrame()

#WORKING
def get_submission_WithKeyWord(sub,keyword):        #IF WE WANT TO USE KEYWORD TOO
    
        
#    reddit = praw.Reddit(                        #Moeen Credentials 
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
            # print(submission.title)
            sub_collect.add(submission.title) #ADDED THIS HERE TO COLLECT THE SUBMISSIONS IN THE SET (SUB_COLLECT)
            # Output: the submission's title
            # print(submission.score) 
            # Output: the submission's score

#WORKING            
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
    for submission in subreddit.hot(limit=None):  #prints the submission if keyword exists.
        # print(submission.title)
        sub_collect.add(submission.title)

#WORKING
def create_csv(): #creates csv of the submissions collected (NOT RUN ON VADER YET)
    df = pd.DataFrame(sub_collect)
    df.to_csv('Submissions Collected.csv', header= False, encoding= 'utf-8', index = False)

#WORKING
def executeVader():
    sia = SentimentIntensityAnalyzer()
    

    for line in sub_collect:
        polarity = sia.polarity_scores(line)
        # print(polarity)
        polarity2.append(line)
        results.append(polarity)

#WORKING
def modified_CSV(): #contains csv with vader results
    
    df['Submission'] = polarity2
    df['Label'] = 0
    for i, (result, submission) in enumerate(zip(results, polarity2)):
        if result['compound'] > 0.2:
            df.loc[i, 'Label'] = 1
        elif result['compound'] < -0.2:
            df.loc[i, 'Label'] = -1
        df.loc[i, 'Submission'] = submission
    df.to_csv('Submissions_With_Vader.csv', encoding='utf-8', index=False)


#WORKING
def Label_Scores_by_count():
    count = df.Label.value_counts()
    print(count)

#WORKING
def Label_Scores_by_percentage():
    pcntage = df.Label.value_counts(normalize = True) * 100
    print(pcntage)

#WORKING
def print_Positive_Submission():
    print("Positive Submissions: \n")
    pprint(list(df[df['Label'] == 1].Submission), width=200)

#WORKING
def print_Negative_Submission():
    print("Negative Submissions:\n")
    pprint(list(df[df['Label'] == -1].Submission), width=200)

# NO NEED OF THIS CODE. IF HOGI, THEN I'LL WRITE IT AGAIN BECAUSE THIS FUNCTION IS NOT WORKING
# def print_All_Submissions():
#     print("All Submissions:\n")
#     pprint(list(df[df['Label']].Submission))

def plot_Sentiment_BarGraph():
    fig, ax = plt.subplots(figsize = (8,8))
    counts = df.Label.value_counts(normalize=True) * 100
    sns.barplot(x = counts.index, y = counts, ax = ax)

    ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
    ax.set_ylabel("Percentage")
    plt.show()



def play():
    get_submission("politics")

    create_csv()
    
    executeVader()

    modified_CSV()

    print("\n")
    print("The Labels by count are:")
    Label_Scores_by_count()

    print("\n")
    print("The count by percentage are:")
    Label_Scores_by_percentage()

    print("\n")
    print_Positive_Submission()

    print("\n")
    print_Negative_Submission()

    plot_Sentiment_BarGraph()


play()
