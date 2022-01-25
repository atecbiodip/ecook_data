import requests 
import mysql.connector
import json
import time

db_host = "localhost"
db_username = "root"
db_password = ""
db_name = "db_ecook_data"

con_url = "https://payg.angazadesign.com/nexus/v1/usage_data?unit_number="
username = "atec_iot"
password = "U*p9fJi31$$X"

unit_number = "69074953"
from_date = "2022-01-02T00:00:00+00:00"
end_date = "2022-01-11T00:00:00"

#full_request = con_url + unit_number + "&from_when_dt=" + from_date + "&to_when_dt=" + end_date

auth_values = (username, password)

#response = requests.get(full_request, auth=auth_values)

#print(json.dumps(response.json(), indent=2))

db_con = mysql.connector.connect(host=db_host, user=db_username, password=db_password, database=db_name)

db_cursor = db_con.cursor()
db_cursor.execute("SELECT * FROM tbl_ecook")
db_result = db_cursor.fetchall()

for x in db_result:
    unit_number = x[1]
    full_request = con_url + unit_number + "&from_when_dt=" + from_date + "&to_when_dt=" + end_date
    response = requests.get(full_request, auth=auth_values)
    if response.status_code == 200:
        rjson = response.json()
        wdata = rjson["_embedded"]["item"]
        count = len(wdata)
        print(count)
        for i in range(0, count):
            sdata = wdata[i]
            type = sdata['type']
            value = sdata['value']
            time = sdata['when']
            print(f"Time: {time}, Type: {type}, Value: {value}")
            inserrt_cursor = db_con.cursor()
            sql = "INSERT INTO tbl_raw_data(unit_number, type, value, time) VALUES (%s, %s, %s, %s)"
            val = (unit_number, type, value, time)
            inserrt_cursor.execute(sql, val)
            db_con.commit()
            print(inserrt_cursor.rowcount, "Record Inserted")
        #time.sleep(0.5)
    else:
        pass



