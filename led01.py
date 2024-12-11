from machine import Pin
import time

# Definice pinů pro LED diody a tlačítko
led_pins = [Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT)]
button_pin = Pin(4, Pin.IN, Pin.PULL_DOWN)

# Funkce pro zapnutí LED diody
def turn_on_led(led):
    led.value(1)

# Funkce pro vypnutí LED diody
def turn_off_led(led):
    led.value(0)

# Hlavní smyčka
running = True
while True:
    if button_pin.value() == 1:  # Pokud je tlačítko stisknuto
        running = not running  # Přepnutí stavu běhu
        time.sleep(0.5)  # Debouncing tlačítka

    if running:
        # Běžící světlo dopředu
        for led in led_pins:
            turn_on_led(led)
            time.sleep(0.1)
            turn_off_led(led)
        
        # Běžící světlo zpět
        for led in reversed(led_pins):
            turn_on_led(led)
            time.sleep(0.1)
            turn_off_led(led)
    else:
        # Vypnutí všech LED diod, pokud není běh aktivní
        for led in led_pins:
            turn_off_led(led)

