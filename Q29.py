def evaluate_model(df, features_to_use, model):
    accuracy = accuracy_score(df[target], model.predict(df[features_to_use]))
    precision, recall, f1, _ = precision_recall_fscore_support(df[target], model.predict(df[features_to_use]))

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)
