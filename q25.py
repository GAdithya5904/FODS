from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# User input for new flower's features
sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

# Predict the species of the new flower
new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]
predicted_species = clf.predict(new_flower)

# Map target names to species
species_names = iris.target_names
predicted_species_name = species_names[predicted_species][0]

print(f"The predicted species of the new flower is: {predicted_species_name}")
