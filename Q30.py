def car_price_prediction(df, new_car_features):
    features = list(df.columns[:-1])
    target = df.columns[-1]

    # Create a CART model
    model = DecisionTreeClassifier()

    # Fit the model to the training data
    model.fit(df[features], df[target])

    # Predict the price of the new car
    predicted_price = model.predict(pd.DataFrame(new_car_features, columns=features))[0]

    # Print the predicted price and the decision path
    print("The predicted price of the new car is:", predicted_price)
    print("The decision path is:", model.decision_path(pd.DataFrame(new_car_features, columns=features)))

