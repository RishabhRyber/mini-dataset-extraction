import pandas as pd
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="000012300"
)
cur = con.cursor()
cur.execute("USE mini_data")
# cur.execute("""CREATE TABLE diseases(
#     code VARCHAR(30) NOT NULL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     details TEXT(500),
#     precautions TEXT(500)

# )""")
for i in cur:
    print(i)


data = pd.read_csv("Database.csv")
disease_codes_series=data["DiseaseCode"]
disease_codes = list(set(disease_codes_series))

for code in disease_codes:
    ind = disease_codes_series[disease_codes_series == code].index[0]
    print(ind)
    name = data["DiseaseName"][ind]
    print(name)
    cur.execute("""
        INSERT INTO diseases VALUE(
            "?","?","This is a very dangerous disease","No special precautions"
        )
    """.format(code,name))
    