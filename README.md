# RetroMeter
A utility board that converts a +/-10V CV signal to a current level compatible with a retro analog ammeter. LiPo battery powered (no internal charger). From the collaborative project with John Park’s Workshop. (retro meter 2018-08-20 PCB v02a)

The Retro CV Meter board accepts a -10 to +10 volt signal and translates that into a +3.3 to 0 volt signal connected to the TrinketM0's A1 analog input pin (physical pin D2). The A0~ DAC output pin (physical pin D1) provides current output through a 2K-ohm resistor to the analog meter connection. The maximum DAC value (65535) produces 1.5mA to the attached meter.

The CircuitPython code reads the input voltage and adjusts the scale for the meter. The inertia_move helper integrates and sends the scaled voltage to the meter resistor. An integration routine in the code protects the meter movement from sudden voltage changes.

