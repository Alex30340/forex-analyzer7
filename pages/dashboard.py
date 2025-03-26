
from dash import html, register_page
register_page(__name__, path="/dashboard", name="Dashboard")

layout = html.Div([
    html.H3("Dashboard du Portefeuille"),
    html.P("Graphique de capital, PnL, export CSV.")
])
