import pandas as pd, os
import plotly.express as px
import dataupdater as dUpdate
import dash
import dash_core_components as dcc
import dash_html_components as html
import chartbuilder as cb


# These functions pull the latest Date sources
dUpdate.JHU()
dUpdate.CDCExcess()
dUpdate.covidTracking()

casesFig = cb.casesChart()
deathFig = cb.deathChart()
casesDayFig = cb.casesDayChart()
deathDayFig = cb.deathDayChart()

# Creates HTML file temp-plot and opens it
app = dash.Dash()

app.layout = html.Div([
    html.Div(html.H1(children="Covid-19 Comparison Charts:")),
    html.Div([html.H2("Covid 19 Total Cases:"),
              html.Div(
                  dcc.Graph(id="Cases",
                            figure=casesFig)
              )
              ], style={
        'height': '600',
        'width': '50%',
        'float': 'left'
    }),
    html.Div([html.H2("Covid 19 Total Deaths:"),
              html.Div(
                  dcc.Graph(id="Deaths",
                            figure=deathFig)
              )
              ], style={
        'height': '600',
        'width': '50%',
        'float': 'left'
    }),
    html.Div([html.H2("Covid 19 Cases Per Day:"),
              html.Div(
                  dcc.Graph(id="Cases Per Day",
                            figure=casesDayFig)
              )
              ], style={
        'height': '600',
        'width': '50%',
        'float': 'left'
    }),
    html.Div([html.H2("Covid 19 Deaths Per Day:"),
              html.Div(
                  dcc.Graph(id="Deaths Per Day",
                            figure=deathDayFig)
              )
              ], style={
        'height': '600',
        'width': '50%',
        'float': 'left'
    }),
], style={
    'width': '100%'
})
app.run_server()

