# plotter.py

import pandas as pd  # Add this line to import pandas
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_nulls(self):
        """Visualize NULL values in each column."""
        null_counts = self.df.isnull().sum()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=null_counts.index, y=null_counts.values)
        plt.xticks(rotation=90)
        plt.title("Count of NULL values per column")
        plt.show()

    def plot_correlation_matrix(self):
        """Plot a heatmap of the correlation matrix."""
        corr_matrix = self.df.corr()
        plt.figure(figsize=(12, 10))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Matrix")
        plt.show()

    def plot_skew_distribution(self, columns):
        """Visualize the distribution to check skewness."""
        for col in columns:
            plt.figure(figsize=(6, 4))
            sns.histplot(self.df[col].dropna(), kde=True)
            plt.title(f"Distribution of {col}")
            plt.show()
