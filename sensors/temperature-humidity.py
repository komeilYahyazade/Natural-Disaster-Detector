import time
import Adafruit_DHT
import requests

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        # Send a request to add the temperature
        temp_url = "http://192.168.36.170:8000/add_temperature/"
        temp_data = {'value': temperature}
        temp_response = requests.post(temp_url, data=temp_data)
        if temp_response.status_code == 200:
            print("Temperature added successfully")
        else:
            print("Failed to add temperature")

        # Send a request to add the humidity
        humidity_url = "http://192.168.36.170:8000/add_humidity/"
        humidity_data = {'value': humidity}
        humidity_response = requests.post(humidity_url, data=humidity_data)
        if humidity_response.status_code == 200:
            print("Humidity added successfully")
        else:
            print("Failed to add humidity")
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(1)
