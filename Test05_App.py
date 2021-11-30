import dash

app = dash.Dash(
    __name__,
    assets_url_path='assets',
    suppress_callback_exceptions=True,
    # "OSC Automation Dashboard",
    meta_tags=[
        # A description of the app, used by e.g.
        # search engines when displaying search results.
        {
            'name': 'description',
            'content': 'My description'
        },
        # A tag that tells Internet Explorer (IE)
        # to use the latest renderer version available
        # to that browser (e.g. Edge)
        {
            'http-equiv': 'X-UA-Compatible',
            'content': 'IE=edge'
        },
        # A tag that tells the browser not to scale
        # desktop widths to fit mobile screens.
        # Sets the width of the viewport (browser)
        # to the width of the device, and the zoom level
        # (initial scale) to 1.
        #
        # Necessary for "true" mobile support.
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ],
    # external_stylesheets=[dbc.themes.BOOTSTRAP],
)
# app.index_string = '''
# <!DOCTYPE html>
# <html>
#     <head>
#         {%metas%}
#         <title>{%title%}</title>
#         {%favicon%}
#         {%css%}
#     </head>
#     <body>
#         <div>My Custom header</div>
#         {%app_entry%}
#         <footer>
#             {%config%}
#             {%scripts%}
#             {%renderer%}
#         </footer>
#         <div>My Custom footer</div>
#     </body>
# </html>
# '''

app.title = "OSC Automation Dashboard"

app_name = "OSC Automation Dashboard"
# app.renderer = 'var renderer = new DashRenderer();'
server = app.server
