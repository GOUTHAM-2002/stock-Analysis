import yfinance as yf

import matplotlib.pyplot as plt

ticker = "AAPL"
start_date = "2016-01-01"
end_date = "2021-01-01"
stock_data = yf.download(ticker, start=start_date, end=end_date)

stock_data["MA_50"] = stock_data["Close"].rolling(window=50).mean()
stock_data["MA_200"] = stock_data["Close"].rolling(window=200).mean()


stock_data["Daily_Return"] = stock_data["Close"].pct_change()
plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data["Close"], label="Close Price", color="blue")
plt.plot(stock_data.index, stock_data["MA_50"], label="MA 50", color="orange")
plt.plot(stock_data.index, stock_data["MA_200"], label="MA 200", color="red")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"{ticker} Stock Price")
plt.legend()
plt.show()
