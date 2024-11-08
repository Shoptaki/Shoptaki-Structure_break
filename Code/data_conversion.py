# -*- coding: utf-8 -*-
"""data_conversion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CX8XgpThIosepM-idBlIl_XudrngTVD2
"""

import pandas as pd

# Load the data
file_path = '/content/daily_sentiment_score_analysis.csv'
daily_data = pd.read_csv(file_path)

# Convert 'date' column to datetime format for resampling
daily_data['date'] = pd.to_datetime(daily_data['date'])

# Set the date column as the index
daily_data.set_index('date', inplace=True)

# Resample data to weekly, monthly and yearly frequencies and calculate mean
weekly_data = daily_data.resample('W').mean()
monthly_data = daily_data.resample('M').mean()
yearly_data = daily_data.resample('Y').mean()

# Save the weekly, monthly and yearly data to CSV files
weekly_data.to_csv('weekly_sentiment_score_analysis.csv')
monthly_data.to_csv('monthly_sentiment_score_analysis.csv')
yearly_data.to_csv('yearly_sentiment_score_analysis.csv')