import pandas as pd

def validate_inventory(file_path):
    df = pd.read_csv(file_path)
    issues = df[df['quantity'] < 0]
    expired = df[df['expiry_date'] < pd.Timestamp.today()]
    return issues, expired