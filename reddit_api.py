import praw



def get_submission(sub,keyword):
    
        
    reddit = praw.Reddit(                       # connection
        client_id="ml3JKWrmbdnHChAxNziJjg",
        client_secret="2cXTppbxDoSnvOBLpnqvmm1XnMAZng",
        user_agent="my user agent",
    )

    if reddit.read_only == True:
        print("Connected Successfully")

    
    subreddit = reddit.subreddit(sub)
    # input of subreddit and keyword
    for submission in subreddit.hot(limit=None):  
        if keyword.casefold() in submission.title.casefold() :    # to check if the keyword exists in the title
            print(submission.title)
            # Output: the submission's title
            print(submission.score)
            # Output: the submission's score
            
    

#get_submission("Politics","trump")        
