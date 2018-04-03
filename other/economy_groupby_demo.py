
#!/usr/bin/python
import sys
import datetime
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import random
import string
random.seed(0)

# create N stock codes
N = 1000

def rands(n):
	choices = string.ascii_uppercase
	return ''.join([random.choice(choices) for _ in xrange(n)])

def create_tickers_by(name_len,number):
	tickers = np.array([rands(name_len) for _ in xrange(number)])
	return tickers

def create_tickers():
	return create_tickers_by(5,N)


M = 500
def create_dataframe(tickers):
	df = DataFrame({'Momentum':np.random.randn(M)/200+0.03
		,'Value':np.random.randn(M)/200+0.08
		,'ShortInterest':np.random.randn(M)/200 - 0.02}
		,index=tickers[:M])
	return df

def create_industry(tickers):
	ind_names = np.array(['FINANCIAL','TECH'])
	sampler = np.random.randint(0,len(ind_names),N)
	industries = Series(ind_names[sampler],index=tickers,name='industry')
	return industries

def main():
	tickers = create_tickers()
	df = create_dataframe(tickers)
	print df[:50]
	by_industry = df.groupby(create_industry(tickers))
	print by_industry.mean()
	return


if __name__ == "__main__":
	main()

