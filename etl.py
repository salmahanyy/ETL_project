import mysql.connector
import requests
import json
import pandas as pd
from sqlalchemy import create_engine

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

data = response.json()

with open("data.json", "w") as file:
    json.dump(data,file)
    
# print(data)

normalized_data = pd.json_normalize(data)
df = pd.DataFrame(normalized_data)
# print(df)

normalized_data=normalized_data[[
    "id",
    "name",
    "username",
    "email",
    "address.street",
    "address.suite",
    "address.city",
    "address.zipcode",
    "phone",
    "website",
    "company.name",
    ]]

normalized_data.columns = ["id","name","username","email","street","suite","city","zipcode","phone","website","company_name"]

normalized_data.to_csv("users.csv",index=False)
# print("////////")
# print(normalized_data)

print(normalized_data.isnull().sum())
print(normalized_data.dtypes)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Salma@mysql.learn",
    database="user_data"
)
cursor = conn.cursor()

users_df = pd.read_csv("users.csv")


for _, row in users_df.iterrows():
    sql = "INSERT INTO user (id, name, username, email, street, suite, city, zipcode, phone, website, company_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (row["id"], row["name"], row["username"], row["email"], row["street"],
                row["suite"], row["city"], row["zipcode"],
                row["phone"] , row["website"], row["company_name"])  
    cursor.execute(sql, values)

conn.commit()
cursor.close()
conn.close()



