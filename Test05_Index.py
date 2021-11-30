import dash
import base64
# from dash import callback_context
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import numpy as np
import pandas as pd
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from Test05_App import app
from Page_header05 import header
from Base_Module import SHELL, start, get_ftp, send_ftp, client
from template_05 import template_1, template_2
# from threading import Thread

layout_style = {"background-color": "grey82"}
options = []
image_filename_Intro = 'Intro.PNG'
encoded_image_Intro = base64.b64encode(open(image_filename_Intro, 'rb').read())


SIDEBAR_STYLE = {
    # "position": "fixed",
    # "top": 170,
    # "left": 10,
    # "bottom": 10,
    # "width": "16rem",
    # "height": "100%",
    "z-index": 1,
    # "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    'font-weight': 'bold',
    "background-color": "dark",
    'color': 'lightgrey',
    'height': '25.1rem',
    'mrgin-left': '3px'
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    # "top": 62.5,
    # "left": "-16rem",
    # "bottom": 0,
    # "width": "16rem",
    # "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
    'color': 'grey'

}

CONTENT_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "2rem 1rem",
    # "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = dbc.Col(id="page-content", children=[])

sidebar = html.Div(
    [
        # html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "operation Level",
            className="lead",
            style={
                'background-color': 'lightgrey',
                'font-family': 'Calibri',
                'font-weight': 'bold',
                'text-align': 'center'
            }
        ),
        dbc.Nav([
                # dbc.NavLink(
                #     [html.I(className="fas fa-home me-2"), html.Span("Home")],
                #     href="/",
                #     active="exact",
                #     style={
                #         # 'background-color':'lightcyan'
                #     }
                # ),
                # dbc.NavLink("Home", href="/", id="page-0-link",active='exact'),
                dbc.NavLink("RNC", href="/", id="page-1-link", active='exact',external_link=False),
                dbc.NavLink("BSC", href="/page-2", id="page-2-link", active='exact',external_link=False),
                dbc.NavLink("Log History", href="/page-3", id="page-3-link", active='exact')],
            style=SIDEBAR_STYLE,
            vertical=True,
            pills=True,
            className='sidebar'
        ),
    ],
    id="sidebar",
    style={
        'background-color': 'lightgrey',
        'margin-left': '5px'
         # 'border':'1px outset ',
         # 'margin-left':'1px'
    }
)

global Controller

