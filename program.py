import requests
import mysql.connector
import json
import time

# Database Variables
db_host = "localhost"
db_username = "root"
db_password = ""
db_name = "db_ecook_data"

# Connection Variables
api_url = "https://payg.angazadesign.com/nexus/v1/usage_data?unit_number="
username = "atec_iot"
password = "U*p9fJi31$$X"

# Initial/ Default values
unit_numbers = []
unit_number = "69074953"
from_date = "2021-12-17T00:00:00+00:00"
end_date = "2021-12-20T00:00:00"

# Database Connection
db_connection = mysql.connector.connect(host=db_host, user=db_username, password=db_password, database=db_name)


# Function to return the list of all ecook serial numbers
def get_all_ecook_id():
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT unit_number FROM tbl_ecook")
    db_result = db_cursor.fetchall()
    all_units = []
    for i in db_result:
        all_units.append(db_result["unit_number"])
    return all_units


# Main Program
unit_numbers = get_all_ecook_id()
print(unit_numbers)
