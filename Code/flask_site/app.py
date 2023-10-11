from sqlalchemy import create_engine, inspect
import sqlalchemy
import pandas as pd
import os
from dotenv import load_dotenv 

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}")
engine = create_engine(conn_string)

def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

output = get_tables(engine)
print(output)
    