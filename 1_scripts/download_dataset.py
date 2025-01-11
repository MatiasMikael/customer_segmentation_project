import kagglehub
import logging
import os
import shutil

# Set up logging
log_file = os.path.join("5_logs", "dataset_download.log")
os.makedirs("5_logs", exist_ok=True)
os.makedirs("2_data", exist_ok=True)  # Ensure the target folder exists
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def download_dataset():
    """
    Downloads the dataset from Kaggle using kagglehub, moves it to '2_data' folder, and logs the process.
    """
    try:
        logging.info("Starting dataset download...")
        print("Downloading dataset...")
        
        # Download the dataset
        path = kagglehub.dataset_download("vjchoudhary7/customer-segmentation-tutorial-in-python")
        logging.info(f"Dataset downloaded successfully to: {path}")
        
        # Move dataset to '2_data' folder
        for file_name in os.listdir(path):
            source = os.path.join(path, file_name)
            destination = os.path.join("2_data", file_name)
            shutil.move(source, destination)
        
        logging.info("Dataset moved to '2_data' folder.")
        print("Dataset moved to '2_data' folder successfully.")
    except Exception as e:
        logging.error("Failed to download or move dataset: %s", e)
        print(f"Error occurred during dataset download or move: {e}")

if __name__ == "__main__":
    download_dataset()