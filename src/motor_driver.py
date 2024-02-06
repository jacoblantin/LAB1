"""!
@file motor_driver.py
This file contains code which does the tasks for the second checkpoint of lab1. The class below contains an init function to initialize
the pins and timers for use in the motor driver and contains a method to set the duty cycle for the motor. 

TODO:

@author Lab05 Group05
@date   6-Feb-2024
"""

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__(self):
        """!

        Initializes pins and timers for use in motor driver.
        
        """
        
        pyb.Timer.PWM
    
        pinIN1A = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
        tim3 = pyb.Timer(3, freq=1000)
        ch1 = tim3.channel (1, pyb.Timer.PWM, pin=pinIN1A)
    
        pinIN2A = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
        ch2 = tim3.channel (2, pyb.Timer.PWM, pin=pinIN2A)
    
        pinENA = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
        self.ch1 = ch1
        self.ch2 = ch2
        self.pinENA = pinENA
        
        print("Creating a motor driver")
        
    def set_duty_cycle(self, level):
        """!

        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
             
        @param level A signed integer holding the duty cycle of the motor.
        
        """

        ch1 = self.ch1
        ch2 = self.ch2
        pinENA = self.pinENA
        pinENA.high()
        if level > 0: 
            ch1.pulse_width_percent (level)
            ch2.pulse_width_percent (0)
        else:
            ch1.pulse_width_percent (0)
            ch2.pulse_width_percent (abs(level))
            
        print (f"Setting duty cycle to {level}")
        

if __name__ == "__main__":
    moe = MotorDriver ()
    
    # the following command sets the level for the motor driver
    moe.set_duty_cycle (50)
