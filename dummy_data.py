import time
import os
import glob
import datetime
from influxdb import InfluxDBClient

client = InfluxDBClient('10.84.109.148', 8086, 'root', 'root', '_internal')

result = client.query("show databases")
client.create_database('dreamers')
client.switch_database('dreamers')
# res = client.query("select * from light")
# res = client.query("show series on ruuvi5")
# res = client.query('show measurements')

json_body = [
    {
        "measurement": "health_info",
        "tags": {
            "region": "espoo"
        },
        # "time": 'timestamp',
        "fields": {
            "pole_id": 213,
            "id": 123456,
            "age": 30,
            "heart_rate": 80,
            "blood_pressure": 100,
            "bmi": 20,
            "height": 180,
            "weight": 75,
            "respiratory_rate": 30
        }
    },
    {
        "measurement": "health_info",
        "tags": {
            "region": "espoo"
        },
        # "time": 'timestamp',
        "fields": {
            "pole_id": 4423,
            "id": 923456,
            "age": 30,
            "heart_rate": 80,
            "blood_pressure": 100,
            "bmi": 20,
            "height": 180,
            "weight": 75,
            "respiratory_rate": 30
        }
    },
    {
        "measurement": "health_info",
        "tags": {
            "region": "espoo"
        },
        # "time": 'timestamp',
        "fields": {
            "pole_id": 423,
            "id": 133456,
            "age": 30,
            "heart_rate": 80,
            "blood_pressure": 100,
            "bmi": 20,
            "height": 180,
            "weight": 75,
            "respiratory_rate": 30
        }
    },

]

client.write_points(json_body)
res = client.query('select * from "health_info"')

print(res)