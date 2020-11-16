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

	args = {}
	args['pf_data'] = pf_data
	args['stock'] = 'PG'

	df_marks = pd.DataFrame({'name': ['Somu', 'Kiku', 'Amol', 'Lini'],
     'physics': [68, 74, 77, 78],
     'chemistry': [84, 56, 73, 69],
     'algebra': [78, 88, 82, 87]})

	# render dataframe as html
	args['html'] = df_marks
	return render(request, 'stock/price.html', args)