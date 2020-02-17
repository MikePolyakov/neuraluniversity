"""
Загрузка ядер процессора
"""
import psutil
import time


def get_cpu_load():
    return psutil.cpu_percent(percpu=True)


while True:
    time.sleep(1)
    print(get_cpu_load())