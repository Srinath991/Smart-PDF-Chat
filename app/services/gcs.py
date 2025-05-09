from google.cloud import storage
from core.config import settings

def upload_to_gcs(file, filename: str):
    client = storage.Client()
    bucket = client.bucket(settings.GCS_BUCKET)
    blob = bucket.blob(filename)
    blob.upload_from_file(file.file)
    return filename  # Only return the blob name

