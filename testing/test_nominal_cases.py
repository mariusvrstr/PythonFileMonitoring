from typing import List

from src.contracts.source import Source
from src.contracts.stages import Stage
from src.contracts.current_file import CurrentFile
from src.contracts.existing_file import ExistingFile
from src.test_harness.current_file_builder import CurrentFileBuilder
from src.test_harness.existing_file_builder import ExistingFileBuilder
from src.file_processor import FileProcessor
from src.data_access.file_repo import FileRepo
from src.contracts.action import Action

def test_addition():
    assert 1 + 1 == 2
    
def _init_file_processor(existing_files:List[ExistingFile]) -> FileProcessor:
    repo = FileRepo(existing_files=existing_files)
    file_processor = FileProcessor(repo)    
    return file_processor

def test_file_in_progress_no_changes():   
    # Setup
    file_builder = ExistingFileBuilder(1, 'cust_001', 'AAAAA')
    file_processor = _init_file_processor([file_builder.build()])
    current_file = CurrentFileBuilder(file_builder).build()
    
    action = file_processor.process_file(current_file)
    
    assert action == Action.NoAction
    
def test_add_new_file_from_client():   
    # Setup
    file_builder = ExistingFileBuilder(1, 'cust_001', 'AAAAA')
    file_processor = _init_file_processor([])
    current_file = CurrentFileBuilder(file_builder).build()
    
    action = file_processor.process_file(current_file)
   
    assert action == Action.Added
    
def test_manual_move_to_in_progress():   
    # Setup
    file_builder = ExistingFileBuilder(1, 'cust_001', 'AAAAA')
    file_processor = _init_file_processor([file_builder.build()])
    current_file = CurrentFileBuilder(file_builder).set_file_step(Stage.InProgress, Source.Manual).build()
    
    action = file_processor.process_file(current_file)
    
    assert action == Action.Updated

def test_manual_move_to_etl():   
    # Setup
    file_builder = ExistingFileBuilder(1, 'cust_001', 'AAAAA').set_file_step(Stage.InProgress, Source.Manual)
    file_processor = _init_file_processor([file_builder.build()])
    current_file = CurrentFileBuilder(file_builder).set_file_step(Stage.Ready, Source.ETL).set_file_details(324,'AAAAB', 'converted.xls').build()
    
    action = file_processor.process_file(current_file)
    
    assert action == Action.Updated
    
    
def test_manual_move_etl_to_archive():   
    # Setup
    file_builder = ExistingFileBuilder(1, 'cust_001', 'AAAAB').set_file_step(Stage.Ready, Source.ETL)
    file_processor = _init_file_processor([file_builder.build()])
    current_file = CurrentFileBuilder(file_builder).set_file_step(Stage.Archived, Source.ETL).build()
    
    action = file_processor.process_file(current_file)
    
    # Need to include check to make sure the correct item was updated
    assert action == Action.Updated
    
    
