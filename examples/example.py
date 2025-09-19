import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    assets_folder="../themes",
)

app.layout = html.Div(children=[
    html.H1(children='Hello World'),
    html.Div(children='This is a simple Dash app.')
])


if __name__ == '__main__':
    app.run(debug=True)
