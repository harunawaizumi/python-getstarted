from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

def index(request):
	assets = ['PG', '^GSPC']
	pf_data = pd.DataFrame()
	for a in assets:
		pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2010-1-1')['Adj Close']
	return HttpResponse("this is price page")