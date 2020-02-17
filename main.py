import psutil
from time import sleep
import time
import influxdb
from influxdb import InfluxDBClient


def get_cpu_load():
    return psutil.cpu_percent()


while True:
    time.sleep(1)
    print(get_cpu_load())

a = numpy.random.normal(1, 100)
b = numpy.random.normal(1, 1000)


def two_numbers():
    while True:
        print(f'from first {a}, from second {b}')
        sleep(1)


two_numbers()

