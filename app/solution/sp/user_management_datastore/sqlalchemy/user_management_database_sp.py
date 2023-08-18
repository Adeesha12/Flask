from sqlalchemy.sql import *
from sqlalchemy.sql.expression import and_, or_

from core.spi.database_management.user_management_database import UsermanagemantdatabaseSPI
from solution.sp.user_management_datastore.sqlalchemy.global_session import SQLAlchemySessionCreation
from solution.sp.user_management_datastore.model.user_management import UsermanagemantTable

class UsermanagementDatabaseSp(UsermanagemantdatabaseSPI,SQLAlchemySessionCreation):
    def __init__(self, host_name: str, db_name: str, username: str, password: str) -> None:
        super(UsermanagementDatabaseSp, self).__init__(host_name, db_name, username, password)
        
    
    def ingest_data(self):
        pass
    

    def read_data(self):
        pass

    def edit_data(self):
        pass

    def remove_data(self):
        pass
    
    
    