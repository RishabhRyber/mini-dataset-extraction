import requests 
from bs4 import BeautifulSoup 
import csv 

diseases =  []
diseaseCount = []
symptoms = [] 


r = requests.get("http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html")

bs = BeautifulSoup(r.content,'html5lib')

# bs = bs.prettify()
table = bs.tbody
rows = table.find_all('tr')

#temprorily stores symptoms of all current disease

temp = []
for row in rows:
    d1 = row.find_all("td")[0].p.span.get_text()
    count = row.find_all("td")[1].p.span.get_text()
    symptom = row.find_all("td")[2].p.span.get_text()
    if  d1.isspace():
        temp.append(symptom)
    else: 
        diseases.append(d1)
        symptoms.append(temp)
        diseaseCount.append(count)

for i in range(0, len(diseases)):
    print(diseases[i])
    print(symptoms[i])
    print(diseaseCount[i])
