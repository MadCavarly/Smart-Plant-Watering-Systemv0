from machine import I2C
from sh1106 import SH1106_I2C

class OLEDDisplay:
    def __init__(self, width, height, pins, address):
        self.i2c = I2C(0, scl=pins[0], sda=pins[1], freq=100000)
        self.oled = SH1106_I2C(width, height, self.i2c, addr=address, rotate=180)
        self.oled.sleep(False)
        self.oled.contrast(50)

    def show_message(self, message):
        self.oled.text(message, x=0, y=0)
        self.oled.show()
