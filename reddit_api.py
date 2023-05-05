import praw
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer 
sia = SentimentIntensityAnalyzer()


def get_submission(sub,keyword):
    
        
    reddit = praw.Reddit(                        #Moeen Credentials  # connection
        client_id="ml3JKWrmbdnHChAxNziJjg",
        client_secret="2cXTppbxDoSnvOBLpnqvmm1XnMAZng",
        user_agent="my user agent",
    )

  #  reddit = praw.Reddit(                           #Mustafa credentials.
   #     client_id = "W3vT8epgjWSF6DhkudzmjA", 
    #    client_secret = "h8X2dVt37L6ZXHRKi2K_tYy1NAozHg", 
     #   user_agent = "My User Agent."
    #)
    


    if reddit.read_only == True:  #Checks if api connected
        print("Connected Successfully")

    
    subreddit = reddit.subreddit(sub) #finds the subreddit given in the argument as sub
    # input of subreddit and keyword
    for submission in subreddit.hot(limit=500):  #prints the submission if keyword exists.
        if keyword.casefold() in submission.title.casefold() :    # to check if the keyword exists in the title
            print(submission.title)
            # Output: the submission's title
            print(submission.score)
            # Output: the submission's score
            
    

#get_submission("Politics", "trump")        
