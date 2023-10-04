from sqlalchemy.sql import *
from sqlalchemy.exc import SQLAlchemyError, NoResultFound, IntegrityError
from sqlalchemy.sql.expression import and_, or_

from core.spi.database_management.user_management_database import UsermanagemantdatabaseSPI
from solution.sp.user_management_datastore.sqlalchemy.global_session import SQLAlchemySessionCreation
from solution.sp.user_management_datastore.model.user_management import UsermanagemantTable

class UsermanagementDatabaseSp(UsermanagemantdatabaseSPI,SQLAlchemySessionCreation):
    def __init__(self, host_name: str, db_name: str, username: str, password: str) -> None:
        super(UsermanagementDatabaseSp, self).__init__(host_name, db_name, username, password)
        
    
    def insert_data(self, data: UsermanagemantTable):
        try:
            with self.get_session.begin() as session:
                session.add(data)
                session.commit()
        except IntegrityError as e:
            raise Exception(e)
        except SQLAlchemyError as e:
            raise Exception(e)
        except Exception as e:
            raise Exception(e)

    

    def read_data(self,_id:str, _name:str, _occupation:str):
        try:
            # TODO need implemet effient logic to get data from availabe and get all the data 
            column = None
            value = None
            if _id is not None:
                column = UsermanagemantTable.Id
                value = _id
            if _name is not None:
                column = UsermanagemantTable.name 
                value = _name
            if _occupation is not None:
                column = UsermanagemantTable.occupation 
                value = _occupation
            
            stmt = select(UsermanagemantTable).where( column == value)
            with self.get_session.begin() as sesssion:
                result = sesssion.execute(stmt)
                data_row = result.scalar_one()
                response = data_row.dict()
            return response   
        except Exception as e:
            raise Exception(e)
        
   

    def edit_data(self, body, _id:str):
        try:
            stmt = update(UsermanagemantTable).where(UsermanagemantTable.Id == _id).values(body)
            with self.get_session().begin() as session:
                session.execute(stmt)
                session.commit()
        except Exception :
            raise Exception("Error in updating exiesting data ")


    def remove_data(self, _id:str):
        try:
            with self.get_session().begin() as session:
                delete_rows = session.query(UsermanagemantTable).filter(UsermanagemantTable.Id == _id).delete()
                session.commit()
                return delete_rows
        except NoResultFound as e:
            raise Exception("there is no rows in that id")
        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(e)
        except Exception as e:
            raise Exception(e)

    
    