from src.contracts.source import Source
from src.contracts.stages import Stage 

from datetime import datetime

class CurrentFile:

    filename:str = None
    source:Source = None
    stage:Stage = None
    client_account:str = None
    folder:str = None
    size_in_bytes:int = None
    created_date:datetime = None
    file_hash:str = None
    
    @staticmethod
    def Create(filename:str, source:str, stage:str, client_account:str, folder:str, size_in_bytes:int, created_date:datetime, file_hash:str):        
        return CurrentFile (filename=filename, source=source, stage=stage, client_account=client_account, folder=folder, 
                            size_in_bytes=size_in_bytes, created_date=created_date, file_hash=file_hash)
        
 