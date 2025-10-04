from src.validate_inventory import validate_inventory
from src.forecast_demand import forecast_demand

issues, expired = validate_inventory('data/inventory.csv')
print("Shortages:\n", issues)
print("Expired Items:\n", expired)

forecast = forecast_demand('data/demand.csv')
print(forecast.tail())