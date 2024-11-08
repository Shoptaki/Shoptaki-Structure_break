# -*- coding: utf-8 -*-
"""data_modification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GYOjN-emnhkUimv3BqhCInslIB2tyIem
"""

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('/content/daily_sentiment_score.csv')
# Replace the path to your actual CSV file

# Append ' 23:59:59' to the date column to make it compatible with the DATETIME format and ensure data is entered at the end of the day
df['date'] = df['date'].apply(lambda x: x + ' 23:59:59')

# Convert the 'date' column from text (string) to datetime format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

# Display the updated DataFrame
print(df)

# Optional: Save the updated DataFrame back to a new CSV
df.to_csv('/content/daily_sentiment_score_analysis.csv', index=False)