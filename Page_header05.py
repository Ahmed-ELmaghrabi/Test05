import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import base64
# from Index_Page04 import index_page

# ------------------------------------------------------------------------------
# Images
image_filename_Orange = 'Orange_logo.png'                                # replace with your own image
encoded_image_Orange = base64.b64encode(open(image_filename_Orange, 'rb').read())
image_filename_Wallpaper = 'WallpaperDog.png'                           # replace with your own image
encoded_image_Wallpaper = base64.b64encode(open(image_filename_Wallpaper, 'rb').read())
image_filename_Promo = 'Promo.png'                                      # replace with your own image
encoded_image_Promo = base64.b64encode(open(image_filename_Promo, 'rb').read())
image_filename_Logo = 'BFAT_logo.png'                                  # replace with your own image
encoded_image_Logo = base64.b64encode(open(image_filename_Logo, 'rb').read())




header = dbc.Row(
        [
            dbc.Col(
                html.Div(
                    children=[
                        html.Img(src='data:image/png;base64,{}'.format(encoded_image_Orange.decode()),
                                 id='Orange-brand',
                                 style={"height": "50px",
                                        'width': 'auto',
                                        'text-align': 'center',
                                        'margin-left': '15%'}),
                        html.H5('internal use only',
                                style={"margin-top": "0px",
                                       'color': 'white',
                                       'margin-left': '1%',
                                       'fontFamily': 'Agency FB',
                                       'width': '150px',
                                       'fontSize': '5',
                                       'textAlign': 'left'})],
                    style={'width': 'auto', 'display': 'inline-block', 'margin-top': '5px'}
                ),
                style={
                    'width': '120px',
                    'margin-left': '1px',
                    'display': 'inline-block',
                    'background-color': 'black'
                }
            ),
            dbc.Col(
                html.Div([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_Logo.decode()),
                             style={'position': 'relative',
                                    'margin-left': 'auto',
                                    'margin-right': 'auto',
                                    'display': 'inline',
                                    'height': '100px',
                                    'width': 'auto',
                                    'color': 'black',
                                    'margin-bottom': '0px'
                                    }),
                    # html.H5('Cairo Lab -Orange Operational Skill Center (OSC)',
                    #         style={'margin-top': '0px',
                    #                'fontSize': '8',
                    #                'color': 'white',
                    #                'margin-left': 'auto',
                    #                'margin-right': 'auto',
                    #                'fontFamily': 'Calibri',
                    #                'textAlign': 'Center'})
                ],
                    id='header',
                    className='row flex-display',
                    style={'width': '550px',
                           'float': 'right',
                           'display': 'inline-block',
                           'margin-right': '12px',
                           'margin-bottom': '1px',
                           'background-color': 'black'
                           })
            ),
            dbc.Col(
                [
                    html.Div([]),
                    dbc.Badge(
                        "github",
                        href="www.google.com",
                        color="black",
                        style={
                            "color": "white",
                            'background-color': 'black',
                            "margin-top": 5,
                            # "margin-right": 10,
                            "font-size": 15,
                            "border": "solid 1px silver",
                            "float": "right",
                        },
                    ),
                    dbc.Badge(
                        "plazza",
                        href="https://plazza.orange.com/get-started",
                        color="black",
                        style={
                            "color": "white",
                            'background-color': 'black',
                            "margin-top": 5,
                            "margin-right": '1rem',
                            "font-size": 15,
                            "border": "solid 1px silver",
                            "float": "right",
                        },
                    ),
                    html.Div(
                        dbc.Button('Log out',
                                   href='/',
                                   id='logout',
                                   n_clicks=0,
                                   size='sm',
                                   external_link=True,
                                   style={'color': '#bed4c4',
                                          'background-color':'black',
                                        'font-family': 'serif',
                                        # 'font-weight': 'bold',
                                        "text-decoration": "none",
                                          'text-align':'center'
                                        # 'font-size': '20px'
                                        }),
                        style={'padding-left': '70%',
                               'margin-top': '1rem',
                               'display': 'inline-block',
                               'text-align':'center'
                               })
                ],
                style={'background-color': 'black'
                       }
            ),
        ],
        style={'background-color': 'black',
               'margin-bottom': '5px',
               # 'width':'100%'
               })



