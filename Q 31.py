def customer_segmentation(df):
    features = list(df.columns[:-1])

    # Create a K-Means model
    model = KMeans(n_clusters=5)

    # Fit the model to the data
    model.fit(df[features])

    # Get the cluster labels for each customer
    cluster_labels = model.predict(df[features])

    # Add the cluster labels to the dataset
    df["cluster_label"] = cluster_labels

    # Print the number of customers in each cluster
    print("Number of customers in each cluster:")
    print(df["cluster_label"].value_counts())
