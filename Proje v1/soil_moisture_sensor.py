from machine import ADC

class SoilMoistureSensor:
    def __init__(self, pin):
        self.pin = ADC(pin)

    def read_moisture(self):
        moisture_value = self.pin.read()
        moisture_percentage = (moisture_value / 1023.0) * 100.0
        return moisture_percentage
