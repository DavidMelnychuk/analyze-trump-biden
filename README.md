# Analyzing 2020 Presidential Candidate Tweets during the COVID-19 pandemic
## Data
Data for both candidates includes tweets from December 31 2019 to August 9 2020. 
Trump data taken from the [trump twitter archive](http://www.trumptwitterarchive.com/archive).  
Biden data extracted from the Twitter API using [Tweepy](https://www.tweepy.org/). Code can be found in get_biden_tweets.py.

## Running the notebook
All code can be found in analyze_tweets.ipynb. 
To run the notebook,

clone the repo: `git clone https://github.com/DavidMelnychuk/analyze-trump-biden.git`

create a virtual environment and install the requirements:

```
cd analyze-trump-biden 

virtualenv venv 

source venv/bin/activate 

pip3 install -r requirements.txt 
```

Run jupyter notebook and then open analyze-tweets.ipynb: `jupyter notebook`


## Summary
In this project, I analyzed the tweets of presidential candidates Donald Trump and Joe Biden since the start of the COVID-19 pandemic. Two datasets in CSV formats containing the tweets of Trump and Biden were used. Data sets were cleaned by filtering retweets, removing tweets before the pandemic, and tokenization. Tweets were also stemmed and lemmatized prior to topic modeling. Aggregate and frequency statistics were performed with Pandas by looking at the average retweet and favorite counts of each candidate and the frequency of their tweets over time. Their most common n-grams were analyzed and so were the number of times they mentioned each other or the coronavirus pandemic. Sentiment analysis was done by using TextBlob which showed that Trump had more polarizing tweets than Biden and that their polarity did not change over time. Topic modeling was conducted with gensim and manually evaluated by interpreting the top-5 words of each cluster and distances between clusters. Lastly classification was done with a multitude of classifiers with the final model being a voting classifier consisting of linear SVM, multinomial Naïve Bayes, and multi-layer perceptron classifiers. Classification evaluation was done with 10-fold cross validation and an 80/20 split of training to test data. The final voting classifier predicted test data with a high accuracy of 95%.
