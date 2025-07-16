
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

LEAGUES = [
    "Mistrzowska", "Platynowa", "Diamentowa", "Złota",
    "Srebrna", "Brązowa", "Miedziana", "Żelazna"
]

DATA_PATH = "data.xlsx"
CSV_RESULTS_PATH = "results.csv"
LOG_PATH = "logs/awanse_spadki.csv"

def load_data():
    return pd.read_excel(DATA_PATH, sheet_name=None)

def save_data(data_dict):
    with pd.ExcelWriter(DATA_PATH) as writer:
        for league, df in data_dict.items():
            df.to_excel(writer, sheet_name=league, index=False)

@app.route('/')
def index():
    data = load_data()
    return render_template('index.html', leagues=LEAGUES, data=data)

@app.route('/admin')
def admin():
    return render_template('admin.html', password="Raph!nh4BallonDor")

if __name__ == '__main__':
    app.run(debug=True)
