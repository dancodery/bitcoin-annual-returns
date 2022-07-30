"""

This simple Python script shows the annual bitcoin price performance (also known as annual Return on Investment).

The average price is determined by using the nth root.

__author__ = "Daniel Gockel"
__copyright__ = "Copyright 2022"
__email__ = "daniel@gockel.co"
"""

import urllib.request
from datetime import datetime, date
import pandas as pd
import os.path
from dateutil.relativedelta import relativedelta
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

app = Dash(__name__)

filename = "btcdata.csv"
if not os.path.exists(filename):
    url = "https://api.blockchain.info/charts/market-price?timespan=all&sampled=true&metadata=false&cors=true&format=csv"

    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        data = response.read()
        out_file.write(data)

df = pd.read_csv(filename, header=None)
df[0] = pd.to_datetime(df[0], format="%Y-%m-%d %H:%M:%S")
fig = go.Figure(data=[go.Scatter(
    x=df[0],
    y=df[1],
    mode='lines', )
])
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=5,
                     label="5 years",
                     step="year",
                     stepmode="todate"),
            ])
        ),
        rangeslider=dict(
            visible=True,
        ),
    )
)

app.layout = html.Div([
    html.H1("Bitcoin Annual Return on Investment Calculator:"),
    dcc.Graph(figure=fig),
    dcc.Slider(
        id='year_slider',
        min=2009,
        max=2021,
        value=2017,
        step=1,
        marks={
            2009: {'label': '2009'},
            2010: {'label': '2010'},
            2011: {'label': '2011'},
            2012: {'label': '2012'},
            2013: {'label': '2013'},
            2014: {'label': '2014'},
            2015: {'label': '2015'},
            2016: {'label': '2016'},
            2017: {'label': '2017'},
            2018: {'label': '2018'},
            2019: {'label': '2019'},
            2020: {'label': '2020'},
            2021: {'label': '2021'}
        },
        included=False
    ),
    html.Br(),
    html.H3(id='my-output'),
])


@app.callback(
    Output('my-output', 'children'),
    Input('year_slider', 'value')
)
def update_output_div(input_value):
    today = date.today()
    year_diff = int(today.year) - input_value
    years_ago = (datetime.now() - relativedelta(years=year_diff))
    current_price = float(df.iloc[-1, 1])
    ago_price_index = df[0].searchsorted(years_ago)
    ago_price = float(df.iloc[ago_price_index, 1])

    if ago_price > 0:
        annual_return = (((current_price / ago_price) ** (1 / year_diff)) - 1) * 100
        return f'From {years_ago.date()} {ago_price} to {today} {current_price}, annual return on investment is: {"%.2f" % annual_return}%'
    else:
        return 'Infinity'


if __name__ == "__main__":
    app.run_server(debug=True)
