# 2018-08-31 Retro CV Meter v00.py
# TrinketM0-based CV monitor with analog current meter output
# 2018 John Park's Workshop, Cedar Grove Studios
#
# The Retro CV Meter board accepts a -10 to +10 volt signal and
# translates that into a +3.3 to 0 volt signal connected to the
# TrinketM0's A1 analog input pin (physical pin D2). The A0~ DAC
# output pin (physical pin D1) provides current output through
# a 2K-ohm resistor to the analog meter connection. The maximum
# DAC value (65535) produces 1.5mA to the meter.
#
# This code reads the input voltage and adjusts the scale for the
# meter. The inertia_move helper integrates and sends the scaled 
# voltage to the meter resistor. Integration protects the meter
# movement from sudden voltage changes.

# ### Setup ###
import digitalio
from analogio import AnalogIn, AnalogOut
import board
import time
from simpleio import map_range
import adafruit_dotstar as dotstar  # Trinket

import microcontroller  # for checking CPU temperature
import gc  # for checking memory capacity

# set up CV input and meter output
cv_pin = AnalogIn(board.A1)
meter_pin = AnalogOut(board.A0)

# set up red LED activity indicator
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# set up GPIO for polarity indicators
neg_led = digitalio.DigitalInOut(board.D0)
neg_led.direction = digitalio.Direction.OUTPUT
zero_led = digitalio.DigitalInOut(board.D3)
zero_led.direction = digitalio.Direction.OUTPUT
pos_led = digitalio.DigitalInOut(board.D4)
pos_led.direction = digitalio.Direction.OUTPUT

# set up DotStar as polarity indicator
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1)
dot[0] = [64, 64, 64]  # wht = startup
time.sleep(0.1)

# ## Dictionaries and Lists ##

# ## Helpers ##
def inertia_move(v=0, target_v=0, rate=1, increment=1):
    # move output from current voltage to target voltage at the
    # specified rate (seconds per input volt for the -/+10 input range)
    # increment is number of volts per step (output resolution)

    led.value = True  # activity indicator
    
    if increment <= 0:     # limit the size of the voltage increment
        increment = 0.001  # minimum increment of 1mV/step
    if increment > 5: 
        increment = 5      # maximum increment of 5V/step

    # proportional movement control; determine number of needed steps
    delta_v = target_v - v
    steps = delta_v / increment
    if steps == 0:  # have to take at least one step
        steps = 1

    # step from current position to target position over time
    # this is where input voltage is scaled to DAC output
    for i in range(1+int(abs(steps))):
        meter_pin.value = int(map_range(v, -10, +10, 0, 65535))
        time.sleep(rate * increment)
        v = v + ((steps / abs(steps)) * increment)
    v = target_v
    led.value = False  # clear activity indicator
    return (v)  # return new v value

# ### Set Initial Parameters ###
# experiment with these parameters to get the right "feel" for the meter
move_rate = 0.100    # seconds to move 1 volt on a -10 to +10 volt scale
move_inc = 0.500     # smallest movement representing input voltage
output_hold = 0.100  # number of seconds to hold position before repositioning

print("2018-08-31 Retro CV Meter v00.py")
print("GC.mem_free: ", gc.mem_free())
print("CPU.freqency: ", microcontroller.cpu.frequency)
print("CPU.temperature: ", microcontroller.cpu.temperature)
# print("Battery voltage: ", AnalogIn(board.Ax) )

# center the output
meter_out_volt = inertia_move(-10, 0, move_rate, move_inc)
time.sleep(output_hold)  # hold the current output value

# ### Main Loop ###
while True:
    cv_input_volt = map_range(cv_pin.value, 0, 65535, +10, -10)
    
    # show input voltage polarity on the DotStar indicator
    if cv_input_volt > +1.0:    # 1V noise threshold
        dot[0] = (0, 255, 0)    # grn = positive
        neg_led.value = False
        zero_led.value = False
        pos_led.value = True
    elif cv_input_volt < -1.0:  #1V noise threshold
        dot[0] = (255, 0, 0)    # red = negative
        neg_led.value = True
        zero_led.value = False
        pos_led.value = False
    else: 
        dot[0] = (0, 0, 255)    # blu = zero
        neg_led.value = False
        zero_led.value = True
        pos_led.value = False

    # send the scaled input voltage to the meter output
    meter_out_volt = inertia_move(meter_out_volt, cv_input_volt, move_rate, move_inc)

    time.sleep(output_hold)  # hold output voltage for a while

    