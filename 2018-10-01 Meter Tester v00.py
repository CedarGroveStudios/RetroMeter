# 2018-10-01 Meter Tester v00.py
# TrinketM0-based analog meter tester utilizing the Retro CV Meter PCB
# (c) 2018 John Park's Workshop with Cedar Grove Studios
#
# The Meter Tester measures and displays analog meter parameters. The
#   meter voltage is monitored by a probe connection from analog input A4.
#   Up to +1.65mA current is output from the Retro CV Meter board to the
#   meter under test. The test potentiometer (attached to analog
#   input A2) is manually adjusted from zero to a level that causes the
#   meter to deflect to full-scale. The serial output continuously displays
#   meter parameters.
#
# The Trinket's A0~ DAC output pin (physical pin D1) provides a voltage that
#   is converted to a current through a 2K-ohm resistor to the analog ammeter.
#   The maximum 16-bit DAC value (65535) produces 1.65mA to deflect the meter
#   to full-scale.
#

import digitalio
import pulseio
from analogio import AnalogIn, AnalogOut
import board
import time
from simpleio import map_range
import adafruit_dotstar as dotstar  # Trinket

import microcontroller  # for checking CPU temperature
import gc  # for checking memory capacity

# ### Setup ###
# analog inputs and meter output
probe_pin = AnalogIn(board.A4)
test_pin = AnalogIn(board.A2)
meter_pin = AnalogOut(board.A0)
meter_pin.value = 0  # Position the meter to zero

# on-board activity indicator (when moving the meter needle)
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# GPIO for pwm indicators
# neg_led = pulseio.PWMOut(board.D3)  # negative red LED
# pos_led = pulseio.PWMOut(board.D4)  # positive green LED
amber_led = pulseio.PWMOut(board.D3)  # absolute value amber LED

amber_led.duty_cycle = 65535  # turn on amber LED for general illumination

# on-board DotStar; low brightness
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1)
dot[0] = [64, 0, 0]  # display red
time.sleep(0.1)

# ### Dictionaries and Lists ###

# ### Helpers ###

# ### Set Initial Parameters ###
output_hold = 1  # number of seconds to hold measurement display
dac_resist = 2000 # the PCB's series meter resistor value in ohms
test_volt = 0
probe_volt = 0

print("2018-10-01 Meter Tester v00.py")
print("GC.mem_free: ", gc.mem_free())
print("CPU.freqency: ", microcontroller.cpu.frequency)
print("CPU.temperature: ", "%0.1f" % microcontroller.cpu.temperature)
# print("Battery voltage: ", AnalogIn(board.Ax) )  # not used

print("--- Analog Meter Test ---")
print("Starting from zero, adjust test voltage to deflect the meter to full-scale")

t0 = time.monotonic()

# ### Main Loop ###
while True:
    meter_pin.value = test_pin.value

    if time.monotonic() > t0 + output_hold:
        test_volt = int(((test_volt + map_range(test_pin.value, 0, 65535, 0, 3.3)) / 2)*1000)/1000
        probe_volt = int(((probe_volt + map_range(probe_pin.value, 0, 65535, 0, 3.3)) / 2)*1000)/1000
        
        if probe_volt > test_volt: probe_volt = test_volt
        meter_current = (test_volt - probe_volt) / dac_resist
    
        if (test_volt - probe_volt) != 0:
            meter_resist = (probe_volt * dac_resist) / (test_volt - probe_volt)
        else: meter_resist = 9999999

        meter_volt = probe_volt
        
        print("------")
        if test_volt == 0:
            print("* Increase test voltage to deflect meter to full scale *")
        elif test_volt == probe_volt: print("* Meter open or less than test range ( < 3uA) *")
        elif probe_volt == 0: print("* Meter shorted or greater than test range ( > 1.6mA) *")
    
        print("Meter current (mA)= ", "%0.3f" % (meter_current * 1000))
        if meter_resist != 9999999:
            print("Meter resistance (ohms)= ", "%0.1f" % meter_resist)
        else:
            print("Meter resistance (ohms)= *infinity*")
        print("Meter voltage (mV): ", "%0.1f" % (meter_volt * 1000))
        print(" ")
        t0 = time.monotonic()

    time.sleep(0.010)  # Hold the output voltage for a while.