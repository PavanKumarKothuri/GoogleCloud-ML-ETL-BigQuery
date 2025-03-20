import transform_data
import upload_to_gcs
import load_to_bigquery

# Step 1: Clean Data
transform_data.clean_data("sample_data.csv", "cleaned_data.csv")

# Step 2: Upload to GCS
upload_to_gcs.upload_to_gcs("cleaned_data.csv", "cleaned_data.csv")

# Step 3: Load into BigQuery
load_to_bigquery.load_gcs_to_bigquery()

print("🚀 ETL Pipeline Completed Successfully!")