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
Select name from symptoms
""")

with open('SymptomsName.csv',mode='w') as data:
	fieldnames=["SymptomsName"]
	writer=csv.DictWriter(data,fieldnames=fieldnames)
	writer.writeheader()
	for i in cur:
		writer.writerow({'SymptomsName':i[0]})