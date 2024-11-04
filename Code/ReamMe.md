# Code Snippets

This folder contains code snippets for data processing, transformation, and analysis within the **Structure Break** project. Each snippet is designed to assist in preparing and managing sentiment score data for efficient storage and analysis.

## Contents

- **data_modification.py**: Scripts to convert date data from string format to `datetime` format suitable for SQL, ensuring consistency in date handling across the database.
- **data_conversion.py**: Code to aggregate daily sentiment data into weekly, monthly, and yearly summaries, providing flexibility in analysis across different time intervals.

## Usage

Each file in this folder is designed to handle a specific aspect of data preparation and transformation. Use the **data_modification.py** and **data_conversion.py** scripts prior to importing data into the database to ensure the data is correctly formatted and aggregated. Refer to the `/Documentation` section for further carifications.
