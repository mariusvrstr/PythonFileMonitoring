from typing import List
from src.contracts.existing_file import ExistingFile
from src.contracts.current_file import CurrentFile
from src.contracts.source import Source
from src.contracts.stages import Stage
from datetime import datetime

class FileRepo:
    
    existing_files:List[ExistingFile] = None
    
    def __init__(self, existing_files:List[ExistingFile]) -> None:
        self.existing_files = existing_files
        
        
    def get_existing_file(self, stage:Stage, source:Source, file_name:str, file_hash:str) -> ExistingFile:
        
        if source == Source.Manual: # Match by name
            found = [file for file in self.existing_files if file.filename == file_name]
            return found[0] if len(found) > 0 else None
        
        
    def add_file(self, new_file:CurrentFile):
        converted_file = ExistingFile.Create(new_file.filename, new_file.source, new_file.stage, new_file.client_account, new_file.folder,
                                new_file.size_in_bytes, new_file.created_date, new_file.file_hash, 1, datetime.utcnow(), None, datetime.utcnow())

        self.existing_files.append(converted_file)
        
    def update_file(self, current_file:CurrentFile, existing_file:ExistingFile) -> bool:
        has_changed = False
        
        if existing_file.filename != current_file.filename:
            existing_file.filename = current_file.filename
            has_changed = True
        
        if existing_file.file_hash != current_file.file_hash:
            existing_file.file_hash = current_file.file_hash
            has_changed = True
            
        if existing_file.source != current_file.source:
            existing_file.source = current_file.source
            has_changed = True
            
        if existing_file.stage != current_file.stage:
            existing_file.stage = current_file.stage
            has_changed = True            
        
        if has_changed:
            existing_file.last_change_date = datetime.utcnow()
            existing_file.number_of_changes += 1
        
        return has_changed
        
        
        
        
        
        
        

        
    