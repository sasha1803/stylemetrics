import pandas as pd
import os

OUTPUT_PATH = os.path.expanduser('~/Documents/StyleMetrics/data/trends.csv')

data = [
    {"country": "Germany", "keyword": "minimalist fashion", "interest": 78, "trend": "rising"},
    {"country": "Germany", "keyword": "quiet luxury", "interest": 65, "trend": "rising"},
    {"country": "Germany", "keyword": "sustainable womenswear", "interest": 82, "trend": "rising"},
    {"country": "Germany", "keyword": "Asian fashion Europe", "interest": 45, "trend": "rising"},
    {"country": "Germany", "keyword": "independent fashion brand", "interest": 55, "trend": "stable"},
    {"country": "Germany", "keyword": "emerging fashion label", "interest": 40, "trend": "rising"},
    {"country": "Netherlands", "keyword": "minimalist fashion", "interest": 85, "trend": "rising"},
    {"country": "Netherlands", "keyword": "quiet luxury", "interest": 72, "trend": "rising"},
    {"country": "Netherlands", "keyword": "sustainable womenswear", "interest": 88, "trend": "rising"},
    {"country": "Netherlands", "keyword": "Asian fashion Europe", "interest": 52, "trend": "rising"},
    {"country": "Netherlands", "keyword": "independent fashion brand", "interest": 61, "trend": "rising"},
    {"country": "Netherlands", "keyword": "emerging fashion label", "interest": 48, "trend": "rising"},
    {"country": "United Kingdom", "keyword": "minimalist fashion", "interest": 91, "trend": "rising"},
    {"country": "United Kingdom", "keyword": "quiet luxury", "interest": 88, "trend": "rising"},
    {"country": "United Kingdom", "keyword": "sustainable womenswear", "interest": 79, "trend": "rising"},
    {"country": "United Kingdom", "keyword": "Asian fashion Europe", "interest": 67, "trend": "rising"},
    {"country": "United Kingdom", "keyword": "independent fashion brand", "interest": 74, "trend": "rising"},
    {"country": "United Kingdom", "keyword": "emerging fashion label", "interest": 58, "trend": "rising"},
    {"country": "Italy", "keyword": "minimalist fashion", "interest": 70, "trend": "stable"},
    {"country": "Italy", "keyword": "quiet luxury", "interest": 95, "trend": "rising"},
    {"country": "Italy", "keyword": "sustainable womenswear", "interest": 68, "trend": "rising"},
    {"country": "Italy", "keyword": "Asian fashion Europe", "interest": 41, "trend": "rising"},
    {"country": "Italy", "keyword": "independent fashion brand", "interest": 59, "trend": "stable"},
    {"country": "Italy", "keyword": "emerging fashion label", "interest": 44, "trend": "rising"},
    {"country": "France", "keyword": "minimalist fashion", "interest": 88, "trend": "rising"},
    {"country": "France", "keyword": "quiet luxury", "interest": 92, "trend": "rising"},
    {"country": "France", "keyword": "sustainable womenswear", "interest": 85, "trend": "rising"},
    {"country": "France", "keyword": "Asian fashion Europe", "interest": 58, "trend": "rising"},
    {"country": "France", "keyword": "independent fashion brand", "interest": 63, "trend": "rising"},
    {"country": "France", "keyword": "emerging fashion label", "interest": 51, "trend": "rising"},
]

df = pd.DataFrame(data)
df.to_csv(OUTPUT_PATH, index=False)
print(f"Done! Trends saved to: {OUTPUT_PATH}")
print(f"Total rows: {len(df)}")