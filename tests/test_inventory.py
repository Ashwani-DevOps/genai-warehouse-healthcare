import pandas as pd
from src.validate_inventory import validate_inventory

def test_validate_inventory():
    issues, expired = validate_inventory('data/inventory.csv')
    assert isinstance(issues, pd.DataFrame)
    assert isinstance(expired, pd.DataFrame)