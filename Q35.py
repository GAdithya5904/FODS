def customer_segmentation_kmeans(df):
    features = list(df.columns[:-1])

    # Create a K-Means model
    model = KMeans(n_clusters=5)

    # Fit the model to the data
    model.fit(df[features])

    # Get the cluster labels for each customer
    cluster_labels = model.predict(df[features])

    # Add the cluster labels to the dataset
    df["cluster_label"] = cluster_labels

    # Visualize the clusters
    plt.scatter(df["cluster_label"], df["age"])
    plt.show()
