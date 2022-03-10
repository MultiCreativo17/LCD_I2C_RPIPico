# LCD_I2C_RPIPico
Librerías para LCD I2C con raspberry pi pico


En este repositorio tendrás acceso a las librerías para utilizar la raspberri pi pico con la LCD por medio de I2C y el adaptador PFC8574AT

Para la conexión con la raspberry se utilizo la siguiente configuración

LCD I2C             RPI PICO

GND   ---------->    GND

VCC   ---------->    VBUS

SDA   ---------->    GP8

SCL   ---------->    GP9

Se añaden dos archivos .py los cuales son útiles para la conexión con la LCD  (lcd_api.py y pico_i2c_lcd.py) y además se pone un archivo main.py para colocarlo como prueba.

Es de suma importancia conocer la dirección de nuestra LCD. por lo que se debe utilizar el siguiente fragmento de código

from machine import Pin, I2C

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

print("I2C Address    :"+hex(i2c.scan()[0]).upper())
