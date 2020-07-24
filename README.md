Got Trump Data from December 31 2019 (Start of COVID 19) to July 23 2020.


Look up how to use heuristics in classification.
I.e if includes the word Biden in it and negative sentiment then probably
Trump tweet.

reply_count is a premium twitter api feature.

Heuristic: If they tweet about the other and sentiment is negative, probably classify as
trump/biden tweet.

Distribution of positve/negative tweets of biden and trumps.
Count of positve/negative/netural.
Rate of positive/negative/neutral over time of the pandemic.

Trump tweets A LOT more than Biden.
1700 tweets vs 5200 tweets since December 2019.
Mention this in the report. Frequency statistics not as cool then.

Average tweets a day, week, month.

Can use the entire 3200 biden tweet dataset for training. 
The other statistical text analysis will be for during COVID19 pandemic.

Retweets not included because we want to get tweets that are indicative of how the
candidate writes and not the content they promote.

# Make this nice and fancy like kaggle to describe the data.
csv Data Columns, names 
tweet text, created_at, retweet_count, favorite_count, is_retweet, id_str

Data from December 31 2019 to July 23 2020.
No Retweets included because want writing indicative of candidate not other people.
I can turn this into a kaggle/blog post later.


Number of links they put.
Frequency of words.
Frequency of n-grams.


6 columns: text, created_at, retweet_count, favorite_count, is_retweet, id_str


Trump: 5186 rows
Biden: 3092 rows (but this includes beyond December 31.) Biden doesn't tweet as much.
Need to filter and get the amount of biden tweets since dec_31 then update



Binary classifier can use the entire data,
But to do the text analysis, I can focus on Since December 31.
