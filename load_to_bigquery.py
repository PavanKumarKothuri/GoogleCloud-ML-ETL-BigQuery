from google.cloud import bigquery
import config

def load_gcs_to_bigquery():
    """Loads data from GCS to BigQuery."""
    client = bigquery.Client()
    table_id = f"{config.GCP_PROJECT_ID}.{config.DATASET_NAME}.{config.TABLE_NAME}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    uri = f"gs://{config.BUCKET_NAME}/sample_data.csv"

    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()

    print(f"✅ Data loaded into {table_id}")

if __name__ == "__main__":
    load_gcs_to_bigquery()