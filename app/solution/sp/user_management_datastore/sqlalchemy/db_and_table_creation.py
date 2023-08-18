from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import database_exists,create_database

from solution.sp.user_management_datastore.sqlalchemy.global_session import SQLAlchemySessionCreation
from solution.sp.user_management_datastore.model.user_management import init_db

def initialize_db(host_name, db_name, username, password):
    db_end_point = SQLAlchemySessionCreation.create_db_string(host_name, db_name, username, password)
    try:
        if not database_exists(db_end_point):
            create_database(db_end_point)
    except SQLAlchemyError as e:
        raise Exception(e)
    
    try:
        engine = create_engine(db_end_point, echo=True, future=True)        
    except SQLAlchemyError as e:
        raise Exception(e)
    init_db(engine)
    
     