
from src.contracts.current_file import CurrentFile
from src.data_access.file_repo import FileRepo
from src.contracts.action import Action

class FileProcessor:    
    file_repo:FileRepo = None

    # In the real solution the existing files must be access through DB repo
    def __init__(self, file_repo:FileRepo) -> None:
        self.file_repo = file_repo
    
    def process_file(self, file:CurrentFile) -> Action:
        
        existing_file = self.file_repo.get_existing_file(file.stage, file.source, file.filename, file.file_hash)
        
        if existing_file != None:
            was_updated = self.file_repo.update_file(file, existing_file)
            return Action.Updated if was_updated else Action.NoAction
        
        self.file_repo.add_file(file)
        return Action.Added
        
    
    