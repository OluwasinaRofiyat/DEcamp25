import pandas as pd
from sqlalchemy import create_engine

def load_csv_to_postgres(csv_path, user, password, host, port, db, table_name):
    """
    Loads a CSV file into a PostgreSQL database.
    
    Parameters:
    csv_path (str): Path to the CSV file.
    user (str): PostgreSQL username.
    password (str): PostgreSQL password.
    host (str): Database host.
    port (int): Database port.
    db (str): Database name.
    table_name (str): Name of the table where data will be inserted.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # Create the PostgreSQL connection string
    conn_string = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    
    # Create an SQLAlchemy engine
    engine = create_engine(conn_string)
    
    try:
        # Write the DataFrame to the specified table
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        print(f"Data successfully loaded into table '{table_name}' in the database '{db}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        engine.dispose()  # Close the connection

# Example usage
load_csv_to_postgres(
    csv_path='/workspaces/DEcamp25/taxi_zone_lookup.csv',
    user='root',
    password='root',
    host='localhost',
    port=5432,
    db='ny_taxi',
    table_name='taxi_zone_lookup'
)
