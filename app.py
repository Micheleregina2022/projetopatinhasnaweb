import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px


df = pd.read_csv('planilhaDoFormulário.csv')


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1('Meu Dashboard'),
    dcc.Graph(
        id='exemplo-grafico',
        figure=px.bar(df, x='coluna1', y='coluna2')
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
