from machine import I2C

class TemperatureSensor:
    def __init__(self, pins, address):
        self.i2c = I2C(0, scl=pins[0], sda=pins[1], freq=100000)
        self.address = address

    def read_temperature(self):
        val = self.i2c.readfrom_mem(self.address, 0, 4)
        temperature = f"{val[2]}.{val[3]} °C"
        humidity = f"{val[0]}.{val[1]}%"
        return temperature, humidity
