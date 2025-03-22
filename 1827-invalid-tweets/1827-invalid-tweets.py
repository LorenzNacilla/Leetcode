import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[tweets['content'].str.len() > 15].get(['tweet_id'])