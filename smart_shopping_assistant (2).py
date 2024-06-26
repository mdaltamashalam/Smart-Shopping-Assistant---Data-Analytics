# -*- coding: utf-8 -*-
"""Smart Shopping Assistant.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SO8MZ_Utndk5-5xm_dA8QeCzvvzdUHII

###                                         Smart Shopping Assistant

**Load the data and Data Preprocessing with CSV**
"""

import pandas as pd

# Load product data from a CSV file
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Example usage:
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"
product_data = load_data(file_path)

from google.colab import drive
drive.mount('/content/drive')

import csv

# Function to load and preprocess data from a CSV file
def preprocess_data_csv(file_path):
    product_data = []

    # Read data from CSV file
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check if all required columns are present
            if 'Product' not in row or 'Price' not in row or 'Category' not in row:
                continue

            # Check for missing values
            if not all(row.values()):
                continue

            # Convert price to numeric, handling errors
            try:
                row['Price'] = float(row['Price'])
            except ValueError:
                continue

            product_data.append(row)

    return product_data

# Example usage:
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"
cleaned_product_data = preprocess_data_csv(file_path)

"""**Product Comparison Algorithm with CSV**"""

import csv

# Function to load data from a CSV file
def load_data_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Product Comparison Algorithm
def compare_products(product1, product2):
    if product1['Purchase Amount (USD)'] < product2['Purchase Amount (USD)']:
        return f"{product1['Item Purchased']} is cheaper than {product2['Item Purchased']}"
    elif product1['Purchase Amount (USD)'] > product2['Purchase Amount (USD)']:
        return f"{product1['Item Purchased']} is more expensive than {product2['Item Purchased']}"
    else:
        return f"{product1['Item Purchased']} and {product2['Item Purchased']} have the same price"

# Example usage:
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"
product_data = load_data_csv(file_path)

if len(product_data) >= 2:
    product1 = product_data[0]
    product2 = product_data[1]
    comparison_result = compare_products(product1, product2)
    print(comparison_result)
else:
    print("Insufficient data for comparison.")

"""**Product Recommendations : Smart Shopping**"""

import csv

# Function to load data from a CSV file
def load_data_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Function to recommend products similar to a given product
def recommend_products(product_name, product_data):
    recommended_products = []

    # Find the product with the given name
    for product in product_data:
        if 'Item Purchased' in product and product['Item Purchased'] == product_name:
            target_product = product
            break
    else:
        print(f"Product '{product_name}' not found.")
        return recommended_products

    # Find similar products based on category
    for product in product_data:
        if 'Category' in product and product['Category'] == target_product['Category'] and 'Item Purchased' in product and product['Item Purchased'] != target_product['Item Purchased']:
            recommended_products.append(product)

    return recommended_products

# Example usage:
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"
product_data = load_data_csv(file_path)

product_name = "Sweater"
recommendations = recommend_products(product_name, product_data)

if recommendations:
    print(f"Products similar to '{product_name}':")
    for product in recommendations:
        print(product)
else:
    print("No recommendations available.")

import csv
import matplotlib.pyplot as plt

# Function to load data from a CSV file
def load_data_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Function to recommend products similar to a given product
def recommend_products(product_name, product_data):
    recommended_products = []

    # Find the product with the given name
    for product in product_data:
        if 'Item Purchased' in product and product['Item Purchased'] == product_name:
            target_product = product
            break
    else:
        print(f"Product '{product_name}' not found.")
        return recommended_products

    # Find similar products based on category
    for product in product_data:
        if 'Category' in product and product['Category'] == target_product['Category'] and 'Item Purchased' in product and product['Item Purchased'] != target_product['Item Purchased']:
            recommended_products.append(product)

    return recommended_products

# Example usage:
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"
product_data = load_data_csv(file_path)

product_name = "Sweater"
recommendations = recommend_products(product_name, product_data)

if recommendations:
    print(f"Products similar to '{product_name}':")
    for product in recommendations:
        print(product)

    # Extract category labels from recommendations
    categories = [product['Category'] for product in recommendations]

    # Plot histogram of recommended product categories
    plt.hist(categories, bins=len(set(categories)), edgecolor='black')
    plt.xlabel('Product Category')
    plt.ylabel('Frequency')
    plt.title('Recommended Products by Category')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("No recommendations available.")

