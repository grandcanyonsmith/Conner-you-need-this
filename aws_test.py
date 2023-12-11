import boto3
import pandas as pd
from datetime import datetime

# Initialize a DynamoDB service client with the us-west-2 region
dynamodb = boto3.client('dynamodb', region_name='us-west-2')

# Function to retrieve a list of all DynamoDB tables and their last updated timestamps
def fetch_tables_and_update_info():
    # Create a list to store info about each table
    all_tables_info = []
    # Make the initial request to list tables
    response = dynamodb.list_tables()
    
    # Loop through all tables to accumulate their information
    while True:
        # For every table listed in the response, describe it to get details
        for table_name in response.get('TableNames', []):
            description = dynamodb.describe_table(TableName=table_name)
            # Extract the LastUpdateTime, fall back to January 1, 2000 if not available
            last_updated = description['Table'].get('LastUpdateTime', datetime(2000, 1, 1))
            all_tables_info.append({'TableName': table_name, 'LastUpdated': last_updated})
        
        # Handle response pagination if there are more tables
        if 'LastEvaluatedTableName' in response:
            response = dynamodb.list_tables(ExclusiveStartTableName=response['LastEvaluatedTableName'])
        else:
            break  # No more tables left, exit the loop
    
    return all_tables_info  # Return the list of tables and their last updated timestamps or the default date

# Function to convert the list of DynamoDB table information into a Pandas DataFrame
def convert_to_dataframe():
    tables_info = fetch_tables_and_update_info()
    dataframe = pd.DataFrame(tables_info)
    return dataframe

# Execute the main script
if __name__ == "__main__":
    # Create the DataFrame and print it out
    tables_dataframe = convert_to_dataframe()
    print(tables_dataframe)