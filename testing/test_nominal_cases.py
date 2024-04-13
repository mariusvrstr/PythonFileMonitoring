from src.test_harness.data_snapshot import DataSnapshot
from src.test_harness.current_file_builder import CurrentFileBuilder
from src.test_harness.existing_file_builder import ExistingFileBuilder

def test_addition():
    assert 1 + 1 == 2
    
def _setup_t1_data() -> DataSnapshot:
    snapshot = DataSnapshot()    
    existing_file = snapshot.add_existing_file(ExistingFileBuilder(1, 'cust_001', 'AAAAA'))
    snapshot.add_current_file(CurrentFileBuilder(existing_file).set_file_details(244, 'AAAAB', 'converted.xls'))        
    return snapshot                
    
def test_t1_normal_manual_file_movement():        
    test_data = _setup_t1_data()
    
    assert 0 == 0 
