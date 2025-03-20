from google.cloud import bigquery
import config

def query_bigquery():
    """
    Runs a SQL query on BigQuery and prints the results.
    """
    # Initialize BigQuery client
    client = bigquery.Client(project=config.GCP_PROJECT_ID)

    # Define the SQL query
    query = f"""
        SELECT * 
        FROM `{config.GCP_PROJECT_ID}.{config.DATASET_NAME}.{config.TABLE_NAME}`
        LIMIT 10
    """

    # Run the query
    query_job = client.query(query)  # API request

    # Fetch results
    results = query_job.result()

    # Print results
    print("\nQuery Results:")
    for row in results:
        print(row)

if __name__ == "__main__":
    query_bigquery()
