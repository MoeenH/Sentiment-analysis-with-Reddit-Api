# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

import nltk 

#read in data

df = pd.read_csv('Restaurant reviews.csv')

df.head() #head command for data set

# %%
df['Review'].values[0] #prints the first review only

# %%
print(df.shape) #prints the size of the dataset (20491 reviews, and 2 columns (reviews and ratings))

# %%
df = df.head(101)
print(df.shape)

# %%
df['Rating'] #gives the rating column only

# %%
df['Rating'].value_counts() #tells which rating number has occured how many times

# %%
ax = df['Rating'].value_counts().sort_index().plot(kind= 'bar', title= 'Count of reviews by Ratings', figsize=(10,5))
# sort_index sorts the Ratings count by index
# plot function plots the graph
ax.set_xlabel('Review Stars')
ax.set_ylabel('Count of reviews')
plt.show()

# %%
# BASIC NLTK STUFF

example = df['Review'][1]
print(example)

# %%
# BASIC NLTK STUFF CONTINUATION

#nltk.download('punkt')
token = nltk.word_tokenize(example)
token[:10] #prints the first 10 words only.

# %%
# BASIC NLTK STUFF CONTINUATION

#nltk.download('averaged_perceptron_tagger')
## https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk      (THIS HAS LIST OF ABBREVIATIONS)
tagged = nltk.pos_tag(token) #find the part of speech for each word
tagged[:10]

# %%
# BASIC NLTK STUFF CONTINUATION

# nltk.download('maxent_ne_chunker')
# nltk.download('words')

entities = nltk.chunk.ne_chunk(tagged)
entities.pprint()


# %%
#VADER SENTIMENT SCORING 


#VADER (VALENCE AWARE DICTIONARY AND SENTIMENT REASONER) - BAG OF WORDS APPROACH
#THIS APPROACH DOES NOT ACCOUNT FOR RELATIONSHIPS BETWEEN WORDS WHICH IN HUMAN SPEECH IS IMPORTANT
#STOP WORDS ARE WORDS LIKE AND/OR (WORDS THAT DO NOT HAVE A POSITIVE OR NEGATIVE FEELING)

#WE WILL USE NLTK'S SENTIMENT_INTENSITY_ANALYZER TO GET THE NEG/NEU/POS SCORES OF THE TEXT
#THIS USES A "BAG OF WORDS" APPROACH, STOP WORDS ARE REMOVED AND EACH WORD IS SCORED AND COMBINED TO A TOTAL SCORE

from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

#nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# %%
#VADER SENTIMENT SCORING CONTINUATION

sia.polarity_scores('I am  happy') #CHECK FOR EXAMPLE
#COMPOUND VALUE RANGES FROM -1 TO +1 
#TOWARDS -1 BEING THE MOST NEGATIVE, AND +1 TOWARDS MOST POSITIVE

# %%
#VADER SENTIMENT SCORING CONTINUATION

sia.polarity_scores('I am not happy') #CHECK FOR EXAMPLE

# %%
#VADER SENTIMENT SCORING CONTINUATION

sia.polarity_scores('I am not happy but not sad either') #CHECK FOR EXAMPLE

# %%
#VADER SENTIMENT SCORING CONTINUATION

example #PRINTS THE EXAMPLE THAT WE CHOSE EARLIER

# %%
#VADER SENTIMENT SCORING CONTINUATION

sia.polarity_scores(example)

# %%
#VADER SENTIMENT SCORING CONTINUATION

#RUN THE POLARITY SCORE ON THE ENTIRE DATASET

result = {} #DICTIONARY TO STORE THE POLARITY SCORES.

for i, row in tqdm(df.iterrows(), total = len(df)):
    rev = row['Review']
    myID = row['Id']
    result[myID] = sia.polarity_scores(rev) #IF YOU UNCOMMENT THE BELOW CODE, THEN COMMENT OUT THIS LINE

    #IF YOU WANT TO DISPLAY RESTAURANT NAMES, UNCOMMENT THE BELOW CODE
    #restaurant_name = row['Restaurant']
    #scores = sia.polarity_scores(rev) 
    #scores['Restaurant'] = restaurant_name
    #result[myID] = scores

#USE COMPOUND SCORES ONLY WITH INDEX NUMBER (MOEEN)


# %%
#VADER SENTIMENT SCORING CONTINUATION

result

# %%
#VADER SENTIMENT SCORING CONTINUATION

#store into pandas dataframe for an organized order.

vaders = pd.DataFrame(result).T  #.T flips the whole table.
vaders

# %%
#VADER SENTIMENT SCORING CONTINUATION

vaders = vaders.reset_index().rename(columns={'index': 'Id'}) #merge it onto our original data frame
vaders = vaders.merge(df, how='left')
vaders

# %%
#VADER SENTIMENT SCORING CONTINUATION

#NOW WE HAVE THE SENTIMENT SCORES AND THE METADATA.
vaders.head()

# %%
#VADER SENTIMENT SCORING CONTINUATION

