from soil_moisture_sensor import SoilMoistureSensor
from temperature_sensor import TemperatureSensor
from oled_display import OLEDDisplay
from relay import Relay
from wifi_connection import connect_wifi, disconnect_wifi
from thingspeak import send_data_to_thingspeak, read_sensor_values
from time import sleep
from datetime import datetime

def main():
    moisture_sensor = SoilMoistureSensor(36)
    temperature_sensor = TemperatureSensor((22, 21), 0x5c)
    oled = OLEDDisplay(128, 64, (22, 21), 0x3c)
    relay = Relay(3)

    WIFI_SSID = "UREL-SC661-V-2.4G"
    WIFI_PSWD = "TomFryza"
    THINGSPEAK_API_KEY = "9DMMO9PAUUENESA9"  #We need to check this again

    connect_wifi(WIFI_SSID, WIFI_PSWD)

    try:
        while True:
            temperature, air_humidity, soil_humidity = read_sensor_values(temperature_sensor, air_humidity_sensor, moisture_sensor)
            current_time = datetime.now().strftime("%H:%M:%S")  # Get current time

            display_data = f"Soil Mois: {soil_humidity}%\nT: {temperature}\nHum: {air_humidity}\nTime: {current_time}"

            print(display_data)  # Print data to console

            oled.show_message(display_data)  # Show data on OLED

            # We need to calculate threshold value
            if soil_humidity < threshold_value:  #instead of soil_humidity we can create a mix of all three values from sensors
                relay.control_relay(True, 1000)  # calculate the time for relay opening instead of 1s or keep 1s and it will keep opening for 1s till values are above threshold

            send_data_to_thingspeak(THINGSPEAK_API_KEY, temperature, air_humidity, soil_humidity)

            disconnect_wifi()

            sleep(60)  # Delay between readings 1m maybe 1800 for 30m

    except KeyboardInterrupt:
        print("Execution stopped.")
