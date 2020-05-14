import sqlite3
import pandas as pd
import numpy as np
from pandas_datareader import data

def Fill_table(ticker:str):
    # 2019 Stock Data to a DF  from which I populate the DB later
    df = data.DataReader(ticker, start='2019-1-1', end='2019-12-31',data_source='yahoo')   

    # Creates table 

    # Only bug is that after a new DB is created for a given ticker it saves it to
    # Stock_Data.DB. To look at a new ticker, we must delete the previously created DB

    conn = sqlite3.connect('Stock_Data.db') 
    c = conn.cursor()                  
    createTable =  """ CREATE TABLE IF NOT EXISTS 'Stock_Data' (                        
                                        'Timestamp' INTEGER NOT NULL,
                                        'Open' decimal(10,2) ,
                                        'High' decimal(10,2),
                                        'Low' decimal(10,2),
                                        'Close' decimal(10,2),
                                        'Adj_Close' decimal(10,2)
                                    ); """
    c.execute(createTable)

    # In this for loop I am using an f string to give the INSERT statement values from the dataframe and then populating the DB
    
    for a in range(len(df)):
        c.execute(f""" INSERT INTO 'Stock_Data' VALUES ('{df.index[a]}', {df['Open'][a]}, {df['High'][a]}, {df['Low'][a]}, {df['Close'][a]}, {df['Adj Close'][a]}); """)
        
    conn.commit()
    conn.close()


def Daily_Returns(closes):
    adj_closes = np.array(closes)[1:]
    previous = np.array(closes)[:-1]
    return (((adj_closes/previous)-1)*100)

def Monthly_Var(confidence=0.05):
    conn = sqlite3.connect('Stock_Data.db')
    c = conn.cursor()
    c.execute("""SELECT  Adj_Close FROM Stock_Data """)
    closes = np.array(c.fetchall())
    return pd.DataFrame((Daily_Returns(closes))).quantile(confidence)[0]

