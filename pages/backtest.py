
from dash import html, register_page
register_page(__name__, path="/backtest", name="Backtest")

layout = html.Div([
    html.H3("Backtest Visuel"),
    html.P("Simulation avec stratégie MACD et Risk/Reward.")
])
