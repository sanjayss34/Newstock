from flask import Flask, render_template, request, jsonify
from fetch_stock_data import get_data
import datetime
import pandas as pd
import ml
import urllib2

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
    data = ml.get_data(args['symbol'])
    new_data = {}
    print(len(data.keys()))
    for d in data.keys():
        date = data[d][0][:10]
        if data[d][0] not in new_data.keys():
            new_data[date] = [(d, data[d][1])]
        else:
            new_data[date].append((d, data[d][1]))
    return jsonify(**{'Dates': list(df.index.astype('str'))[::-1], 'Prices': list(df['Adj Close'])[::-1], 'ArticleData': new_data})

@app.route('/symbols', methods=['GET'])
def symbols():
    args = request.args.to_dict()
    symbols_file = urllib2.urlopen('ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt')
    symbols_lines = symbols_file.readlines()
    symbols_dict = {}
    for i in range(1, len(symbols_lines)-1):
        info = symbols_lines[i].split('|')
        symbols_dict[info[0]] = info[1]
    return symbols_dict

if __name__ == "__main__":
    app.run()
