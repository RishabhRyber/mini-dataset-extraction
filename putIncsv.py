import csv

code=[1,12,3,4]
disease=['a','b','c','d']
Occurances=[1,2,'',4]
symptoms=['sd','sds','sds','sdsd']

with open('data.csv',mode='w') as data:
	fieldnames=["DiseaseCode","DiseaseName","Occurances","Symptoms"]
	writer=csv.DictWriter(data,fieldnames=fieldnames)
	writer.writeheader()
	for i in range(len(code)):
		writer.writerow({'DiseaseCode':code[i],'DiseaseName':disease[i],'Occurances':Occurances[i],'Symptoms':symptoms[i]})	
