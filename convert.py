import requests 
import mysql.connector
import json
import time
import datetime

db_host = "localhost"
db_username = "root"
db_password = ""
db_name = "db_ecook_data"

'''
con_url = "https://payg.angazadesign.com/nexus/v1/usage_data?unit_number="
username = "atec_iot"
password = "U*p9fJi31$$X"
'''

unit_number = "69074953"
from_date = "2022-01-02T00:00:00+00:00"
end_date = "2022-01-11T00:00:00"

#full_request = con_url + unit_number + "&from_when_dt=" + from_date + "&to_when_dt=" + end_date

#auth_values = (username, password)

#response = requests.get(full_request, auth=auth_values)

#print(json.dumps(response.json(), indent=2))

db_con = mysql.connector.connect(host=db_host, user=db_username, password=db_password, database=db_name)

db_cursor = db_con.cursor()
db_cursor.execute("SELECT * FROM tbl_ecook")
db_result = db_cursor.fetchall()
db_cursor.close()

for x in db_result:
    unit_number = x[1]
    raw_db_cursor = db_con.cursor()
    raw_sql = "SELECT * FROM tbl_raw_data WHERE unit_number = %s"
    raw_db_cursor.execute(raw_sql, (unit_number,))
    raw_db_result = raw_db_cursor.fetchall()
    raw_db_cursor.close()

    # Battery Critical State Count: 223 / 300 / 286 / 244
    battery_critial_state_count_counter = 0
    battery_critial_state_count_sum = 0
    battery_critial_state_count_avg = 0
    battery_critial_state_count_min = 0
    battery_critial_state_count_max = 0

    # 1 Hour Samples Count: 224 / 301 / 287 / 245
    one_hour_sample_count_counter = 0
    one_hour_sample_count_sum = 0
    one_hour_sample_count_avg = 0
    one_hour_sample_count_min = 0
    one_hour_sample_count_max = 0

    # Factory Mode Entry Count: 226 / 303 / 289 / 247
    factory_mode_entry_count_counter = 0
    factory_mode_entry_count_sum = 0
    factory_mode_entry_count_avg = 0
    factory_mode_entry_count_min = 0
    factory_mode_entry_count_max = 0

    # Max Battery Voltage (Last 12 Hours): 221 / 298 / 284 / 242
    max_battery_voltage_counter = 0
    max_battery_voltage_sum = 0
    max_battery_voltage_avg = 0
    max_battery_voltage_min = 0
    max_battery_voltage_max = 0

    # Min Battery Voltage (Last 12 Hours): 222 / 299 / 285 / 243
    min_battery_voltage_counter = 0
    min_battery_voltage_sum = 0
    min_battery_voltage_avg = 0
    min_battery_voltage_min = 0
    min_battery_voltage_max = 0

    # Right Stove Cooktime per Hour: 231 / 308 / 294 / 252
    right_stove_cooking_time_counter = 0
    right_stove_cooking_time_sum = 0
    right_stove_cooking_time_avg = 0
    right_stove_cooking_time_min = 0
    right_stove_cooking_time_max = 0

    # Left Stove Cooktime per Hour: 230 / 307 / 293 / 251
    left_stove_cooking_time_counter = 0
    left_stove_cooking_time_sum = 0
    left_stove_cooking_time_avg = 0
    left_stove_cooking_time_min = 0
    left_stove_cooking_time_max = 0

    # Average Battery Voltage (Last 12 Hours): 220 / 297 / 283 / 241
    average_battery_voltage_counter = 0
    average_battery_voltage_sum = 0
    average_battery_voltage_avg = 0
    average_battery_voltage_min = 0
    average_battery_voltage_max = 0

    # Product MCU Firmware ID (ATEC): 232 / 296 / 282 / 240
    product_mcu_firmware_counter = 0
    product_mcu_firmware_sum = 0
    aproduct_mcu_firmware_avg = 0
    product_mcu_firmware_min = 0
    product_mcu_firmware_max = 0

    # Stove On/Off Count: 228 / 305 / 291 / 249
    stove_on_off_count_counter = 0
    stove_on_off_count_sum = 0
    stove_on_off_count_avg = 0
    stove_on_off_count_min = 0
    stove_on_off_count_max = 0

    # GSM Sync Button Count: 227 / 304 / 290 / 248
    gsm_sync_button_count_counter = 0
    gsm_sync_button_count_sum = 0
    gsm_sync_button_count_avg = 0
    gsm_sync_button_count_min = 0
    gsm_sync_button_count_max = 0

    # Lock Mode Entry Count: 225 / 302 / 288 / 246
    lock_mode_entry_count_counter = 0
    lock_mode_entry_count_sum = 0
    lock_mode_entry_count_avg = 0
    lock_mode_entry_count_min = 0
    lock_mode_entry_count_max = 0

    # Energy Consumed per Hour': 229 / 306 / 292 / 250
    energy_consumed_counter = 0
    energy_consumed_sum = 0
    energy_consumed_avg = 0
    energy_consumed_min = 0
    energy_consumed_max = 0


    for i in raw_db_result:
        unit = i[1]
        tpe = i[2]
        value = i[3]
        tme = i[4]

        # Average Battery Voltage (Last 12 Hours): 220 / 297 / 283 / 241
        if tpe == 220 or tpe == 297 or tpe == 283 or tpe == 241:
            average_battery_voltage_counter += 1
            average_battery_voltage_sum += value
            if average_battery_voltage_min >= value:
                average_battery_voltage_min = value
            if average_battery_voltage_max <= value:
                average_battery_voltage_max = value 

        # Max Battery Voltage (Last 12 Hours): 221 / 298 / 284 / 242
        if tpe == 221 or tpe == 298 or tpe == 284 or tpe == 242:
            max_battery_voltage_counter += 1
            max_battery_voltage_sum += value
            if max_battery_voltage_min >= value:
                max_battery_voltage_min = value
            if max_battery_voltage_max <= value:
                max_battery_voltage_max = value

        # Min Battery Voltage (Last 12 Hours): 222 / 299 / 285 / 243
        if tpe == 222 or tpe == 299 or tpe == 285 or tpe == 243:
            min_battery_voltage_counter += 1
            min_battery_voltage_sum += value
            if min_battery_voltage_min >= value:
                min_battery_voltage_min = value
            if min_battery_voltage_max <= value:
                min_battery_voltage_max = value
        
    dt_cursor = db_con.cursor()
    dt_sql = "SELECT IFNULL(MIN(when_date), '2021-11-01') AS min_date, DATE_SUB(CURDATE(), INTERVAL 1 DAY) AS max_date FROM report_dailyusagedata WHERE serial_number = %s"
    dt_cursor.execute(dt_sql, (unit,))
    dt_result = dt_cursor.fetchone()
    min_date = dt_result[0]
    max_date = dt_result[1]

    min_date = datetime.date.fromisoformat(str(min_date))
    max_date = datetime.date.fromisoformat(str(max_date))
        
    delta = datetime.timedelta(days=1)
    date_counter = min_date
    while date_counter <= max_date:
        print(date_counter)
        date_counter += delta

    #print(f"Unit: {unit}\nType: {tpe}\nValue: {value}\nDate: {tme}\nMIN Date: {min_date}\nMAX Date: {max_date}\n")


'''
print(f"Time: {time}, Type: {type}, Value: {value}")
inserrt_cursor = db_con.cursor()
sql = "INSERT INTO tbl_raw_data(unit_number, type, value, time) VALUES (%s, %s, %s, %s)"
val = (unit_number, type, value, time)
inserrt_cursor.execute(sql, val)
db_con.commit()
print(inserrt_cursor.rowcount, "Record Inserted")
'''