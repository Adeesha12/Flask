from core.spi.database_management.user_management_database import UsermanagemantdatabaseSPI

class UsermanagementSpRegistery():
    def __init__(self, user_managemant_database: UsermanagemantdatabaseSPI):
        self._user_managemant_database = user_managemant_database
        
    def get_db_sp(self) -> UsermanagemantdatabaseSPI:
        return self._user_managemant_database