class Controller:

    def __init__(self, name):
        self.name = name

    def get_controller(self, name, color, usecases):
        return dbc.Row([
            dbc.Row([html.P(f'{name} Regression',
                            style={'background-color': f'{color}',
                                   'font-weight': 'bold',
                                   })]),
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
                    dbc.Row([
                        dcc.Dropdown(
                            id='dropdown',
                            options=usecases,
                            value="please select an operation",
                            style={
                                'color': 'primary',
                                # 'background-color':'silver',
                                'size': '27rem',
                                'margin-left': 'auto',
                                'margin-right': 'auto',
                                'width': '27.7rem',
                            }

                        ),
                        html.Div(
                            id='extra-inputs', children=[],
                            style={
                                # 'display':'inline',
                                'margin-top': '1px',
                                'margin-bottom': '1px',
                                'text-align': 'center'}
                        ), ],
                        justify='left', align='center'),
                    dbc.Row([
                        dbc.Col([
                            html.Div(id='description', children=[],
                                     style={
                                         # 'display':'inline-block',
                                         'margin-top': '1px',
                                         'margin-bottom': '1px',
                                     }
                                     ),

                        ], width={'size': 4, }),
                        dbc.Col([
                            html.Div(id='result', children=[],
                                     hidden=False,
                                     style={
                                         # 'display':'inline-block',
                                         'margin-top': '1px',
                                         'margin-bottom': '1px',
                                         'text-align': 'center'
                                     }
                                     ),
                            html.Div(id='result-extended', children=[],
                                     hidden=False,
                                     style={
                                         # 'display':'inline-block',
                                         'margin-top': '1px',
                                         'margin-bottom': '1px',
                                         'text-align': 'center'
                                     }
                                     ),
                        ],
                            width={'size': 4, 'offset': 3})
                    ]
                        , justify='right', align='center'
                    ),

                ], className='mb-4',
                    style={
                        'margin-top': '15px',
                        'margin-bottom': '2px'
                    }, )
            ], width=10),
            dbc.Col([
                dbc.Row([
                    dbc.Button("Submit", id='submit-access', color="dark", size='sm', n_clicks=0)
                ], style={'margin-top': '1rem', 'margin-bottom': '1rem'}),
                dbc.Row([
                    # dbc.Button("Activate", id='submit-operation', color="success", size='sm', n_clicks=0)
                ], style={'margin-top': '1.3rem', 'margin-bottom': '1rem'})

            ], width='auto')
        ], className='mb-4', style={'margin-top': '4px', 'margin-bottom': '4px'})

    def usecase_description(self, text, button, color):
        card_content = [
            dbc.CardHeader("Test Description", style={
                                              # 'color': 'white',
                                              'text-align': 'center',
                                              'font-weight': 'bold'}),
            dbc.CardBody([
                html.Div(
                    children=[text],
                    className="card-text",
                    style={'width': '27rem',
                           'margin-top': '2px',
                           'margin-bottom': '1rem',
                           'margin-left': 'auto',
                           'margin-right': 'auto',
                           'text-align': 'left'
                           }
                ),
            dbc.Button(f"{button}",
                       id='submit-operation',
                       color=f"{color}",
                       size='sm',
                       n_clicks=0,
                       style={
                           'margin-right':'auto',
                           'margin-left':'auto'
                           })],
                style={'text-align':'center'})]
        return card_content

    def case_input_model_2(self):
        input_card = html.Div([
                dbc.Row([
                    # input one
                    html.P("Iterations",
                           style={'width': 'auto',
                                  'display': 'inline',
                                  'margin-right': '3px'
                                  }),
                    dbc.Input(type="number",
                              placeholder="test to be repeated",
                              size='md',
                              value=1,
                              className='me-3',
                              style={'width': 'auto',
                                     'display': 'inline',
                                     'background-color': 'whitesmoke',
                                     'text-align': 'center'
                                     },
                              id='case-input-0',
                              min=0, max=10, step=1),
                        dcc.Dropdown(id='switch-over',
                                     placeholder="please select a BTS",
                                     options=[{'label': i, 'value': i} for i in options],
                                     style={
                                         'color': 'primary',
                                         'width': '15rem',
                                         # 'display':f'{input1}'
                                     }
                                     )],
                    justify='center',
                    align='center'
                )
                ,
            ],
                id="styled-numeric-input",
            )
        return input_card

    def case_input_model_1(self):
        input_card = html.Div([
                dbc.Row([
                    # input one
                    html.P("Iterations",
                           style={'width': 'auto',
                                  'display': 'inline',
                                  'margin-right': '3px'
                                  }),
                    dbc.Input(type="number",
                              placeholder="test to be repeated",
                              size='md',
                              value=0,
                              className='me-3',
                              style={'width': 'auto',
                                     'display': 'inline',
                                     'background-color': 'whitesmoke',
                                     'text-align': 'center'
                                     },
                              id='case-input-0',
                              min=0, max=10, step=1),
                        ],
                    justify='center',
                    align='center'
                )
                ,
            ],
                id="styled-numeric-input",
            )
        return input_card


# class Log_history:
#     def __init__(self):
#         pass

Log_history = None

class Feedback:
    def __init__(self, content):
        self.content = content

    def feedback(self, content):
        return html.Div(dbc.Fade(
            dbc.Card(content, color='dark', outline=True, style={
                'width': '30rem',
                'margin-top': '2px',
                'margin-bottom': '4px'
            }),
            id='fade',
            is_in=True,
            appear=False),
            # persistence=True, persistence_type="local",
        )



controls1 = dbc.Form([],style={"inline-block": True})

controls2_a = dbc.Form([], style = {"inline-block": True})

controls2_b = dbc.Form([

    ])

controls3_a = dbc.Form([
        dbc.Form([]),
        dbc.Form([]),
    ])

controls3_b = dbc.Form([])

controls4 = dbc.Form([
        dbc.Form([]),
        html.Hr(),
        dbc.Form([]),
        html.Hr(),
        dbc.Form([]),
    ])

