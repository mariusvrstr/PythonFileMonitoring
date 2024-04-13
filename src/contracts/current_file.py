from src.contracts.source import Source
from src.contracts.stages import Stage 

from datetime import datetime

class CurrentFile():

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
        file = CurrentFile()
        file.filename = filename
        file.source = source
        file.stage = stage
        file.client_account = client_account
        file.folder = folder
        file.size_in_bytes = size_in_bytes
        file.created_date = created_date,
        file.file_hash = file_hash
        
        return file
        
 