sns.barplot(data=vaders, x = 'Rating', y = 'compound')
ax.set_title('Compound score by Ratings.')
plt.show()


# %%
#VADER SENTIMENT SCORING CONTINUATION

sns.barplot(data=vaders, x = 'Rating', y = 'pos')
ax.set_title('Compound score by Ratings.')
plt.show()

# %%
#VADER SENTIMENT SCORING CONTINUATION

sns.barplot(data=vaders, x = 'Rating', y = 'neg')
ax.set_title('Compound score by Ratings.')
plt.show()

# %%
#VADER SENTIMENT SCORING CONTINUATION

sns.barplot(data=vaders, x = 'Rating', y = 'neu')
ax.set_title('Compound score by Ratings.')
plt.show()

# %%
#VADER SENTIMENT SCORING CONTINUATION

fig, axs = plt.subplots(1, 3, figsize=(12, 3))
sns.barplot(data=vaders, x = 'Rating', y = 'pos', ax = axs[0])
sns.barplot(data=vaders, x = 'Rating', y = 'neg', ax = axs[1])
sns.barplot(data=vaders, x = 'Rating', y = 'neu', ax = axs[2])
axs[0].set_title('Positive')
axs[1].set_title('Negative')
axs[2].set_title('Neutral')
plt.tight_layout() #to avoid the overlapping of y axis labels
plt.show()

# %%
#ROBERTA PRETRAINED MODEL

#MODEL TRAINED OF A LARGE CORPUS OF DATA
#TRANSFORMER MODEL ACCOUNTS FOR THE WORDS BUT ALSO THE CONTEXT RELATED TO WORDS.
#PICKS UP RELATIONSHIP BETWEEN THE WORDS (SARCASM WAGERA)

#WE WILL USE HUGGING FACE

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

# %%
#ROBERTA PRETRAINED MODEL CONTINUATION

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

#LOADS EVERYTHING FROM A PRETRAINED MODEL
#PULLS DOWN THE MODEL WEIGHTS THAT HAVE BEEN STORED 
#ESSENTIALLY DOING TRANSFER LEARNING
#IT WAS TRAINED ON A BUNCH OF TWITTER COMMENTS THAT WERE LABELED AND WE DONT HAVE TO RETRAIN THE MODEL AT ALL
#WE CAN USE THESE TRAINED WEIGHTS AND APPLY TO OUR DATASETS.
#DOWNLOADS IT ALL WHEN FIRST TIME IS USED 



# %%
#ROBERTA PRETRAINED MODEL CONTINUATION

#JUST TO RECALL THE VADER RESULTS ON OUR EXAMPLE
print(example)
sia.polarity_scores(example)

# %%
#ROBERTA PRETRAINED MODEL CONTINUATION

#RUN THE SAME EXAMPLE FOR ROBERTA NOW
encoded_text = tokenizer(example, return_tensors='pt') #TOKENIZER FUNCTION ENCODES THE EXAMPLE
encoded_text

# %%
#ROBERTA PRETRAINED MODEL CONTINUATION

output = model(**encoded_text)
output

# %%
#ROBERTA PRETRAINED MODEL CONTINUATION

#CHANGE THE OUTPUT TO A MORE READABLE FORM

changed_output = output[0][0].detach().numpy()
changed_output = softmax(changed_output)
changed_output

#OUTPUT IS IN THE FORM OF NEGATIVE, NEUTRAL, AND POSITIVE RATIO RESPECTIVELY.

# %%
#ROBERTA PRETRAINED MODEL CONTINUATION

changed_output_dictionary = {
    'roberta negative' : changed_output[0],
    'roberta_neutral' : changed_output[1], 
    'roberta_positive' : changed_output[2]
}

print(changed_output_dictionary)

# %%
def polarity_scores_roberta(example):
    encoded_text = tokenizer(example, return_tensors='pt')
    
    output = model(**encoded_text)
    
    changed_output = output[0][0].detach().numpy()
    
    changed_output = softmax(changed_output)
    
    changed_output_dictionary = {
    'roberta negative' : changed_output[0],
    'roberta_neutral' : changed_output[1], 
    'roberta_positive' : changed_output[2]
    }

    return changed_output_dictionary
    
    

# %%
#ALSO ROBERTA MODEL IS VERY SLOW! 10/100 REVIEWS ANALYZED IN 1.5 MINUTES.

vader_result = {}
roberta_result ={}

result = {}

for i, row in tqdm(df.iterrows(), total = len(df)):
    rev = row['Review']
    myID = row['Id']
    vader_result = sia.polarity_scores(rev)
    vader_result_rename = {}
    for key, value in vader_result.items(): # rename the neg, pos, neu in vader results to vader_neg, vader_neu etc
        vader_result_rename[f"vader_{key}"] = value

    roberta_result = polarity_scores_roberta(rev)
    both = {**vader_result_rename,**roberta_result}
    result[myID] = both

# %%
vader_result

# %%
roberta_result

# %%
both

# %%
result

# %%
roberta_pd = pd.DataFrame(result).T
roberta_pd