tab0_content =dbc.Card([
        dbc.Row([
                html.Img(src='data:image/png;base64,{}'.format(encoded_image_Intro.decode()),
                         id='Intro-image',
                         style={
                            'width':'50rem',
                            'height':'29.5rem'
                                }
                         )
        ],
            className='mb-4',
            justify='center',
            align='center',
            style={
                'margin-top':'4px',
                'margin-bottom':'4px'
            }),  ## Row_1
    ],
    color='white',
    style={
        'height':'30rem',
        'background-color':'white'
    }
)

tab1_content = dbc.Card([
        dbc.Row([
            dbc.Col([
                # dbc.Card([dbc.CardBody([
                #
                # ])
                # ])
                dcc.Location(id='url'),
                sidebar
            ],
                width=2),    # Sidebar
            content
        ],
            className='mb-4',
            style={
                'margin-top':'4px',
                'margin-bottom':'4px'
            }),  ## Row_1
    dbc.Row([
        html.Div(id='output', style={'text-align': 'center'}),
        html.Div(id='output1', style={'text-align': 'center'},hidden=True)
    ],
        justify='center', align='center')


    ],
    color='whitesmoke',
    style={
        'height':'30rem',
        'background-color':'whitesmoke'
    }
)

tab2_content = dbc.Card(dbc.CardBody([
            dbc.Row(

            ),

        ]))

tab3_content = dbc.Card(dbc.CardBody([dbc.Row()]))

tab4_content = dbc.Card(dbc.CardBody([
            dbc.Row(

            ),
            html.Hr(),
            dbc.Row(

            ),
            dbc.Row(

            ),
            html.Hr(),
            dbc.Row(

            ),
        ]))

app.layout = dbc.Container(
    [
        header,
        dbc.Tabs(
            [
                dbc.Tab(tab0_content,label='Home',
                        tab_style={'background-color':'silver',
                                   'color':'grey',
                                   'font-weight':'bold',
                                   'margin':'0px 4px',
                                   'border-radius':'3px 3px 0px 0px',
                                   'box-shadow': '0 0.5rem 0.8rem #00000080'
                                   },
                        ),
                dbc.Tab(tab1_content, label="Controllers",
                        tab_style={'background-color':'silver',
                                   'color':'grey',
                                   'margin':'0px 4px',
                                   'font-weight':'bold',
                                   'border-radius':'3px 3px 0px 0px',
                                   'box-shadow': '0 0.5rem 0.8rem #00000080'
                                   },
                        # label_style={'color':'white'}
                        ),
                dbc.Tab(tab2_content, label="SRAN",
                        tab_style={
                                   'background-color':'Silver',
                                   'color':'grey',
                                   'font-weight':'bold',
                                   'margin':'0px 4px',
                                   'border-radius':'3px 3px 0px 0px',
                                   'box-shadow': '0 0.5rem 0.8rem #00000080'
                                   },
                        # label_style={'color':'white'}
                        ),
                dbc.Tab(tab3_content, label="SRAT",
                        tab_style={
                                   'background-color':'silver',
                                   'color':'grey',
                                   'font-weight':'bold',
                                   'margin':'0px 4px',
                                   'border-radius':'3px 3px 0px 0px',
                                   'box-shadow': '0 0.5rem 0.8rem #00000080'
                                   },
                        label_style={'active-color':'black'}
                        ),
                dbc.Tab(tab4_content, label="KPIs' Analysis",
                        tab_style={
                                'background-color':'silver',
                                   'color':'grey',
                                   'font-weight':'bold',
                                   'margin':'0px 4px',
                                   'border-radius':'3px 3px 0px 0px',
                                   'box-shadow': '0 0.5rem 0.8rem #00000080'
                                   },
                        # label_style={'color':'white'}
                        ),
            ]
        ),
    ],

    fluid=True,
    style={
        'width':'100%',
        'height':'100vh',
        'background-color':'lightcyan',

    },
)


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    global MO
    # if pathname == '/':
    #     return dbc.Row([
    #         html.P('Please select a controller')
    #     ],justify='center',align='center')
    if pathname == "/":
        MO = Controller(name='RNC')
        Test_list = [{"label": 'Test_1', "value": 'Test_1'},
                     {"label": 'Test_2', "value": 'Test_2'},
                     {"label": 'Test_3', "value": 'Test_3'},
                     {"label": 'Test_4', "value": 'Test_4'},
                     {"label": 'Test_5', "value": 'Test_5'}]
        return MO.get_controller(name='RNC',color='navajowhite',usecases=Test_list)
    elif pathname == "/page-2":
        MO = Controller(name='BSC')
        Test_list = [{"label": 'OMU Restart', "value": 'OMU Restart'},
                     {"label": 'Switch Over', "value": 'Switch Over'},
                     {"label": 'Backup', "value": 'Backup'},
                     {"label": 'BCXU Switchover', "value": 'BCXU Switchover'},
                     {"label": 'Restore', "value": 'Fallback'}]
        return MO.get_controller(name='BSC',color='lightpink',usecases=Test_list)
    elif pathname == "/page-3":
        return [Log_history]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
