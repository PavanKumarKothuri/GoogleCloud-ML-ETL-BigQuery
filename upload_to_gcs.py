from google.cloud import storage
import config

def upload_to_gcs(source_file, destination_blob):
    """Uploads a file to Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(config.BUCKET_NAME)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(source_file)
    print(f"✅ File {source_file} uploaded to {destination_blob} in {config.BUCKET_NAME}")

if __name__ == "__main__":
    upload_to_gcs("sample_data.csv", "sample_data.csv")