from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import DbConfig

# Create the database connection URL
db_url = f'mysql+mysqlclient://{DbConfig.DB_USER}:{DbConfig.DB_PASSWORD}@{DbConfig.DB_HOST}:{DbConfig.DB_PORT}/{DbConfig.DB_NAME}'

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Declare a base for table creation
Base = declarative_base()

# Define your data table
class DataTable(Base):
    __tablename__ = 'solution_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    occupation = Column(String)
    Address = Column(String)

# Check if the table exists, and if not, create it
if not engine.dialect.has_table(engine, 'solution_table'):
    Base.metadata.create_all(engine)
    print("create Table if not exist !")

# Close the session
session.close()