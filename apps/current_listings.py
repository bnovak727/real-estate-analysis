from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.models import NumeralTickFormatter
from flask import Flask, render_template, request

import numpy as np
import pandas as pd

from rea.data_sources.redfin import redfin

app = Flask(__name__)

df = redfin('Ypsilanti, MI', 100, 250)
feature_names = df.columns[0:-1].values.tolist()

def create_figure(current_feature_name):
    data = df[current_feature_name]
    hist, edges = np.histogram(data, bins=10)
    data.replace('',0,inplace=True)

    p = figure(sizing_mode='stretch_both')
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:])

    # Set the x axis label
    p.xaxis.axis_label = current_feature_name
    if 'price' in current_feature_name.lower() or \
        '$' in current_feature_name.lower():
        p.xaxis.formatter = NumeralTickFormatter(format='$0,0')

    # Set the y axis label
    p.yaxis.axis_label = 'Count'
    return p

# Index page
@app.route('/')
def index():
    # Determine the selected feature
    current_feature_name = request.args.get("feature_name")
    if current_feature_name == None:
        current_feature_name = "PRICE"

    plot = create_figure(current_feature_name)

    # Embed plot into HTML via Flask Render
    script, div = components(plot)
    return render_template("redfin.html", script=script, div=div,
        feature_names=feature_names,  current_feature_name=current_feature_name)
