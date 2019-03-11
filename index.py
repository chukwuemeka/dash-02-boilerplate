import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import importlib

from app import app


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    module_name = pathname.replace("/",".") if pathname is not None and pathname != '/'  else ".home"

    modul = importlib.import_module(module_name, "apps")

    return modul.layout

external_css = ["hhttps://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]
                
if __name__ == '__main__':
    app.run_server(debug=True)