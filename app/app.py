import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.forecast_demand import forecast_demand
from src.validate_inventory import validate_inventory
from src.notify import send_email_alert

from flask import Flask, jsonify
import pandas as pd
from src.forecast_demand import forecast_demand, plot_forecast

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>✅ GenAI Warehouse Healthcheck System</h1>
    <ul>
        <li><a href="/validate">Inventory Validation</a></li>
        <li><a href="/forecast">Forecast Table</a></li>
        <li><a href="/forecast-plot">Forecast Plot</a></li>
        <li><a href="/alert">Send Alert</a></li>
    </ul>
    """


@app.route("/validate")
def validate():
    issues, expired = validate_inventory("data/inventory.csv")
    return f"Issues: {len(issues)}, Expired: {len(expired)}"


@app.route("/forecast")
def forecast():
    forecast = forecast_demand("data/demand.csv")
    return forecast.to_html()


@app.route("/alert")
def alert():
    issues, expired = validate_inventory("data/inventory.csv")
    if not issues.empty or not expired.empty:
        body = f"Shortages:\n{issues.to_string()}\n\nExpired:\n{expired.to_string()}"
        send_email_alert("Warehouse Alert", body, "ashu_07@hotmail.com")
        return "Alert sent!"
    return "No issues found."


@app.route("/forecast-plot")
def forecast_plot():
    forecast = forecast_demand("data/demand.csv")
    return plot_forecast(forecast)


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
