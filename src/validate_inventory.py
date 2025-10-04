import pandas as pd


def validate_inventory(file_path):
    df = pd.read_csv(file_path)

    # Convert expiry_date to datetime
    df['expiry_date'] = pd.to_datetime(df['expiry_date'], errors='coerce')

    issues = df[df['quantity'] < 0]
    expired = df[df['expiry_date'] < pd.Timestamp.today()]

    return issues, expired