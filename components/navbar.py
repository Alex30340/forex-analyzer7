
from dash import html, dcc

def Navbar():
    return html.Nav([
        dcc.Link("Accueil", href="/"),
        dcc.Link("Analyse", href="/analyse"),
        dcc.Link("Dashboard", href="/dashboard"),
        dcc.Link("Backtest", href="/backtest"),
        dcc.Link("Éducation", href="/education"),
        dcc.Link("LAB", href="/lab")
    ])
