import pandas as pd
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="000012300"
)
cur = con.cursor()

def disease_insertion():
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
        querry = 'INSERT INTO diseases(code,name,details, precautions) VALUES('
        querry+='%s, %s ,"This is a very dangerous disease","No special precautions") ;'
        cur.execute(querry,(code,name))

    con.commit()

def symptoms_insertion():
    cur.execute("USE mini_data")
    # cur.execute("""CREATE TABLE symptoms(
    #     code VARCHAR(30) NOT NULL PRIMARY KEY,
    #     name VARCHAR(100) NOT NULL,
    #     details TEXT(500),
    #     additional TEXT(500)

    #     )""")
    data = pd.read_csv("Database.csv")
    symptom_codes_series=data["SymptomsCode"]
    symptom_codes = list(set(symptom_codes_series))

    for code in symptom_codes:
        ind = symptom_codes_series[symptom_codes_series == code].index[0]
        print(ind)
        name = data["SymptomsCode"][ind]
        print(name)
        querry = 'INSERT INTO symptoms(code,name,details, additional) VALUES('
        querry+='%s, %s ,"This is a very dangerous disease","No special precautions") ;'
        cur.execute(querry,(code,name))

    con.commit()

def symptom_disease_relation_insert():

    ##to create table
    #     """ CREATE TABLE disease_symptom(
    #     disease_code VARCHAR(30) NOT NULL ,
    #     symptom_code VARCHAR(30) NOT NULL,
    #     id int(5)  NOT NULL PRIMARY KEY, 
    #     FOREIGN KEY(disease_code) REFERENCES diseases(code),
    #     FOREIGN KEY(symptom_code) REFERENCES symptoms(code)
    #     );
    # """
    cur.execute("USE mini_data")
    data = pd.read_csv("Database.csv")
    for i in zip(data["SymptomsCode"],data["DiseaseCode"]):
        cur.execute("INSERT INTO disease_symptom(disease_code,symptom_code) VALUES(%s , %s)",(i[1],i[0]))
    con.commit()


symptom_disease_relation_insert()
