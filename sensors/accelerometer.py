import time
import board
import busio
import adafruit_adxl34x
import requests

url = 'http://192.168.36.170:8000/add_acceleration/'

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

while True:
    x, y, z = accelerometer.acceleration
    print("%f %f %f" % (x, y, z))
    
    data = {
        'x': x,
        'y': y,
        'z': z
    }
    
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print('POST request successful')
    else:
        print(f'POST request failed with error code {response.status_code}')
    
    time.sleep(1)
