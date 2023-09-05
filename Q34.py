def medical_treatment_outcome_prediction(df):
    features = list(df.columns[:-1])
    target = df.columns[-1]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2)

    # Create a KNN model
    model = KNeighborsClassifier(n_neighbors=5)

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Evaluate the model on the test data
    accuracy = model.score(X_test, y_test)

    print("Accuracy on test data:", accuracy)

    # Print the confusion matrix
    print(confusion_matrix(y_test, model.predict(X_test)))
