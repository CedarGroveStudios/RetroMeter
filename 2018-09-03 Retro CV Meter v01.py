# 2018-09-03 Retro CV Meter v01.py
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
def inertia_move(v=0, target_v=0, rate=1, increment=1):
    # This helper moves the output voltage from the current value to the
    # target value at the specified rate (seconds per input volt). Output
    # resolution is controlled by increment and is measured in volts per step.

    led.value = True  # turn on activity indicator

    # limit the voltage increment to a reasonable value
    if increment <= 0:
        increment = 0.001  # minimum increment of 1mV/step
    if increment > 5:
        increment = 5      # maximum increment of 5V/step

    # This is the proportional movement control. It determines the
    # number of steps needed to move from the current value to the target
    # value based on the increment value.
    #
    delta_v = target_v - v
    steps = delta_v / increment
    if steps == 0:  # have to take at least one step
        steps = 1

    # This portion of code steps from the current value to the target value
    # over time specified by the rate.
    #
    # This is where input voltage is scaled before sending to the DAC output.
    # To change the meter's full-scale voltage, modify the 2nd and 3rd
    # map_range parameters. For example, to change to +/-5V:
    #        meter_pin.value = int(map_range(v, -5, +5, 0, 65535))
    #
    for i in range(1+int(abs(steps))):
        meter_pin.value = int(map_range(v, -10, +10, 0, 65535))
        time.sleep(rate * increment)
        v = v + ((steps / abs(steps)) * increment)
    v = target_v
    led.value = False  # clear activity indicator
    return (v)  # return new v value

# ### Set Initial Parameters ###
#
# The following parameters set rate, increment, and outut hold. You should
# experiment with these parameters to get the right "feel" for the particular
# application and analog meter.
#
move_rate = 0.050    # seconds to move 1 volt on a -10 to +10 volt scale
move_inc = 0.050     # smallest movement representing input voltage
output_hold = 0  # number of seconds to hold position before repositioning

print("2018-09-03 Retro CV Meter v01.py")
print("GC.mem_free: ", gc.mem_free())
print("CPU.freqency: ", microcontroller.cpu.frequency)
print("CPU.temperature: ", microcontroller.cpu.temperature)
# print("Battery voltage: ", AnalogIn(board.Ax) )  # not used

# Slowly center (zero) the meter's output before reading the input voltage.
# This should take about one second to move the needle to the center.
meter_out_volt = inertia_move(-10, 0, 0.200, 0.050)
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

    # Send the scaled input voltage to the analog meter via the inertia_move
    # helper to the Trinket DAC output.
    meter_out_volt = inertia_move(meter_out_volt, cv_input_volt, move_rate, move_inc)

    time.sleep(output_hold)  # Hold the output voltage for a while.
