import boto3
import pandas as pd
from datetime import datetime, timezone

# Initialize a DynamoDB service client with the us-west-2 region
dynamodb = boto3.client('dynamodb', region_name='us-west-2')

# Function to retrieve a list of all DynamoDB tables and their creation timestamps
def fetch_tables_and_creation_info():
    all_tables_info = []
    response = dynamodb.list_tables()

    while True:
        for table_name in response.get('TableNames', []):
            description = dynamodb.describe_table(TableName=table_name)
            # Extract the CreationDateTime
            creation_time_utc = description['Table']['CreationDateTime']
            all_tables_info.append({
                'TableName': table_name,
                'CreatedAt': creation_time_utc
            })

        if 'LastEvaluatedTableName' in response:
            response = dynamodb.list_tables(
                ExclusiveStartTableName=response['LastEvaluatedTableName'])
        else:
            break

    # Sort tables by creation date
    sorted_tables_info = sorted(all_tables_info, key=lambda x: x['CreatedAt'])
    return sorted_tables_info

# Function to convert the list of DynamoDB table information into a Pandas DataFrame, including formatting the creation date
def convert_to_dataframe(tables_info):
    # Format creation dates
    for table in tables_info:
        table['CreatedAt'] = table['CreatedAt'].strftime('%b. %d %Y %I:%M %p')

    # Convert to DataFrame
    dataframe = pd.DataFrame(tables_info)
    return dataframe

# Execute the main script
if __name__ == "__main__":
    tables_info = fetch_tables_and_creation_info()
    tables_dataframe = convert_to_dataframe(tables_info)
    print(tables_dataframe)