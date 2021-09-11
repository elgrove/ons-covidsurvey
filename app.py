from flask import Flask, render_template
import pandas as pd
import json
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px

app = Flask(__name__)


@app.route("/")
def index():
    df = pd.read_csv("output.csv")
    percentage_ = df[-1:].iloc[0, 1].round(2)
    ratio_ = round(1 / df[-1:].iloc[0, 1].round(2) * 100)
    latest_date_ = pd.to_datetime(df[-1:].iloc[0, 0]).strftime("%d/%m")

    fig = px.line(x=df.dte, y=df.pc)

    chart_json = json.dumps(fig, cls=PlotlyJSONEncoder)

    return render_template(
        "index.html",
        ratio=ratio_,
        percentage=percentage_,
        latest_date=latest_date_,
        chart=chart_json,
    )
