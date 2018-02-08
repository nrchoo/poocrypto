import os
import pandas as pd
import sqlite3
import sqlalchemy 
from bs4 import Comment,BeautifulSoup
import requests

from datetime import date
from dateutil.rrule import rrule, DAILY

#Standard Imports
import csv
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
import re
from sklearn.cluster import KMeans
import random
from sklearn import datasets
from sklearn import metrics

import matplotlib
#matplotlib.style.use('default')
import seaborn as sns
from datetime import datetime

import httplib
import requests
import time, threading
import datetime


def foo():
    print(time.ctime())
    conn = sqlite3.connect('/Users/nathanchoo/cryptodb/crypto.db')
    cur = conn.cursor()
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=10").json()
    for row in r:
        cur.execute("INSERT INTO CMC_FIVE (date,name,ticker,last_updated,marketcap) VALUES (?,?,?,?,?)",\
                    (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),row['id'],row['symbol'],datetime.datetime.fromtimestamp(int(row['last_updated'])).strftime('%Y-%m-%d %H:%M:%S'),row['market_cap_usd']));
    conn.commit()
    threading.Timer(10, foo).start()

foo()