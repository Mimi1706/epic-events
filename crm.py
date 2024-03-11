from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

##  engine is a factory that can create new database connections
engine = create_engine(f'mysql://{DB_USER}:{DB_PASSWORD}@localhost/epic_events_db', echo=True) ## echo will log all SQL commands

inspector = inspect(engine)
table_names = inspector.get_table_names()
