# db_utils.py

import yaml
import pandas as pd
from sqlalchemy import create_engine, exc

def load_credentials(file_path="credentials.yaml"):
    """
    Load database credentials from a YAML file and return as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
    except FileNotFoundError:
        print(f"Error: Credentials file '{file_path}' not found.")
        return None
    except yaml.YAMLError:
        print("Error: Failed to parse the YAML file. Please check the file format.")
        return None

class RDSDatabaseConnector:
    def __init__(self, credentials):
        """
        Initialize with a dictionary of credentials.
        """
        if not credentials:
            raise ValueError("No credentials provided.")
        self.credentials = credentials
        self.engine = None

    def init_db_engine(self):
        """
        Initialize a SQLAlchemy engine using the provided credentials.
        """
        try:
            connection_string = (
                f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@"
                f"{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/"
                f"{self.credentials['RDS_DATABASE']}"
            )
            self.engine = create_engine(connection_string)
            # Test the connection
            with self.engine.connect():
                print("Database engine initialized and connected.")
        except KeyError as e:
            print(f"Error: Missing database credential '{e}' in the credentials file.")
        except exc.SQLAlchemyError as e:
            print(f"Error initializing database engine: {e}")

    def fetch_data(self, table_name="loan_payments"):
        """
        Fetch data from the specified table and return it as a Pandas DataFrame.
        """
        if not self.engine:
            raise Exception("Database engine not initialized.")
        
        try:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, self.engine)
            print(f"Fetched data from '{table_name}'.")
            print(f"Data shape: {df.shape}")
            return df
        except exc.SQLAlchemyError as e:
            print(f"Error fetching data: {e}")
            return None

    def save_data_to_csv(self, df, file_path="C:/Users/Anas Abubakar/Desktop/data analysis/Task 1/loan_payments.csv"):
        """
        Save the DataFrame to a CSV file in the specified path.
        """
        if df is None or df.empty:
            print("Error: No data to save.")
            return
        try:
            df.to_csv(file_path, index=False)
            print(f"Data saved to '{file_path}'.")
        except IOError as e:
            print(f"Error saving data to '{file_path}': {e}")

    def load_data_from_csv(self, file_path="C:/Users/Anas Abubakar/Desktop/data analysis/Task 1/loan_payments.csv"):
        """
        Load data from a CSV file into a Pandas DataFrame, print its shape, and display a sample.
        """
        try:
            df = pd.read_csv(file_path)
            print(f"Data loaded from '{file_path}'.")
            print(f"Data shape: {df.shape}")
            print(df.head())  # Display the first few rows for a quick overview
            return df
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except pd.errors.EmptyDataError:
            print("Error: No data found in the CSV file.")
            return None
        except pd.errors.ParserError:
            print("Error: Parsing CSV file failed.")
            return None
