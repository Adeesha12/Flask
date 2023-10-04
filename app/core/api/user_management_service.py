from abc import ABC,abstractclassmethod

class Usermanagementservice(ABC):
    
    @abstractclassmethod
    def create_user(self):
        pass
    
    @abstractclassmethod
    def get_user(self):
        pass
    
    @abstractclassmethod
    def update_user(self):
        pass
    
    @abstractclassmethod
    def delete_user(self):
        pass