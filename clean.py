import pandas as pd

#first make the file cleaner by removing the first line and all lines with heading like '#           time             counts unit events'

df = pd.DataFrame(columns=['instructions', 'L1-dcache-loads', 'L1-dcache-load-misses', 'branch-misses']);
data = dict();

count = 0
with open('f10') as f:
	for line in f:
		if(line[0] != '#'):
			line_array = line.split()
			if(line_array[1].replace(',', '').isnumeric()):
				data[line_array[2]] = int(line_array[1].replace(',', ''))
			else:
				data[line_array[3]] = -1
			count+=1
			if(count%4 == 0):
				df = df.append(data, ignore_index = True)
				print('hello', data)
				data.clear()
				#print(len(data))
print(df)

df.to_csv('f10.csv')
