import requests

ticker = str(input("Please enter the ticker symbol of the company whose data you want: "))

import timeToUnix

p1 = timeToUnix.period1
p2 = timeToUnix.period2

r = requests.get("https://query1.finance.yahoo.com/v7/finance/download/" + ticker + "?period1=" + p1 + "&period2=" + p2 + "&interval=1d&events=history")

file = open(r'stock.csv', 'w')
file.write(r.text)
file.close()

