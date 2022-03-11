import utime

import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x3F
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

def test_main():
    #Prueba funcional
    print("Ejecutando prueba de LCD")
    i2c = I2C(0, sda=machine.Pin(8), scl=machine.Pin(9), freq=200000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
    lcd.putstr("Funciona")
    utime.sleep(2)
    lcd.clear()
    count = 0
    while True:
        lcd.clear()
        lcd.move_to(1,0)
        lcd.putstr("Multi Creativo")
        lcd.move_to(0,1)
        lcd.putstr("Expade tu mente")
        if count % 10 == 0:
            print("Muestra cursor")
            lcd.show_cursor()
        if count % 10 == 1:
            print("Oculta cursor")
            lcd.hide_cursor()
        if count % 10 == 2:
            print("Parpadea el cursor lleno")
            lcd.blink_cursor_on()
        if count % 10 == 3:
            print("Apaga cursor lleno")
            lcd.blink_cursor_off()                    
        if count % 10 == 4:
            print("Apaga luz de fondo")
            lcd.backlight_off()
        if count % 10 == 5:
            print("Enciende luz de fondo")
            lcd.backlight_on()
        if count % 10 == 6:
            print("Oculta texto visible")
            lcd.display_off()
        if count % 10 == 7:
            print("Muestra texto visible")
            lcd.display_on()
        if count % 10 == 8:
            print("Rellena de caracteres")
            lcd.clear()
            string = ""
            for x in range(32, 32+I2C_NUM_ROWS*I2C_NUM_COLS):
                string += chr(x)
            lcd.putstr(string)
        count += 1
        utime.sleep(2)

#if __name__ == "__main__":
test_main()