import csv
import matplotlib.pyplot as plt
from collections import Counter

# Function to load data from a CSV file
def load_data_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Function to recommend products similar to a given product
def recommend_products(product_name, product_data):
    recommended_products = []

    # Find the product with the given name
    for product in product_data:
        if 'Item Purchased' in product and product['Item Purchased'] == product_name:
            target_product = product
            break
    else:
        print(f"Product '{product_name}' not found.")
        return recommended_products

    # Find similar products based on category
    for product in product_data:
        if 'Category' in product and 'Item Purchased' in product and product['Item Purchased'] != target_product['Item Purchased']:
            recommended_products.append(product)

    return recommended_products

# Example usage:
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"
product_data = load_data_csv(file_path)

product_name = "Sweater"
recommendations = recommend_products(product_name, product_data)

if recommendations:
    print(f"Products similar to '{product_name}':")
    for product in recommendations:
        print(product)

    # Extract category labels from recommendations
    categories = [product['Category'] for product in recommendations]

    # Count occurrences of each category
    category_counts = Counter(categories)

    # Sort categories and corresponding counts for plotting
    sorted_categories = sorted(category_counts.keys())
    counts = [category_counts[cat] for cat in sorted_categories]

    # Plot line graph of recommended product categories
    plt.plot(sorted_categories, counts, marker='o', linestyle='-')
    plt.xlabel('Product Category')
    plt.ylabel('Frequency')
    plt.title('Recommended Products by Category')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("No recommendations available.")

# Function to recommend products similar to a given product and compare their prices
def recommend_and_compare_prices(product_name, product_data):
    recommended_products = []

    # Find the product with the given name
    target_product = None
    for product in product_data:
        if 'Item Purchased' in product and product['Item Purchased'] == product_name:
            target_product = product
            break

    if target_product is None:
        print(f"Product '{product_name}' not found.")
        return

    # Find similar products based on category
    for product in product_data:
        if ('Category' in product and 'Purchase Amount (USD)' in product and
            product['Category'] == target_product['Category'] and
            product['Item Purchased'] != target_product['Item Purchased']):
            recommended_products.append(product)

    if not recommended_products:
        print(f"No similar products found for '{product_name}'.")
        return

    # Print price comparison
    print(f"Price comparison for products similar to '{product_name}':")
    for product in recommended_products:
        print(f"{product['Item Purchased']}: ${product['Purchase Amount (USD)']} vs {target_product['Item Purchased']}: ${target_product['Purchase Amount (USD)']}")

file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"
product_data = load_data_csv(file_path)

product_name = "T-shirt"
recommend_and_compare_prices(product_name, product_data)

