import pandas as pd
import os

OUTPUT_PATH = os.path.expanduser('~/Documents/StyleMetrics/data/competitors.csv')

data = [
    {"brand": "Paloma Wool", "style": "Artsy Minimalist", "followers": 480000, "engagement_rate": 1.8, "posts_per_week": 4, "top_content": "Reels"},
    {"brand": "Baserange", "style": "Sustainable Basics", "followers": 120000, "engagement_rate": 2.1, "posts_per_week": 3, "top_content": "Carousel"},
    {"brand": "Toteme", "style": "Quiet Luxury", "followers": 890000, "engagement_rate": 1.2, "posts_per_week": 5, "top_content": "Static"},
    {"brand": "Nanushka", "style": "Contemporary", "followers": 320000, "engagement_rate": 1.5, "posts_per_week": 4, "top_content": "Reels"},
    {"brand": "Studio Nicholson", "style": "Minimalist", "followers": 280000, "engagement_rate": 1.9, "posts_per_week": 3, "top_content": "Static"},
    {"brand": "Aeron", "style": "Eastern European", "followers": 95000, "engagement_rate": 2.4, "posts_per_week": 5, "top_content": "Reels"},
    {"brand": "Rejina Pyo", "style": "Asian Influenced", "followers": 180000, "engagement_rate": 2.2, "posts_per_week": 4, "top_content": "Carousel"},
    {"brand": "Remain", "style": "Copenhagen Chic", "followers": 210000, "engagement_rate": 1.7, "posts_per_week": 4, "top_content": "Reels"},
    {"brand": "Simone Rocha", "style": "Feminine Artistic", "followers": 650000, "engagement_rate": 2.8, "posts_per_week": 3, "top_content": "Static"},
    {"brand": "Jacquemus", "style": "Mediterranean", "followers": 4200000, "engagement_rate": 3.1, "posts_per_week": 6, "top_content": "Reels"},
]

df = pd.DataFrame(data)
df.to_csv(OUTPUT_PATH, index=False)
print(f"Done! Competitor data saved to: {OUTPUT_PATH}")
print(f"Total brands: {len(df)}")
print(df[["brand", "followers", "engagement_rate", "top_content"]])
