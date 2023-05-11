<!DOCTYPE html>
<html>
<body>

  <h1>Sentiment Analysis using Reddit API</h1>

  <p>This is a Python-based project that performs natural language proccessing to get sentiment analysis of Reddit comments using the Vader model and PRAW (Python Reddit API Wrapper) to get data from Reddit.</p>

  <h2>Requirements</h2>

  <p>To use this project, you will need to install the following libraries:</p>

  <ul>
    <li>praw</li>
    <li>pandas</li>
    <li>nltk</li>
  </ul>

  <p>You can install all these libraries by running the following command in your terminal:</p>

  <pre><code>pip install -r requirements.txt</code></pre>

  <h2>How to use</h2>

  <p>To use this project, follow these steps:</p>

  <ol>
    <li>Clone this repository to your local machine.</li>
    <li>Install the required libraries by running <code>pip install -r requirements.txt</code>.</li>
    <li>Set up a Reddit API account and obtain a client ID, client secret.</li>
    <li>Enter your Reddit API credentials in <code>config.py</code>.</li>
    <li>Run the <code>gui-test.py</code> file to analyze Reddit comments.</li>
  </ol>

  <p>When you run the <code>gui-test.py</code> file, the program will prompt you to enter the select a subreddit and the keyword you want to analyze. After entering this information, the program will retrieve the comments from Reddit and perform sentiment analysis on them using the Vader model.</p>

</body>
</html>
