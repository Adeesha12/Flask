from abc import ABC,abstractclassmethod

class db_storage(ABC):
    
    
    @abstractclassmethod
    def ingest_data(self):
        pass
    
    @abstractclassmethod
    def read_data(self):
        pass
    
    @abstractclassmethod
    def edit_data(self):
        pass
    
    @abstractclassmethod
    def remove_data(self):
        pass
    
    