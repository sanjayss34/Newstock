import pandas as pd
def get_data(symbol, month1, day1, year1, month2, day2, year2):
    print('a')
    symbol = symbol.upper()
    print(symbol)
    url = "http://chart.finance.yahoo.com/table.csv?s=" + symbol + "&a=" + str(month1) + "&b=" + str(day1) + "&c=" + str(year1) + "&d=" + str(month2) + "&e=" + str(day2) + "&f=" + str(year2) + "&g=d&ignore=.csv"
    print(url)
    return pd.read_csv(url, index_col=0)
