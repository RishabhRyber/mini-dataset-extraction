import csv
import main

diseaseCode=[]
diseaseName=[]

# including diseaseName and diseaseCode to the database
disease,occurances,symptoms = main.funct()
for i in range(len(disease)):
	diseaseCode.append(disease[i][5:13])
	diseaseName.append(disease[i][14:])

with open('data.csv',mode='w') as data:
	fieldnames=["DiseaseCode","DiseaseName","Occurances","Symptoms"]
	writer=csv.DictWriter(data,fieldnames=fieldnames)
	writer.writeheader()
	for i in range(1,len(diseaseName)):
		for j in range(len(symptoms[i])):
			writer.writerow({'DiseaseCode':diseaseCode[i],'DiseaseName':diseaseName[i],'Occurances':occurances[i],'Symptoms':symptoms[i][j]})
