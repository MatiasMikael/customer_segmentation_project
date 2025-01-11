import pandas as pd
import matplotlib.pyplot as plt
import logging
import os

# Set up logging
log_file = os.path.join("5_logs", "data_visualization.log")
os.makedirs("5_logs", exist_ok=True)
os.makedirs("3_results", exist_ok=True)
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data(file_path):
    """
    Loads the segmented data from the given file path.
    """
    try:
        logging.info("Loading segmented data from %s", file_path)
        data = pd.read_csv(file_path)
        logging.info("Segmented data loaded successfully.")
        return data
    except Exception as e:
        logging.error("Error loading segmented data: %s", e)
        raise

def plot_clusters(data):
    """
    Creates a scatter plot visualizing customer clusters.
    """
    try:
        logging.info("Creating cluster visualization...")
        
        # Plot each cluster
        plt.figure(figsize=(10, 6))
        for cluster in data['Cluster'].unique():
            cluster_data = data[data['Cluster'] == cluster]
            plt.scatter(
                cluster_data['Annual Income (k$)'],
                cluster_data['Spending Score (1-100)'],
                label=f"Cluster {cluster}"
            )
        
        # Add plot details
        plt.title("Customer Segments", fontsize=14)
        plt.xlabel("Annual Income (k$)", fontsize=12)
        plt.ylabel("Spending Score (1-100)", fontsize=12)
        plt.legend(title="Clusters")
        plt.grid(True)
        
        # Save plot
        output_file = os.path.join("3_results", "cluster_visualization.png")
        plt.savefig(output_file)
        logging.info("Cluster visualization saved to %s", output_file)
        print(f"Cluster visualization saved to {output_file}")
        
        plt.show()
    except Exception as e:
        logging.error("Error creating cluster visualization: %s", e)
        raise

if __name__ == "__main__":
    try:
        print("Starting cluster visualization...")
        input_file = os.path.join("2_data", "segmented_Mall_Customers.csv")
        
        # Load segmented data
        segmented_data = load_data(input_file)
        
        # Plot clusters
        plot_clusters(segmented_data)
        
        print("Cluster visualization completed successfully.")
    except Exception as main_exception:
        logging.error("Error in main execution: %s", main_exception)
        print(f"An error occurred: {main_exception}")