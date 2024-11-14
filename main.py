from db_utils import load_credentials, RDSDatabaseConnector

# Use the full path to load credentials
credentials = load_credentials("C:/Users/Anas Abubakar/Desktop/data analysis/Task 1/credentials.yaml")

# Initialize database connector with credentials
db_connector = RDSDatabaseConnector(credentials)
db_connector.init_db_engine()

# Fetch data from the database
data = db_connector.fetch_data()

# Save the fetched data to a CSV file
db_connector.save_data_to_csv(data)

# Load data from CSV and display a sample
data_from_csv = db_connector.load_data_from_csv()
