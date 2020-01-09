import requests 
from bs4 import BeautifulSoup 
import csv 
import re

diseases =  []
diseaseCount = []
symptoms = [] 


r = requests.get("http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html")
bs = BeautifulSoup(r.content,'html.parser')
rows = bs.find_all('tr')

#temprorily stores symptoms of all current disease
temp = []
symptom=[]

for row in rows:
    d1 = re.sub(' +',' ',row.find_all("td")[0].p.span.get_text().replace('\n',' '))
    count = row.find_all("td")[1].p.span.get_text()
    symptom = re.sub(' +',' ',row.find_all("td")[2].p.span.get_text().replace('\n',' '))
    if  d1.isspace():
        temp.append(symptom)
    else: 
        diseases.append(d1)
        symptoms.append(temp)
        diseaseCount.append(count)
        temp=[symptom]

symptoms.append(symptom)
symptoms.pop(0)

# for i in range(len(diseases)):
#     print(diseases[i],"\t",symptoms[i],"\t",diseaseCount[i],"\n\n")

def funct():
    return diseases,diseaseCount,symptoms