import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.graph_objs as go
import os
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_auth
from users import USERNAME_PASSWORD_PAIRS

from app import app

import pages

server = app.server
#auth = dash_auth.BasicAuth(
#    app,
#    USERNAME_PASSWORD_PAIRS
#)

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        dbc.Navbar(
            children=[
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src=app.get_asset_url("logo.png"), height="30px"
                                )
                            ),
                            dbc.Col(
                                dbc.NavbarBrand(
                                    "Ipromor", className="ml-2"
                                )
                            ),
                        ],
                        no_gutters=True,
                        className="ml-auto flex-nowrap mt-3 mt-md-0",
                        align="center",
                    ),
                    href=app.get_relative_path("/"),
                ),
                dbc.Row(
                    children=[
                        dbc.NavLink("Inicio", href=app.get_relative_path("/")),
                        dbc.NavLink("Global", href=app.get_relative_path("/seasons")),
                        dbc.NavLink("Maquinas", href=app.get_relative_path("/drivers")),
                    ],
                    style={"paddingLeft": "480px"},
                ),
            ]
        ),
        html.Div(id="page-content"),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page_content(pathname):
    path = app.strip_relative_path(pathname)
    if not path:
        return pages.inicio.layout()
    elif path == "seasons":
        return pages.seasons.layout()
    elif path == "drivers":
        return pages.drivers.layout()
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
