import csv
import main

diseaseCode=[]
diseaseName=[]
symptomCode=[]
symptomName=[]
tempCode=[]
tempName=[]

# including diseaseName and diseaseCode to the database
disease,occurances,symptoms = main.funct()
for i in range(len(disease)):
	diseaseCode.append(disease[i][5:13])
	diseaseName.append(disease[i][14:])
	for j in range(len(symptoms[i])):
		tempCode.append(symptoms[i][j][5:13])
		tempName.append(symptoms[i][j][14:])
	symptomCode.append(tempCode)
	symptomName.append(tempName)
	tempName=[]
	tempCode=[]

with open('data.csv',mode='w') as data:
	fieldnames=["DiseaseCode","DiseaseName","Occurances","SymptomsCode","SymptomsName"]
	writer=csv.DictWriter(data,fieldnames=fieldnames)
	writer.writeheader()
	for i in range(1,len(diseaseName)-1):
		for j in range(len(symptoms[i])):
			writer.writerow({'DiseaseCode':diseaseCode[i],'DiseaseName':diseaseName[i],'Occurances':occurances[i],'SymptomsCode':symptomCode[i][j],'SymptomsName':symptomName[i][j]})