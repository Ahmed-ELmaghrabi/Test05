import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input,Output,State

BSC = dbc.Row([
    dbc.Row([html.P('BSC-Operations',style={'background-color':'lightpink'})]),
    dbc.Col([
        dbc.Form([
            dbc.Row(
                id='form',
                children=[
                    dbc.Label("Username", className="mr-2", size='md', width='auto'),
                    dbc.Input(id='un',
                              type="text",
                              placeholder="Enter NetAct Username",
                              size='md',
                              className='me-3',
                              style={'width': 'auto', 'display': 'inline'}
                              ),

                    dbc.Label("Password", className="mr-2", size='md', width='auto'),
                    dbc.Input(id='pw',
                              type="password",
                              placeholder="Enter password",
                              size='md',
                              className='me-3',
                              style={'width': 'auto', 'display': 'inline'}
                              ),

                    dbc.Label("IP", className="mr-2", size='md', width='auto'),
                    dbc.Input(id='ip',
                              type="numeric",
                              placeholder="Enter Object's IP",
                              size='md',
                              className='me-3',
                              style={'width': 'auto', 'display': 'inline'}
                              )

                ], style={'display': 'inline'}
            )
        ], style={'margin-top': '0.5rem', 'margin-bottom': '1rem', 'display': 'inline'}),
        dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='BSC-dropdown',
                    options=[
                        {"label": 'OMU Restart', "value": 'OMU Restart'},
                        {"label": 'Switch Over', "value": 'Switch Over'},
                        {"label": 'Backup', "value": 'Backup'},
                        {"label": 'Restore', "value": 'Restore'},
                        {"label": 'Restore', "value": 'Fallback'}
                    ],
                    value="please select an operation",
                )
            ], width={'size': 6, 'offset': 2}),
            dbc.Col()

        ], className='mb-4', style={'margin-top': '8px', 'margin-bottom': '2px'}, justify='right')
    ], width=10),
    dbc.Col([
        dbc.Row([
            dbc.Button("Submit", id='submit-access', color="primary", size='sm', n_clicks=0)
        ], style={'margin-top': '1rem', 'margin-bottom': '1rem'}),
        dbc.Row([
            dbc.Button("Activate", id='submit-operation', color="success", size='sm', n_clicks=0)
        ], style={'margin-top': '1.3rem', 'margin-bottom': '1rem'})

    ], width='auto')
], className='mb-4', style={'margin-top': '4px', 'margin-bottom': '4px'})

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
app.layout =dbc.Container([
    dcc.Location(id='url'),
    dbc.Row([BSC]),
    dbc.Row([html.Div(id='output')])
])


@ app.callback(
     Output('output','children'),
    [Input('url','pathname')],
    [Input('BSC-dropdown','value')]
)
def update(pathname,BSC_op):
    if pathname=='/':
        return BSC_op

if __name__=='__main__':
    app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
