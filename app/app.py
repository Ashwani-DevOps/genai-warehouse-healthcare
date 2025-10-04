from flask import Flask
from src.validate_inventory import validate_inventory
from src.forecast_demand import forecast_demand
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "GenAI Warehouse System is Running"

@app.route('/validate')
def validate():
    issues, expired = validate_inventory('data/inventory.csv')
    return f"Issues: {len(issues)}, Expired: {len(expired)}"

@app.route('/forecast')
def forecast():
    forecast = forecast_demand('data/demand.csv')
    return forecast.to_html()

if __name__ == '__main__':
    app.run(debug=True)