"""!
@file led.py
This file contains code which does the tasks for the first checkpoint of lab1, a function to set up the LED circuit, a function to
control LED brightness, and a main file to run the LED sequence.

TODO:

@author Lab05 Group05
@date   6-Feb-2024
"""

import time

def led_setup():
    """!

    This function sets up the pins and timers for the LED sequence
    
    """
    
    pyb.Timer.PWM_INVERTED
    pinPA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    tim2 = pyb.Timer(2, freq=1000)
    ch1 = tim2.channel (1, pyb.Timer.PWM, pin=pinPA0)
    return ch1

def led_brightness(n):
    """!

    This function sets up the input function for brightness for the LED
    
    @param n Input the LED brightness level
    
    """
    
    ch1 = led_setup()
    ch1.pulse_width_percent (n)

if __name__ == "__main__":
    led_setup()
    n=0
    f=1
    while f == 1:
        # dim LED for 5 seconds
        for _ in range(100):
            led_brightness(n)
            # Increment n
            n += 1
            time.sleep(0.05)
        print("done100")
        # brighten LED for 5 seconds
        for _ in range(100):
            led_brightness(n)
            # Increment n
            n -= 1
            time.sleep(0.05)
        print("done")