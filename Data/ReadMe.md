# Data Folder

This folder contains all raw and aggregated sentiment score data files used in the **Structure Break** project. The data is organized by time intervals to support various analytical needs within the project.

## Structure

- **daily_sentiment_score_analysis.csv**: This is the main data source and contains sentiment scores calculated on a daily basis. The daily data serves as the foundation for all other time intervals and is used to create the main tables in the `structure_break` database.
  
- **weekly_sentiment_score_analysis.csv**: Aggregated from the daily data, this folder contains sentiment scores summarized on a weekly basis.
  
- **monthly_sentiment_score_analysis.csv**: Contains monthly sentiment scores derived from the daily data to provide a broader view of trends.

- **yearly_sentiment_score_analysis.csv**: Contains yearly sentiment scores aggregated from daily data, useful for long-term trend analysis.

## Usage

The **daily_data** files are used to create the core tables within the `structure_break` database. Data in this folder is then aggregated to form the **weekly_data**, **monthly_data**, and **yearly_data** tables, allowing for flexible analysis across different time frames.
