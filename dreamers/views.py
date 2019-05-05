from django.shortcuts import render
from django.http import HttpResponse
import json
# import time
# import os
# import glob
# import datetime
# from openalpr import Alpr
from influxdb import InfluxDBClient

# Create your views here.
def index(request):

    client = InfluxDBClient('10.84.109.148', 8086, 'root', 'root', '_internal')

    client.switch_database('dreamers')
    res = client.query('select * from "health_info"')

    data = list(res.get_points(measurement='health_info'))

    return render(request, "dreamers/index.html", {"data": data[-1]})

def home(request):
    return render(request, "dreamers/home.html")