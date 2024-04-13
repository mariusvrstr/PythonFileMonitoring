from src.contracts.source import Source
from src.contracts.stages import Stage 

from datetime import datetime

class ExistingFile():
    filename:str = None
    source:Source = None
    stage:Stage = None
    client_account:str = None
    folder:str = None
    size_in_bytes:int = None
    created_date:datetime = None
    file_hash:str = None
    number_of_changes:int = None
    last_change_date:datetime = None
    from_date:datetime = None
    to_date:datetime = None
    
    @staticmethod
    def Create(filename:str, source:str, stage:str, client_account:str, folder:str, size_in_bytes:int, created_date:datetime, 
               file_hash:str, number_of_changes:int, from_date:datetime, to_date:datetime, last_change_date:datetime):
        
        file = ExistingFile()
        file.filename = filename
        file.source = source
        file.stage = stage
        file.client_account = client_account
        file.folder = folder
        file.size_in_bytes = size_in_bytes
        file.created_date = created_date,
        file.file_hash = file_hash
        file.from_date = from_date
        file.to_date = to_date
        file.last_change_date = last_change_date
        file.number_of_changes = number_of_changes        
        
        return file