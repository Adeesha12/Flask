from abc import ABC,abstractclassmethod

class UsermanagemantdatabaseSPI(ABC):
    
    
    @abstractclassmethod
    def insert_data(self):
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
    
    