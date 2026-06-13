import os
import datetime
import pandas as pd
from sqlalchemy import create_engine

# --- CONFIGURATION ---
# TODO: Replace 'YOUR_PASSWORD' with the actual password you set during PostgreSQL installation
DB_PASSWORD = '100624'
DB_USER = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'retail_warehouse'

# File paths
CSV_FILE_PATH = 'raw_data/SampleSuperstore.csv' # Adjust if your folder structure or file name is slightly different
TABLE_NAME = 'cleaned_sales'

def run_etl():
    print("🚀 Starting ETL Pipeline...")
    
    # 1. EXTRACT
    if not os.path.exists(CSV_FILE_PATH):
        # Fallback if you didn't put it in a raw_data subfolder yet and it's just in the same directory
        if os.path.exists('SampleSuperstore.csv'):
            path_to_use = 'SampleSuperstore.csv'
        else:
            print(f"❌ Error: Could not find the dataset at {CSV_FILE_PATH}")
            return
    else:
        path_to_use = CSV_FILE_PATH

    print(f"📥 Extracting data from: {path_to_use}")
    df = pd.read_csv(path_to_use)
    
    # 2. TRANSFORM
    print("🧹 Transforming and cleaning data...")
    
    # Standardize column names to lowercase and replace spaces/hyphens with underscores
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
    
    # Add a metadata column to keep track of when data entered the warehouse
    df['etl_inserted_at'] = datetime.datetime.now()
    
    print(f"✅ Cleaned columns: {list(df.columns)}")
    print(f"📊 Total rows to process: {len(df)}")
    
    # 3. LOAD
    print("📤 Loading data into PostgreSQL...")
    try:
        # Create database connection engine
        connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(connection_string)
        
        # Load data to PostgreSQL (if table exists, it will replace it)
        df.to_sql(name=TABLE_NAME, con=engine, if_exists='replace', index=False)
        print(f"🎉 Success! Data successfully loaded into table '{TABLE_NAME}' in '{DB_NAME}' database.")
        
    except Exception as e:
        print(f"❌ Database error: {e}")

if __name__ == "__main__":
    run_etl()