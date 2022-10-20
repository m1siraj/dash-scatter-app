from dash import dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
# print(df.head(5))

fig = px.line(df, x="life expectancy", y="gdp per capita"
                 , color="continent", hover_name="country")

fig.update_layout(plot_bgcolor = "#33262F",
                  title = {'x':0.5}, 
                  font = {"family" : "sans serif"})

app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='life-exp-vs-gdp', figure=fig), md=6),
                dbc.Col(dcc.Graph(id='life-exp-vs-gdp-2', figure=fig), md=6)
            ]
        ), 
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='life-exp-vs-gdp-3', figure=fig), width=6),
                dbc.Col(dcc.Graph(id='life-exp-vs-gdp-4', figure=fig), width=6)
            ]
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
