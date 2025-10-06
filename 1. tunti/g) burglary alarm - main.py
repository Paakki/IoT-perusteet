from machine import Pin
import time

# PIR motion sensor connected to GPIO15
pir = Pin(28, Pin.IN)
led = Pin("LED", Pin.OUT)  # onboard LED for visual feedback

print("Burglary alarm ready — waiting for motion...")

while True:
    if pir.value() == 1:
        print("Movement detected! Possible intruder!")
        led.on()
        time.sleep(2)     # keep LED on for 2 seconds
        led.off()
    else:
        led.off()
    time.sleep(0.1)