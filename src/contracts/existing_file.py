from src.contracts.source import Source
from src.contracts.stages import Stage 

from datetime import datetime

class ExistingFile:
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
        
        return ExistingFile (filename=filename, source=source, stage=stage, client_account=client_account, folder=folder, size_in_bytes=size_in_bytes,
                created_date=created_date, file_hash=file_hash, number_of_changes=number_of_changes, from_date=from_date, to_date=to_date, last_change_date=last_change_date)