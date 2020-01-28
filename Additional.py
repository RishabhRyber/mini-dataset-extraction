import requests 
from bs4 import BeautifulSoup 
import mysql.connector
import csv

#to initialize the csv file with header or column name
with open('additional.csv',mode='w') as data:
	fieldnames=["SymptomsCode","Definition"]
	writer=csv.DictWriter(data,fieldnames=fieldnames)
	writer.writeheader()

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="jamesBond@007"
)
cur = con.cursor()

diseaseCodes = []
symptomCode = []

cur.execute("USE mini_data")
cur.execute("SELECT code from symptoms ORDER BY code")

for i in cur:
    symptomCode.append(i[0])

cur.execute("SELECT code from diseases ORDER BY code")
for i in cur:
    diseaseCodes.append(i[0])

for code in diseaseCodes: 
	link = "https://ncim.nci.nih.gov/ncimbrowser/ConceptReport.jsp?dictionary=NCI Metathesaurus&code=" + code
	r = requests.get(link)
	bs = BeautifulSoup(r.content,'html.parser')
	rows = bs.find_all("div", {"class": "tabTableContentContainer"})
	print(code)

	try:
		for p in bs.find_all("p"):
			if(p.b.text == 'NCIt Definition: '):
				definition = p.text[17:]
				break
	except:
		print('Error occured')
	finally:
		with open('additional.csv',mode='a') as data:
			fieldnames=["SymptomsCode","Definition"]
			writer=csv.DictWriter(data,fieldnames=fieldnames)
			if(p.text[:17] == "NCIt Definition: "):				
				writer.writerow({'SymptomsCode':code,'Definition':definition})
				print(definition)
			else:
				writer.writerow({'SymptomsCode':code})	