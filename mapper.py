import pandas as pd
import sys
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
#first make the file cleaner by removing the first line and all lines with heading like '#           time             counts unit events'

df = pd.DataFrame(columns=['instructions', 'L1-dcache-loads', 'L1-dcache-load-misses', 'branch-misses']);
data = dict();

count = 0
threshhold = 0.9999
below_count = 0
above_count = 0
#with open('scilab_report_1.txt') as f:

for line in sys.stdin:
	#print("hello", line)
	if(line[0] != '#' and line[0] != 'p'):
		line_array = line.split()
		#print(line_array[1])
		if(line_array[1].replace(',', '').isnumeric()):
			data[line_array[2]] = int(line_array[1].replace(',', ''))
		else:
			data[line_array[3]] = -1
		count+=1
		if(count%4 == 0):
			df = df.append(data, ignore_index = True)
			#print('hello', data)
			data.clear()
			#print(len(data))

#print(df)
#df.to_csv('scilab.csv')
l=[]
interval=[]
j=1
for i in range(0, len(df)-1):
	p1 = [ df.iloc[i]['instructions'], df.iloc[i]['L1-dcache-loads'], df.iloc[i]['L1-dcache-load-misses'], df.iloc[i]['branch-misses'] ] 
	p2 = [ df.iloc[i+1]['instructions'], df.iloc[i+1]['L1-dcache-loads'], df.iloc[i+1]['L1-dcache-load-misses'], df.iloc[i+1]['branch-misses'] ] 
	np1 = np.array(p1)
	np2 = np.array(p2)
	np1 = np1.reshape(1, -1)
	np2 = np2.reshape(1, -1)
	val = cosine_similarity(np1, np2)
	val1=float(val)
	if(val1>=0.999):
		l.append(val1)
		interval.append(j)
		j=j+1
print(l)
print(interval)
#print(below_count, above_count)
plt.scatter(interval,l)
plt.plot([0, j], [0.9999, 0.9999], c='r')    
plt.ylim(0.998,1.00005)
plt.show()
