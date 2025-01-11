import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import logging
import os

# Set up logging
log_file = os.path.join("5_logs", "data_segmentation.log")
os.makedirs("5_logs", exist_ok=True)
os.makedirs("2_data", exist_ok=True)
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data(file_path):
    """
    Loads the dataset from the given file path.
    """
    try:
        logging.info("Loading data from %s", file_path)
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error("Error loading data: %s", e)
        raise

def perform_segmentation(data, n_clusters=5):
    """
    Performs K-means clustering on the data.
    """
    try:
        logging.info("Starting K-means clustering with %d clusters.", n_clusters)
        
        # Select features for clustering
        features = data[["Annual Income (k$)", "Spending Score (1-100)"]]
        
        # Normalize the data
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        
        # Apply K-means
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(scaled_features)
        
        # Add cluster labels to the dataset
        data["Cluster"] = clusters
        logging.info("Clustering completed successfully.")
        return data
    except Exception as e:
        logging.error("Error during clustering: %s", e)
        raise

def save_data(data, file_path):
    """
    Saves the segmented data to the given file path.
    """
    try:
        logging.info("Saving segmented data to %s", file_path)
        data.to_csv(file_path, index=False)
        logging.info("Segmented data saved successfully.")
    except Exception as e:
        logging.error("Error saving data: %s", e)
        raise

if __name__ == "__main__":
    try:
        print("Starting data segmentation...")
        input_file = os.path.join("2_data", "Mall_Customers.csv")
        output_file = os.path.join("2_data", "segmented_Mall_Customers.csv")
        
        # Load data
        customer_data = load_data(input_file)
        
        # Perform segmentation
        segmented_data = perform_segmentation(customer_data)
        
        # Save segmented data
        save_data(segmented_data, output_file)
        
        print("Data segmentation completed successfully.")
        print(f"Segmented data saved to {output_file}")
    except Exception as main_exception:
        print(f"An error occurred: {main_exception}")