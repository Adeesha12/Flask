from abc import ABC,abstractclassmethod

class db_storage(ABC):
    
    
    @abstractclassmethod
    def ingest_data():
        pass
    
    @abstractclassmethod
    def read_data():
        pass
    
    @abstractclassmethod
    def edit_data():
        pass
    
    @abstractclassmethod
    def remove_data():
        pass
    
    