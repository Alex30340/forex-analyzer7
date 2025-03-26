
from dash import html, register_page
register_page(__name__, path="/analyse", name="Analyse")

layout = html.Div([
    html.H3("Analyse Technique"),
    html.P("Indicateurs, patterns, bougies, TP/SL, etc.")
])
