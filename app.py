from flask import Flask, render_template, request, jsonify
from fetch_stock_data import get_data
import datetime
import pandas as pd
import ml

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stockdata", methods=['GET'])
def stockdata():
    args = request.args.to_dict()
    today = datetime.datetime.now()
    month_before = today - pd.Timedelta(weeks=4)
    print(args['symbol'])
    df = get_data(args['symbol'], month_before.month-1, month_before.day, month_before.year, today.month-1, today.day, today.year)
    print('done')
    data = ml.get_data(args['symbol'])
    return jsonify(**{'Dates': list(df.index.astype('str')), 'Prices': list(df['Adj Close'])})
    data = ml.get_data(args['symbol'])

if __name__ == "__main__":
    app.run()
