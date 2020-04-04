import mysql.connector
import csv

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="jamesBond@007"
)
cur = con.cursor()

cur.execute("USE mini_data")
cur.execute("""
Select code,name from diseases
""")

with open('DiseaseName.csv',mode='w') as data:
	fieldnames=["DiseaseCode","DiseaseName"]
	writer=csv.DictWriter(data,fieldnames=fieldnames)
	writer.writeheader()
	for i in cur:
		writer.writerow({'DiseaseCode':i[0],'DiseaseName':i[1]})