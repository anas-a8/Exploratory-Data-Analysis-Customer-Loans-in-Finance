import pandas as pd
import numpy as np
from scipy.stats import skew

class DataTransform:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def identify_non_numeric_columns(self):
        """Identify columns with non-numeric values."""
        non_numeric_cols = []
        for col in self.df.columns:
            if not pd.api.types.is_numeric_dtype(self.df[col]):
                non_numeric_cols.append(col)
                print(f"Column '{col}' contains non-numeric values or is not numeric.")
        return non_numeric_cols

    def convert_to_numeric(self, columns=None):
        """Convert specified or all possible columns to numeric data type."""
        if columns is None:
            columns = self.df.select_dtypes(include=['object', 'string']).columns.tolist()
        for col in columns:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
            if self.df[col].isnull().any():
                num_missing = self.df[col].isnull().sum()
                print(f"Warning: {num_missing} non-numeric values in '{col}' were coerced to NaN.")
        print("Converted to numeric:", columns)

    def convert_to_datetime(self, columns, date_format=None):
        """Convert specified columns to datetime data type."""
        for col in columns:
            self.df[col] = pd.to_datetime(self.df[col], format=date_format, errors='coerce')
        print("Converted to datetime:", columns)

    def convert_to_categorical(self, columns):
        """Convert specified columns to categorical data type."""
        for col in columns:
            self.df[col] = self.df[col].astype('category')
        print("Converted to categorical:", columns)

    def impute_missing(self, strategy='mean'):
        """Impute missing values with mean or median for numerical columns only."""
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                if self.df[col].isnull().sum() > 0:
                    try:
                        if strategy == 'mean':
                            mean_val = self.df[col].mean()
                            if pd.notna(mean_val):
                                self.df[col].fillna(mean_val, inplace=True)
                            else:
                                print(f"Skipping imputation for column '{col}' as it has no valid numeric data.")
                        elif strategy == 'median':
                            median_val = self.df[col].median()
                            if pd.notna(median_val):
                                self.df[col].fillna(median_val, inplace=True)
                            else:
                                print(f"Skipping imputation for column '{col}' as it has no valid numeric data.")
                    except TypeError as e:
                        print(f"TypeError for column '{col}': {e}")
            else:
                print(f"Skipping non-numeric column: {col}")
        print("Missing values imputed using", strategy)

    def remove_outliers(self, columns, threshold=3):
        """Remove outliers beyond a specified Z-score threshold."""
        for col in columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                z_scores = (self.df[col] - self.df[col].mean()) / self.df[col].std()
                self.df = self.df[(np.abs(z_scores) < threshold)]
        print("Outliers removed from:", columns)

    def reduce_skew(self, columns):
        """Apply transformations to reduce skew in specified columns."""
        for col in columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                if skew(self.df[col].dropna()) > 1:
                    self.df[col] = np.log1p(self.df[col])
        print("Skew reduced for columns:", columns)

    def drop_highly_correlated(self, threshold=0.8):
        """
        Drop columns that have a high correlation above the threshold.
        Only numeric columns are considered for correlation calculation.
        """
        # Select only numeric columns for correlation calculation
        numeric_columns = self.df.select_dtypes(include=[np.number])
        
        # Calculate the correlation matrix for numeric columns
        corr_matrix = numeric_columns.corr().abs()
        
        # Identify columns to drop based on the correlation threshold
        upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > threshold)]
        
        # Drop highly correlated columns from the original DataFrame
        self.df.drop(columns=to_drop, inplace=True)
        print("Dropped highly correlated columns:", to_drop)

class DataFrameInfo:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def describe_columns(self):
        """Display data types and general information for each column."""
        return self.df.info()

    def calculate_statistics(self):
        """Calculate and return mean, median, and standard deviation of numerical columns."""
        stats = self.df.describe().T[['mean', '50%', 'std']]
        stats.rename(columns={'50%': 'median'}, inplace=True)
        return stats

    def count_distinct(self, columns):
        """Count distinct values in categorical columns."""
        return {col: self.df[col].nunique() for col in columns}

    def get_shape(self):
        """Return the shape (rows, columns) of the DataFrame."""
        return self.df.shape

    def count_nulls(self):
        """Return the count and percentage of NULL values in each column."""
        null_counts = self.df.isnull().sum()
        null_percent = (self.df.isnull().mean() * 100)
        return pd.DataFrame({'null_count': null_counts, 'null_percent': null_percent})
