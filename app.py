from flask import Flask, render_template
import pandas as pd
import json
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px
import plotly.graph_objects as go
from apscheduler.schedulers.background import BackgroundScheduler
import os


def update_data():
    os.system("python scripts/update.py")


def process_data():
    os.system("python scripts/process.py")


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(update_data, "interval", seconds=5)
scheduler.add_job(process_data, "interval", seconds=5)
scheduler.start()

app = Flask(__name__)


@app.route("/")
def index():
    df = pd.read_csv("raw/output.csv")
    percentage_ = round(df[-1:].iloc[0, 1] * 100, 2)
    ratio_ = round(1 / df[-1:].iloc[0, 1])
    latest_date_ = pd.to_datetime(df[-1:].iloc[0, 0]).strftime("%d/%m")

    fig = go.Figure(
        layout=go.Layout(
            template="simple_white",
            height=400,
            margin=dict(l=5, t=10, b=20, r=5),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=df.dte,
            y=df.pc.round(4),
            name="Modelled Prevalence",
            line=dict(color="#000000"),
        )
    )
    fig.update_layout(yaxis_tickformat="p")

    # fig = px.line(x=df.dte, y=df.pc, template="simple_white")

    chart_json = json.dumps(fig, cls=PlotlyJSONEncoder)

    return render_template(
        "index.html",
        ratio=ratio_,
        percentage=percentage_,
        latest_date=latest_date_,
        chart=chart_json,
    )
