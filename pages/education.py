
from dash import html, register_page
register_page(__name__, path="/education", name="Éducation")

layout = html.Div([
    html.H3("Page éducative"),
    html.P("Explication des patterns : Doji, Engulfing, etc.")
])
