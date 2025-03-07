# python built- in modules -> math,date
# local modules -> functions.py, oop.py
# 3rd party librarie -> request vs...

#import math # math kütüphanesini dahil ettik
from math import sqrt,pi
from inheritance import car
import requests
print(sqrt(16)) # 4
print(pi) # 3.141592653589793

car = car("hyundai")
car.start()
response = requests.get("https://www.google.com.tr/?hl=tr")
print(response.status_code)