# Callback function decorator corresponding to app instance


@ app.callback(
        Output('description','children'),
        Output('extra-inputs','children'),
    [
        Input('url', 'pathname'),
        Input('dropdown','value'),
        Input('submit-access', 'n_clicks'),
        # Input('switch-over','value')
     ],

)
def update_inputs(pathname,selected,button):
    Feedback= html.Div()
    inpt = html.Div()
    if pathname=='/':
        if button == 0:
            return html.P('Please submit Managed Object Credentials at first',
                          style={'text-align':'center',
                                 'width':'60rem',
                                 'font-weight':'bold',
                                 'margin-top':'1rem'
                                 }
                          ), None
        else:
            return selected , None
    elif pathname== '/page-2':
        if button == 0:
            return html.P('Please submit Managed Object Credentials at first',
                          style={'text-align':'center',
                                 'width':'60rem',
                                 'font-weight':'bold',
                                 'margin-top':'1rem'
                                 }
                          ), None
        else:
            if selected == 'BCXU Switchover':
                text=html.Div([
                                html.P('1) Please Select number of iterations'),
                                html.P('2) Update to get a list of the selected inputs')])
                inpt = MO.case_input_model_2()
                Feedback = html.Div(
                    dbc.Fade(
                        dbc.Card(MO.usecase_description(text,'UPDATE','dark'),
                                 color='dark',
                                 outline=True,
                                 style={
                                     'width': '30rem',
                                     'margin-top': '2px',
                                     'margin-bottom': '4px'
                                 }),
                        id='fade',
                        is_in=True,
                        appear=False)
                )
                return Feedback, inpt
            if selected == 'OMU Restart':
                text = html.Div([
                                 html.P('1) Submit BSC\'s username, password and IP'),
                                 html.P('2) Activate')])
                inpt = MO.case_input_model_1()
                Feedback = html.Div(
                        dbc.Fade(
                        dbc.Card(MO.usecase_description(text,'Activate','dark'),
                            color='dark',
                            outline=True,
                            style={
                                'width':'30rem',
                                'margin-top':'2px',
                                'margin-bottom':'4px'
                                   }),
                            id='fade',
                            is_in=True,
                            appear=False)
                        )
                return Feedback, inpt
            else:
                return [],[]





@ app.callback(
    Output('output1', 'children'),
    [
     Input('submit-access','n_clicks'),
     Input('un', 'value'),
     Input('pw', 'value'),
     Input('ip', 'value')
     ]
)
def input_to_output(n_clicks,username, password, IP):
    '''
    Simple callback function
    '''
    NA_IP ='10.58.93.157'
    NA_un = 'root'
    NA_pw = 'arthur'
    global session
    global sftp
    session, sftp = start(NA_un,NA_pw,NA_IP)
    print(client.get_transport().is_active())
    ssh_cmd = client.invoke_shell()

    if n_clicks is None:
        raise PreventUpdate
    else:
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
        if 'submit-access' in changed_id:
            df_un = pd.Series(username)
            arr_un = df_un.to_numpy()
            np.savetxt('username.txt',arr_un,fmt='%s')
            df_pw = pd.Series(password)
            arr_pw = df_pw.to_numpy()
            np.savetxt('password.txt', arr_pw, fmt='%s')
            df_ip = pd.Series(IP)
            arr_ip = df_ip.to_numpy()
            np.savetxt('ipaddress.txt', arr_ip, fmt='%s')

            # return session, sftp



if __name__=='__main__':
    app.run_server(debug=False)




