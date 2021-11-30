import dash
from Test05_App import app
import time
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from Base_Module import SHELL,start,get_ftp, send_ftp
from dash.dependencies import Input,Output,State
from dash.exceptions import PreventUpdate
from Operations.BSC_Regression.omu_restart import omurestart
from Operations.BSC_Regression.bcxu_swo import bcxuswo, extended_bcxuswo
from Operations.BSC_Regression.Case_Result import usecase_output
import numpy as np
import pandas as pd
from six.moves.urllib.parse import quote


# function that will control the process of execution
@app.callback(
    Output('result', 'children'),
    [Input('submit-operation', 'n_clicks'),
     Input('dropdown','value'),
     Input('case-input-0','value'),
     ]
)
def template_1(n_clicks,Selected_test,var):   # this function will be altered per user case name and returned to main app
    Feedback = html.Div([])
    if n_clicks is None:
         raise PreventUpdate
    else:
         changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
         if 'submit-operation' in changed_id:
             if n_clicks > 0:
                 if Selected_test == 'OMU Restart':
                     global filename
                     XXX , filename = omurestart(var)
                     return XXX


@app.callback(
    Output('result-extended', 'children'),
    Output('switch-over','options'),
    # Output('description','children'),
    [Input('submit-operation', 'n_clicks'),
     Input('dropdown','value'),
     Input('case-input-0','value'),
     Input('switch-over','value')
     ]
)
def template_2(n_clicks,Selected_test,var,BTS):   # this function will be altered per user case name and returned to main app
    global options
    Feedback = html.Div([])
    if n_clicks is None:
         raise PreventUpdate
    else:
         changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
         if 'submit-operation' in changed_id:
             if Selected_test == 'BCXU Switchover':
                 if n_clicks == 1:
                     XXX, options = bcxuswo(var)
                     text = html.Div([
                         html.P('1) Please target Site'),
                         html.P('2) Activate')])
                     # Feedback = html.Div(
                     #     dbc.Fade(
                     #         dbc.Card(MO.usecase_description(text, 'Activate'),
                     #                  color='success',
                     #                  outline=True,
                     #                  style={
                     #                      'width': '30rem',
                     #                      'margin-top': '2px',
                     #                      'margin-bottom': '4px'
                     #                  }),
                     #         id='fade',
                     #         is_in=True,
                     #         appear=False)
                     # )
                     return XXX, options
                 elif n_clicks >=2 :
                     if BTS:
                             VM_path = '/opt/jetty/Mbackup/kkx/BCXU/'
                             local_path = 'C:\\Users\\aelmaghrabi\PycharmProjects\Prototype\Test05\\'
                             BSC_Regression = 'C:\\Users\\aelmaghrabi\PycharmProjects\Prototype\Test05\Operations\BSC_Regression\\'
                             btsid = BTS
                             df_bts = pd.Series(btsid)
                             arr_bts = df_bts.to_numpy()
                             np.savetxt('btsid.txt', arr_bts, fmt='%s')
                             send_ftp(local_path, VM_path, 'btsid.txt')
                             # return html.P(f'You have arrived at {BTS}'), options, False
                             XXX = extended_bcxuswo(BTS, var)
                             # n_clicks = 0
                             return XXX, options
         elif Selected_test != 'BCXU Switchover':
             return Feedback, []



# @app.callback(
#         # Output('result-extended', 'children'),
#         Output('switch-over','options'),
#     [
#         Input('submit-operation', 'n_clicks'),
#         Input('dropdown','value'),
#         Input('case-input-0','value'),
#         Input('switch-over','value')
#     ]
# )
# def template_2_extended(n_clicks,Selected_test,var,BTS):
#     pass
#     # if Selected_test == 'BCXU Switchover':
    #     if n_clicks >=2 :
    #         if BTS:
    #             VM_path = '/opt/jetty/Mbackup/kkx/BCXU/'
    #             local_path = 'C:\\Users\\aelmaghrabi\PycharmProjects\Prototype\Test05\\'
    #             BSC_Regression = 'C:\\Users\\aelmaghrabi\PycharmProjects\Prototype\Test05\Operations\BSC_Regression\\'
    #             btsid = BTS
    #             df_bts = pd.Series(btsid)
    #             arr_bts = df_bts.to_numpy()
    #             np.savetxt('btsid.txt', arr_bts, fmt='%s')
    #             send_ftp(local_path, VM_path, 'btsid.txt')
    #             # return html.P(f'You have arrived at {BTS}'), options, False
    #             XXX, filename = extended_bcxuswo(BTS, var)
    #             # n_clicks = 0
    #             return XXX
    #

#
# @app.callback(
#     Output('download-link', 'href'),
#     [Input('dropdown','value'),]
# )
# def download(value):
#     if value != '':
#         Log_path = 'C:\\Users\\aelmaghrabi\PycharmProjects\Prototype\Test05\Log_History\\'
#         df = pd.read_csv(Log_path+filename)
#         txt_string = df.to_csv(index=False, encoding='utf-8')
#         txt_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + quote(txt_string)
#
#         return txt_string