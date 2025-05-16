#!/usr/bin/env python
# coding: utf-8

# # Data Analysis and Visualization Project
# 
# This script performs data loading, exploration, analysis, and visualization on the Iris dataset.

# ## Task 1: Load and Explore the Dataset

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import warnings

# Set plotting style and ignore warnings
sns.set_style("whitegrid")
warnings.filterwarnings('ignore')

# Display plots inline if running in a Jupyter notebook
# %matplotlib inline

def main():
    print("Starting data analysis and visualization project...")
    
    # Load the Iris dataset
    try:
        print("Loading the Iris dataset...")
        iris = load_iris()
        
        # Create a DataFrame with the iris data
        iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        
        # Add the target column (species)
        iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        print("Dataset loaded successfully!")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return
    
    # Display the first 5 rows of the dataset
    print("\n--- First 5 rows of the dataset ---")
    print(iris_df.head())
    
    # Display dataset information
    print("\n--- Dataset Information ---")
    print(f"Dataset shape: {iris_df.shape}")
    print(f"Number of samples: {iris_df.shape[0]}")
    print(f"Number of features: {iris_df.shape[1] - 1}")  # Excluding the target column
    
    # Check for missing values
    print("\n--- Missing Values Check ---")
    missing_values = iris_df.isnull().sum()
    print(missing_values)
    
    if missing_values.sum() > 0:
        print("Cleaning the dataset by filling missing values...")
        # Fill numerical missing values with the mean of their respective columns
        numeric_columns = iris_df.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_columns:
            iris_df[col].fillna(iris_df[col].mean(), inplace=True)
        
        # Fill categorical missing values with the most frequent value
        categorical_columns = iris_df.select_dtypes(include=['object', 'category']).columns
        for col in categorical_columns:
            iris_df[col].fillna(iris_df[col].mode()[0], inplace=True)
        
        print("Missing values handled successfully!")
    else:
        print("No missing values found. The dataset is clean!")
    
    # Display the data types of each column
    print("\n--- Data Types ---")
    print(iris_df.dtypes)
    
    # ## Task 2: Basic Data Analysis
    
    # Compute basic statistics of numerical columns
    print("\n--- Basic Statistics ---")
    print(iris_df.describe())
    
    # Group by species and compute mean of each feature
    print("\n--- Mean Values Grouped by Species ---")
    species_means = iris_df.groupby('species').mean()
    print(species_means)
    
    # Calculate correlations between numerical features
    print("\n--- Correlation Matrix ---")
    correlation_matrix = iris_df.select_dtypes(include=['float64', 'int64']).corr()
    print(correlation_matrix)
    
    # ## Task 3: Data Visualization
    
    # Creating visualizations
    print("\n--- Creating Visualizations ---")
    
    # 1. Line chart: Average measurements per species (simulating a time-series)
    plt.figure(figsize=(12, 6))
    
    # Transpose the grouped means to get features as columns
    species_means_transposed = species_means.transpose()
    
    # Plot each feature as a line across species
    species_means_transposed.plot(marker='o', linestyle='-')
    
    plt.title('Average Measurements per Species')
    plt.xlabel('Features')
    plt.ylabel('Measurement (cm)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('line_chart.png')
    print("Line chart created and saved as 'line_chart.png'")
    
    # 2. Bar chart: Comparison of average sepal length across species
    plt.figure(figsize=(10, 6))
    
    # Plot average sepal length per species
    sns.barplot(x='species', y='sepal length (cm)', data=iris_df, palette='viridis')
    
    plt.title('Average Sepal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Sepal Length (cm)')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('bar_chart.png')
    print("Bar chart created and saved as 'bar_chart.png'")
    
    # 3. Histogram: Distribution of petal length
    plt.figure(figsize=(10, 6))
    
    # Plot histogram of petal length with kernel density estimate
    sns.histplot(data=iris_df, x='petal length (cm)', hue='species', kde=True, bins=20, palette='viridis')
    
    plt.title('Distribution of Petal Length')
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('histogram.png')
    print("Histogram created and saved as 'histogram.png'")
    
    # 4. Scatter plot: Relationship between sepal length and petal length
    plt.figure(figsize=(10, 6))
    
    # Plot scatter plot with different colors for each species
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', 
                  data=iris_df, palette='viridis', s=70)
    
    plt.title('Relationship between Sepal Length and Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('scatter_plot.png')
    print("Scatter plot created and saved as 'scatter_plot.png'")
    
    # 5. Bonus: Pair plot for all numerical features
    plt.figure(figsize=(12, 10))
    
    # Create pair plot to visualize relationships between all features
    pair_plot = sns.pairplot(iris_df, hue='species', palette='viridis', height=2.5)
    pair_plot.fig.suptitle('Pair Plot of Iris Dataset Features', y=1.02, fontsize=16)
    
    plt.tight_layout()
    plt.savefig('pair_plot.png')
    print("Pair plot created and saved as 'pair_plot.png'")
    
    # ## Findings and Observations
    
    print("\n--- Key Findings and Observations ---")
    print("1. Iris setosa has the smallest petal length and width compared to other species.")
    print("2. Iris virginica generally has the largest measurements across most features.")
    print("3. There is a strong positive correlation between petal length and petal width.")
    print("4. The three species are well-separated based on petal measurements.")
    print("5. Sepal measurements show more overlap between species than petal measurements.")
    print("6. Iris setosa is the most distinct species and can be easily identified by its petal size.")
    
    print("\nData analysis and visualization completed successfully!")

if __name__ == "__main__":
    main()