"""**Accuracy of the Smart Shopping system**"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

# Load the dataset from CSV
data = pd.read_csv('/content/drive/MyDrive/Smart Home /shopping_trends.csv')

# Define the target column
target_column = 'Subscription Status'

# Extracting target variable
y = data[target_column]

# Dropping non-target columns from features
X = data.drop(columns=[target_column])

# Check for missing values in features
if X.isnull().any().any():
    # Impute missing values
    imputer = SimpleImputer(strategy='mean')  # You can also use 'median' or 'most_frequent' strategy
    X_imputed = imputer.fit_transform(X)
    X = pd.DataFrame(X_imputed, columns=X.columns)

# Encoding categorical variables in features if any
X = pd.get_dummies(X)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Making predictions
rf_pred = rf_model.predict(X_test)

# Calculating accuracy
accuracy = accuracy_score(y_test, rf_pred)
print("Random Forest Accuracy:", accuracy)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Change the import
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

# Load the dataset from CSV
data = pd.read_csv('/content/drive/MyDrive/Smart Home /shopping_trends.csv')

# Define the target column
target_column = 'Subscription Status'

# Extracting target variable
y = data[target_column]

# Dropping non-target columns from features
X = data.drop(columns=[target_column])

# Check for missing values in features
if X.isnull().any().any():
    # Impute missing values
    imputer = SimpleImputer(strategy='mean')  # You can also use 'median' or 'most_frequent' strategy
    X_imputed = imputer.fit_transform(X)
    X = pd.DataFrame(X_imputed, columns=X.columns)

# Encoding categorical variables in features if any
X = pd.get_dummies(X)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Decision Tree model  # Change the classifier
dt_model = DecisionTreeClassifier(random_state=42)  # Change the classifier
dt_model.fit(X_train, y_train)  # Change the classifier

# Making predictions
dt_pred = dt_model.predict(X_test)  # Change the predictions

# Calculating accuracy
accuracy = accuracy_score(y_test, dt_pred)  # Change the accuracy calculation
print("Decision Tree Accuracy:", accuracy)  # Change the print statement

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Load the dataset from CSV
data = pd.read_csv('/content/drive/MyDrive/Smart Home /shopping_trends.csv')

# Define the target column
target_column = 'Subscription Status'

# Extracting target variable
y = data[target_column]

# Dropping non-target columns from features
X = data.drop(columns=[target_column])

# Check for missing values in features
if X.isnull().any().any():
    # Impute missing values
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)
    X = pd.DataFrame(X_imputed, columns=X.columns)

# Encoding categorical variables in features if any
X = pd.get_dummies(X)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Making predictions with Random Forest
rf_pred = rf_model.predict(X_test)

# Calculating accuracy for Random Forest
rf_accuracy = accuracy_score(y_test, rf_pred)

# Training the Decision Tree model
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# Making predictions with Decision Tree
dt_pred = dt_model.predict(X_test)

# Calculating accuracy for Decision Tree
dt_accuracy = accuracy_score(y_test, dt_pred)

# Plotting line graphs for accuracy
models = ['Random Forest', 'Decision Tree']
accuracies = [rf_accuracy, dt_accuracy]

plt.figure(figsize=(10, 6))
plt.plot(models, accuracies, marker='o', linestyle='-', color='b')
plt.title('Accuracy Comparison between Random Forest and Decision Tree')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.ylim(0, 1)
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Plotting histogram for accuracy
plt.figure(figsize=(8, 6))
plt.bar(models, accuracies, color=['blue', 'green'])
plt.title('Accuracy Comparison between Random Forest and Decision Tree')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.ylim(0, 1)
plt.grid(axis='y')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"  # Replace "your_file_path_here.csv" with the actual file path
df = pd.read_csv(file_path)

# Plot histogram of purchase amounts
plt.figure(figsize=(10, 6))
plt.hist(df['Purchase Amount (USD)'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Purchase Amounts')
plt.xlabel('Purchase Amount (USD)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"  # Replace "your_file_path_here.csv" with the actual file path
df = pd.read_csv(file_path)

# Get unique categories
unique_categories = df['Category'].unique()

# Plot histogram of purchase amounts with different colors for each category
plt.figure(figsize=(10, 6))
for category in unique_categories:
    category_data = df[df['Category'] == category]['Purchase Amount (USD)']
    plt.hist(category_data, bins=10, alpha=0.5, label=category)

plt.title('Distribution of Purchase Amounts by Category')
plt.xlabel('Purchase Amount (USD)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Plot pie chart of purchase categories
category_counts = df['Category'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Purchases by Category')
plt.axis('equal')
plt.show()

"""**Trends Analysis**"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"  # Replace "your_file_path_here.csv" with the actual file path
df = pd.read_csv(file_path)

# Aggregate data by category
category_groups = df.groupby('Category')

# Plot trend of 'Purchase Amount (USD)' for each category
plt.figure(figsize=(10, 6))
for category, group_data in category_groups:
    plt.plot(group_data.index, group_data['Purchase Amount (USD)'], marker='o', linestyle='-', label=category)

plt.title('Trend of Purchase Amount (USD) by Category')
plt.xlabel('Sequence of Rows')
plt.ylabel('Purchase Amount (USD)')
plt.legend()
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = "/content/drive/MyDrive/Smart Home /shopping_trends.csv"  # Replace "your_file_path_here.csv" with the actual file path
df = pd.read_csv(file_path)

# Aggregate data by category and count the number of items purchased in each category
category_purchase_count = df.groupby('Category').size()

# Plot trend of number of items purchased for each category
plt.figure(figsize=(10, 6))
category_purchase_count.plot(kind='bar', color='skyblue')
plt.title('Number of Items Purchased by Category')
plt.xlabel('Category')
plt.ylabel('Number of Items Purchased')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()