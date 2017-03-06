
# Enter your code here. Read input from STDIN. Print output to STDOUT
#from sklearn.linear_model import LinearRegression 
from sklearn.svm import SVR 
import datetime, time 
import numpy as np 
#from scipy import interpolate 

def isFloat(x):
		try: 
			float(x) 
			return True; 
		except: 
			return False 

dateTimeList = [] 
stockList = [] 
testList = [] 
total = int(raw_input()) 

i = 1 for i in range(int(total)): 
	x = raw_input().split('\t') 

#dateTimeValue = x[0].split() 
#dateValue = dateTimeValue[0].split('/') 
#timeValue = dateTimeValue[1].split(':') 
#t = datetime.datetime(int(dateValue[2]), int(dateValue[0]), 
# int(dateValue[1]), int(timeValue[0]), 
# int(timeValue[1]), int(timeValue[2])) 
#intTime = time.mktime(t.timetuple()) 

if isFloat(x[1]): 
	stock = float(x[1]) 
	stockList.append(stock) 
	dateTimeList.append(i) 
else: 
	testList.append(i) 

#dateTimeList = np.divide(dateTimeList, 1e6) 
#testList = np.divide(testList, 1e6) 

svr = SVR(kernel='rbf', C=20, gamma=0.1, epsilon=0.001) 
svr.fit(np.asarray(dateTimeList).reshape(total-20, 1), stockList) 
output = svr.predict(np.asarray(testList).reshape(20, 1)) 

for i in output: print i
 ''' f = interpolate.interp1d(dateTimeList, stockList) for val in testList: print f(val) '''