from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd




# plot the WordCloud image					
def show_cloud():
    
	df = pd.read_csv(r"Submissions_With_Vader.csv", encoding ="latin-1")

	comment_words = ''
	stopwords = set(STOPWORDS)

	# iterate through the csv file
	for val in df.items():
		
		# typecaste each val to string
		val = str(val)

		# split the value
		tokens = val.split()
		
		# Converts each token into lowercase
		for i in range(len(tokens)):
			tokens[i] = tokens[i].lower()
		
		comment_words += " ".join(tokens)+" "

	wordcloud = WordCloud(width = 800, height = 800,
					background_color ='white',
					stopwords = stopwords,
					min_font_size = 10).generate(comment_words)
	plt.figure(figsize = (8, 8), facecolor = None)
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.tight_layout(pad = 0)


	plt.show()
