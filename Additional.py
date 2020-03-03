import requests 
from bs4 import BeautifulSoup 
import mysql.connector
import csv

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="000012300"
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

def additionalDisease():
	#to initialize the csv file with header or column name
	with open('additional.csv',mode='w') as data:
		fieldnames=["DiseaseCode","Definition"]
		writer=csv.DictWriter(data,fieldnames=fieldnames)
		writer.writeheader()

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
				elif(p.b.text == 'GARD Definition: '):
					definition = p.text[17:]
					break
				elif(p.b.text == 'FDA Definition: '):
					definition = p.text[16:]
					break
				elif(p.b.text == 'HPO Definition: '):
					definition = p.text[16:]
					break
				elif(p.b.text == 'CTCAE Definition: '):
					definition = p.text[18:]
					break
				elif(p.b.text == 'NICHD Definition: '):
					definition = p.text[18:]
					break
				elif(p.b.text == 'MSH Definition: '):
					definition = p.text[16:]
					break
				elif(p.b.text == 'CSP Definition: '):
					definition = p.text[16:]
					break
		except:
			print('Error occured')
		finally:
			with open('additional.csv',mode='a') as data:
				fieldnames=["DiseaseCode","Definition"]
				writer=csv.DictWriter(data,fieldnames=fieldnames)
				if(p.text[:17] == "NCIt Definition: "):				
					writer.writerow({'DiseaseCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:17] == "GARD Definition: "):				
					writer.writerow({'DiseaseCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:16] == "FDA Definition: "):				
					writer.writerow({'DiseaseCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:16] == "HPO Definition: "):				
					writer.writerow({'DiseaseCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:18] == "CTCAE Definition: "):				
					writer.writerow({'DiseaseCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:18] == "NICHD Definition: "):				
					writer.writerow({'DiseaseCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:16] == "CSP Definition: "):				
					writer.writerow({'DiseaseCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:16] == "MSH Definition: "):				
					writer.writerow({'DiseaseCode':code,'Definition':definition})
					print(definition)
				else:
					writer.writerow({'DiseaseCode':code})


def additionalSymptom():

	with open('additionalSymptom.csv',mode='w') as data:
		fieldnames=["SymptomCode","Definition"]
		writer=csv.DictWriter(data,fieldnames=fieldnames)
		writer.writeheader()

	for code in symptomCode: 
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
				elif(p.b.text == 'GARD Definition: '):
					definition = p.text[17:]
					break
				elif(p.b.text == 'FDA Definition: '):
					definition = p.text[16:]
					break
				elif(p.b.text == 'HPO Definition: '):
					definition = p.text[16:]
					break
				elif(p.b.text == 'CTCAE Definition: '):
					definition = p.text[18:]
					break
				elif(p.b.text == 'NICHD Definition: '):
					definition = p.text[18:]
					break
				elif(p.b.text == 'MSH Definition: '):
					definition = p.text[16:]
					break
				elif(p.b.text == 'CSP Definition: '):
					definition = p.text[16:]
					break
		except:
			print('Error occured')
		finally:
			with open('additionalSymptom.csv',mode='a') as data:
				fieldnames=["SymptomCode","Definition"]
				writer=csv.DictWriter(data,fieldnames=fieldnames)
				if(p.text[:17] == "NCIt Definition: "):				
					writer.writerow({'SymptomCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:17] == "GARD Definition: "):				
					writer.writerow({'SymptomCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:16] == "FDA Definition: "):				
					writer.writerow({'SymptomCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:16] == "HPO Definition: "):				
					writer.writerow({'SymptomCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:18] == "CTCAE Definition: "):				
					writer.writerow({'SymptomCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:18] == "NICHD Definition: "):				
					writer.writerow({'SymptomCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:16] == "CSP Definition: "):				
					writer.writerow({'SymptomCode':code,'Definition':definition})
					print(definition)
				elif(p.text[:16] == "MSH Definition: "):				
					writer.writerow({'SymptomCode':code,'Definition':definition})
					print(definition)
				else:
					writer.writerow({'SymptomCode':code})

additionalDisease()
additionalSymptom()