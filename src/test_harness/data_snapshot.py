from src.contracts.source import Source
from src.contracts.stages import Stage
from src.contracts.current_file import CurrentFile
from src.contracts.existing_file import ExistingFile

from datetime import datetime


class DataSnapshot():
    
    current_files:dict[int, any] = None
    existing_files:dict[int, any] = None
    
    def __init__(self) -> None:
        self.current_files = dict()
        self.existing_files = dict()
    
    def add_current_file(self, current_file:CurrentFile) -> CurrentFile:
        max_key = max(self.current_files.keys(), default=0)
        next_key = max_key+1
        
        self.current_files[next_key] = [current_file.client_account, current_file.filename, current_file.folder, current_file.size_in_bytes, 
                    current_file.created_date, current_file.source, current_file.stage, current_file.file_hash]
        
        return current_file
    
    def add_existing_file(self, monitored_file:ExistingFile) -> ExistingFile:
        max_key = max(self.existing_files.keys(), default=0)
        next_key = max_key+1
        
        self.existing_files[next_key] = [monitored_file.client_account, monitored_file.filename, monitored_file.size_in_bytes, 
                    monitored_file.file_hash, monitored_file.last_change_date, monitored_file.source, monitored_file.stage, monitored_file.number_of_changes, 
                    monitored_file.from_date, monitored_file.to_date]
        
        return monitored_file

  

        
        
    
    
    
    
    