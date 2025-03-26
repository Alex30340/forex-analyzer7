
from dash import html, register_page
register_page(__name__, path="/lab", name="LAB")

layout = html.Div([
    html.H3("LAB Technique"),
    html.P("Espace pour tester des modules expérimentaux.")
])
