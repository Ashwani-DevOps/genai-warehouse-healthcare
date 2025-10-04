from prophet import Prophet
import pandas as pd
import plotly.graph_objects as go

def forecast_demand(file_path):
    df = pd.read_csv(file_path)
    df = df.rename(columns={'date': 'ds', 'demand': 'y'})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

def plot_forecast(forecast_df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast_df['ds'], y=forecast_df['yhat'], name='Forecast'))
    fig.add_trace(go.Scatter(x=forecast_df['ds'], y=forecast_df['yhat_upper'], name='Upper Bound', line=dict(dash='dot')))
    fig.add_trace(go.Scatter(x=forecast_df['ds'], y=forecast_df['yhat_lower'], name='Lower Bound', line=dict(dash='dot')))
    fig.update_layout(title='Demand Forecast', xaxis_title='Date', yaxis_title='Demand')
    return fig.to_html(full_html=False)