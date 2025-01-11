import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data
@st.cache
def load_data(file_path):
    """
    Load the dataset from the given file path.
    """
    data = pd.read_csv(file_path)
    return data

# Plot clusters
def plot_clusters(data, selected_clusters):
    """
    Create a scatter plot for the selected clusters.
    """
    plt.figure(figsize=(10, 6))
    for cluster in selected_clusters:
        cluster_data = data[data['Cluster'] == cluster]
        plt.scatter(
            cluster_data['Annual Income (k$)'],
            cluster_data['Spending Score (1-100)'],
            label=f"Cluster {cluster}"
        )
    plt.title("Customer Segments", fontsize=14)
    plt.xlabel("Annual Income (k$)", fontsize=12)
    plt.ylabel("Spending Score (1-100)", fontsize=12)
    plt.legend(title="Clusters")
    plt.grid(True)
    st.pyplot(plt)

# Main application
def main():
    """
    Main Streamlit application for customer segmentation report.
    """
    st.title("Customer Segmentation Report")
    st.write("""
        This Streamlit report visualizes customer segments identified through K-means clustering.
        The cluster descriptions below help in understanding the meaning of each cluster.
    """)

    # Cluster descriptions
    cluster_descriptions = {
        0: "Average Income & Average Spending (40–70 k$)",
        1: "High Income & High Spending (70–140 k$)",
        2: "Low Income & High Spending (15–40 k$)",
        3: "High Income & Low Spending (70–140 k$)",
        4: "Low Income & Low Spending (15–40 k$)"
    }

    st.subheader("Cluster Descriptions")
    for cluster, description in cluster_descriptions.items():
        st.write(f"**Cluster {cluster}:** {description}")

    # Load data
    data_file = "2_data/segmented_Mall_Customers.csv"
    data = load_data(data_file)

    # Cluster selection
    st.subheader("Select Clusters to Display")
    clusters = data['Cluster'].unique()
    selected_clusters = st.multiselect(
        "Choose clusters to visualize:", clusters, default=clusters
    )

    # Plot selected clusters
    if selected_clusters:
        st.subheader("Cluster Visualization")
        plot_clusters(data, selected_clusters)
    else:
        st.warning("Please select at least one cluster to display.")

if __name__ == "__main__":
    main()