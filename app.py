
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url'),
    dbc.NavbarSimple(brand="Forex Analyzer", brand_href="/", color="dark", dark=True),
    dash.page_container
])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

