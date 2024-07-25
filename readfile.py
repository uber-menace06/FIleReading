import os
import csv
from datetime import datetime
import pandas as pd
import logging

# logging setup
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def split_csv_by_dob(file_path, dob_str):
    try:
        df = pd.read_csv(file_path)
        dob_date = datetime.strptime(dob_str, '%d-%m-%Y').date()

        # Adjusting the date format to match the actual format in the CSV file
        df['dob'] = pd.to_datetime(df['Date of birth'], format='%Y-%m-%d')
        
        # Filtering rows based on Date of birth
        df_before = df[df['dob'].dt.date < dob_date]
        df_after = df[df['dob'].dt.date > dob_date]

        # Saving in new CSV files
        df_before.to_csv('records_before.csv', index=False)
        df_after.to_csv('records_after.csv', index=False)

        logging.info(f'Successfully split {file_path} into records_before.csv and records_after.csv based on DoB.')
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {str(e)}")

if __name__ == "__main__":
    file_name = "people-1000.csv"
    dob_input = input("Enter Date of Birth (DD-MM-YYYY): ")
    split_csv_by_dob(file_name, dob_input)
