import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

external_stylesheets = [dbc.themes.DARKLY]
app = dash.Dash(__name__, title='Interactive Model Dashboard', external_stylesheets=[external_stylesheets])

df = pd.read_csv('/Users/dingma/Documents/GitHub/Personal-Projects/Interactive-ML-Dashboard/Dataset/customer_dataset.csv')

features = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicatessen']
models = ['PCA', 'UMAP', 'AE', 'VAE']
df_average = df[features].mean()
max_val = df[features].max().max()

app.layout = html.Div([
    html.Div([

        html.Div([

            html.Div([
                html.Label('Model selection'), ], style={'font-size': '18px'}),

            dcc.Dropdown(
                id='crossfilter-model',
                options=[
                    {'label': 'Principle Component Analysis', 'value': 'PCS'},
                    {'label': 'Unniform Manifold Approximation and Projection', 'value': 'UMAP'},
                    {'label': 'Autoencoder', 'value': 'AE'},
                    {'label': 'Variational Autoencoder', 'value': 'VAE'},
                ],
                value = 'PCA',
                clearable= False

            )], style={'width': '49%', 'display': 'inline-block'}
        ),

        html.Div([

            html.Div([
                html.Label('Feature selection'), ],
                style={'font-size': '18px', 'width': '40%', 'display': 'inline-block'}),

            html.Div([
                dcc.RadioItems(
                    id='gradient-scheme',
                    options=[
                        {'lable': 'Orange to Red', 'value': 'OrRd'},
                        {'lable': 'Viridis', 'value': 'Viridis'},
                        {'lable': 'Plasma', 'value': 'Plasma'},

                    ],
                    value='Plasma',
                    labelStyle={'float': 'right', 'display': 'inline-block', 'margin-right': 10}
                ),
            ], style={'width': '49%', 'display': 'inline-block', 'float': 'right'}),

            dcc.Dropdown(
                id='crossfilter-feature',
                options=  [{'label': i , 'value': i} for i in features + ['None', 'Region', 'Channel','Total_Spend']],
                value = 'None',
                clearable = False
)], style = {'width': '49%', 'float': 'right', 'display': 'inline-block'}

)], style = {'backgroundColor': 'rgb(17, 17, 17)', 'padding': '10px 5px'}
),

html.Div([

    dcc.Graph(
        id = 'Scatter-Plot',
        hoverData = {'points': [{'customdata': 0}]}
)

], style = {'width': '100%', 'height': '90%', 'display': 'inline-block', 'padding': '0 20'}),

html.Div([
    dcc.Graph(id='point-plot'),
], style={'display': 'inline-block', 'width': '100%'}),

], style={'backgroundColor': 'rgb(17, 17, 17)'},
)

@app.callback(
    dash.dependencies.Output('scatter-plot','figure'),[dash.dependencies.Input('crossfilter-feature','value'),
                                                       dash.dependencies.Input('crossfilter-model','value'),
                                                       dash.dependencies.Input('gradient-scheme','value')]
)
def update_graph(feature, model, gradient):
    return None


def create_point_plot(df, title):
    return None


@app.callback(
    ###
)
def update_point_plot(hoverData):
    return None


if __name__ == '__main__':
    app.run_server(debug=True)
