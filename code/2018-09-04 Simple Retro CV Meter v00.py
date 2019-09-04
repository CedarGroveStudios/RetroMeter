# 2018-09-04 Simple Retro CV Meter v00.py
# TrinketM0-based CV monitor with analog current meter output
# (c) 2018 John Park's Workshop with Cedar Grove Studios
#
# The Retro CV Meter board accepts a -10 to +10 volt CV signal and outputs
# a 0 to 1.5mA signal to a connected analog ammeter. The PCB attenuates and
# shifts the incoming signal, translating it into a +3.3 to 0 volt signal
# compatible with the TrinketM0's A1 analog input pin (physical pin D2).
#
# The Trinket's A0~ DAC output pin (physical pin D1) provides a voltage that
# is converted to a current through a 2K-ohm resistor to the analog ammeter.
# The maximum 16-bit DAC value (65535) produces 1.5mA to deflect the meter
# to full-scale.
#
# This code reads the input voltage and adjusts the scale for the
# meter.

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

# set up red LED activity indicator (when moving the meter needle)
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# set up GPIO for polarity indicators
neg_led = digitalio.DigitalInOut(board.D0)   # red LED
neg_led.direction = digitalio.Direction.OUTPUT
zero_led = digitalio.DigitalInOut(board.D3)  # blue LED
zero_led.direction = digitalio.Direction.OUTPUT
pos_led = digitalio.DigitalInOut(board.D4)   # green LED
pos_led.direction = digitalio.Direction.OUTPUT

# set up DotStar as polarity indicator; low brightness
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1)
dot[0] = [64, 64, 64]  # display white during startup
time.sleep(0.1)

# ## Dictionaries and Lists ##
# (none)

# ## Helpers ##
# (none)

# ### Set Initial Parameters ###
# (none)

print("2018-09-04 Simple Retro CV Meter v00.py")
print("GC.mem_free: ", gc.mem_free())
print("CPU.freqency: ", microcontroller.cpu.frequency)
print("CPU.temperature: ", microcontroller.cpu.temperature)
# print("Battery voltage: ", AnalogIn(board.Ax) )  # not used

# Gradually center (zero) the meter's output before reading the input voltage.
for i in range(0, 32768):
    meter_pin.value = i
time.sleep(0.500)  # hold at center scale for 0.500 seconds

# ### Main Loop ###
while True:
    # Read the CV input and map to a +/-10V value.
    # Because of the input op-amp's signal inversion and fixed gain, a 0V
    # input to the Trinket's analog pin correlates to a CV input value of +10V;
    # a 3.3V input maps to a value of -10V. DO NOT adjust these values.
    cv_input_volt = map_range(cv_pin.value, 0, 65535, +10, -10)

    # Show the input voltage polarity on the DotStar indicator.
    if cv_input_volt > +1.0:    # 1V noise threshold
        dot[0] = (0, 255, 0)    # grn = positive
        neg_led.value = False
        zero_led.value = False
        pos_led.value = True
    elif cv_input_volt < -1.0:  # 1V noise threshold
        dot[0] = (255, 0, 0)    # red = negative
        neg_led.value = True
        zero_led.value = False
        pos_led.value = False
    else:
        dot[0] = (0, 0, 255)    # blu = zero
        neg_led.value = False
        zero_led.value = True
        pos_led.value = False

    # Scale the input voltage and send to the meter via the Trinket DAC output.
    # To change the meter's full-scale voltage, modify the 2nd and 3rd
    # map_range parameters. For example, to change to +/-5V:
    #        meter_pin.value = int(map_range(cv_input_volt, -5, +5, 0, 65535))
    meter_pin.value = int(map_range(cv_input_volt, -10, +10, 0, 65535))
