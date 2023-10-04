from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Engine = None
Session: sessionmaker = None

class SQLAlchemySessionCreation:
    
    def __init__(self, host_name: str, db_name: str, username: str, password: str) -> None:
        global Engine, Session 
        endpoint = SQLAlchemySessionCreation.create_db_string(host_name,db_name,username,password)
        if not Engine:
            Engine = create_engine(
                endpoint,
                echo=False,
                future=True,
                pool_pre_ping=True,
                connect_args={'connect_timeout': 10}
            )
        Session = sessionmaker(bind=Engine)
    
    @staticmethod
    def get_session():
        return Session
    
    @staticmethod
    def get_engine():
        return Engine
    
    @classmethod
    def create_db_string(cls,host_name, db_name, username, password):
        db_endpoint = f'mysql+mysqlclient://{username}:{password}@{host_name}'
        if db_name:
            db_endpoint = f'{db_endpoint}/{db_name}'
        if not password:
            slice1, slice2 = db_endpoint.split('@')
            db_endpoint = slice1[:-1]+'@'+slice2
        return db_endpoint
            
            