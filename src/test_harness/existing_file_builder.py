from src.contracts.source import Source
from src.contracts.stages import Stage

from src.contracts.existing_file import ExistingFile
# from src.test_harness.existing_file_builder import ExistingFileBuilder

from datetime import datetime, timedelta

class ExistingFileBuilder():
    
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
    
    def __init__(self, seed:int, client_account:str, file_hash:str, from_date:datetime = datetime.utcnow()) -> None:

        self.source = Source.Manual
        self.stage = Stage.Ready
        self.filename = f'filename_{seed}.xls'
        self.client_account = client_account
        self.folder = f'{client_account}/{self.stage}'
        self.size_in_bytes = seed * 100
        self.created_date = from_date - timedelta(days=5)
        self.file_hash = file_hash    
        self.number_of_changes = 1
        self.last_change_date = from_date
        self.from_date = from_date
        self.to_date = None
    
    
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
    
    def build(self) -> ExistingFile:
        return ExistingFile.Create(filename=self.filename, source=self.source, stage=self.stage, client_account=self.client_account, 
                                  folder=self.folder, size_in_bytes=self.size_in_bytes, created_date=self.created_date, file_hash=self.file_hash,
                                  number_of_changes=self.number_of_changes, from_date=self.from_date, to_date=self.to_date, last_change_date=self.last_change_date)
        
        
    
    
    
    
    