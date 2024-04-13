from src.contracts.source import Source
from src.contracts.stages import Stage
from src.contracts.current_file import CurrentFile
# from src.test_harness.current_file_builder import CurrentFileBuilder
from src.test_harness.existing_file_builder import ExistingFileBuilder

from datetime import datetime

class CurrentFileBuilder():
    
    filename:str = None
    source:Source = None
    stage:Stage = None
    client_account:str = None
    folder:str = None
    size_in_bytes:int = None
    created_date:datetime = None
    file_hash:str = None                
    
    def __init__(self, existing_file_builder:ExistingFileBuilder) -> None:

        self.source = Source.Manual
        self.stage = Stage.Ready
        self.filename = existing_file_builder.filename
        self.client_account = existing_file_builder.client_account
        self.folder = f'{existing_file_builder.client_account}/{self.stage}'
        self.size_in_bytes = existing_file_builder.size_in_bytes
        self.created_date = existing_file_builder.created_date
        self.file_hash = existing_file_builder.file_hash    
    
    def set_file_details(self, size_in_bytes:int, file_hash:str, filename:str = None):
        self.size_in_bytes = size_in_bytes
        self.file_hash = file_hash
        
        if (filename != None):
            self.filename = filename        
        
        return self   
    
    def set_file_step(self, stage:Stage, source:Source):
        self.stage = stage
        self.source = source        
        return self    
    
    def build(self) -> CurrentFile:
        return CurrentFile.Create(filename=self.filename, source=self.source, stage=self.stage, client_account=self.client_account, 
                folder=self.folder, size_in_bytes=self.size_in_bytes, created_date=self.created_date, file_hash=self.file_hash)
        
