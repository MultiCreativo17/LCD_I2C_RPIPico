from machine import Pin, I2C

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

print("I2C Address    :"+hex(i2c.scan()[0]).upper())