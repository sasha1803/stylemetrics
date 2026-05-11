import pandas as pd
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

REVIEWS_PATH = os.path.expanduser('~/Documents/StyleMetrics/data/reviewscsv.csv')
OUTPUT_PATH = os.path.expanduser('~/Documents/StyleMetrics/data/sentiment.csv')

print("Loading reviews...")
df = pd.read_csv(REVIEWS_PATH)
df = df.dropna(subset=['Review Text'])
print(f"Total reviews loaded: {len(df)}")

print("Running sentiment analysis...")
analyser = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyser.polarity_scores(str(text))
    if score['compound'] >= 0.05:
        return 'positive', score['compound']
    elif score['compound'] <= -0.05:
        return 'negative', score['compound']
    else:
        return 'neutral', score['compound']

df[['sentiment', 'score']] = df['Review Text'].apply(
    lambda x: pd.Series(get_sentiment(x))
)

summary = df.groupby(['Department Name', 'sentiment']).size().unstack(fill_value=0)
summary['total'] = summary.sum(axis=1)
summary['positive_pct'] = (summary.get('positive', 0) / summary['total'] * 100).round(1)

df.to_csv(OUTPUT_PATH, index=False)
print(f"\nDone! Sentiment data saved to: {OUTPUT_PATH}")
print(f"\nSentiment by Department:")
print(summary[['positive_pct', 'total']])
