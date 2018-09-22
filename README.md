# RetroMeter
A utility board that converts a +/-10V CV signal to a current level compatible with a retro analog ammeter. USB or 3 to 6V battery powered (no internal battery charger). From the collaborative project with John Park’s Workshop.

![Retro CV Meter and Trinket M0 Rendering](https://github.com/CedarGroveStudios/RetroMeter/blob/master/retro%20meter%20v02.png)

The Retro CV Meter board accepts a -10 to +10 volt signal and through an analog op-amp, translates it into a +3.3 to 0 volt signal connected to the Atafruit Trinket M0's A1 analog input pin (physical pin D2). The A0~ DAC output pin (physical pin D1) provides current output through a 2K-ohm resistor to the analog meter connection. The maximum DAC value (65535) produces 1.5mA to the attached meter.

The CircuitPython code reads the input voltage and adjusts the DAC output for the scale for the meter. The ``inertia_move`` helper integrates the incoming signal then sends the scaled and smoothed voltage to the on-board meter resistor to convert the voltage to current compabile with the analog meter. The integration routine protects the meter movement from sudden voltage changes.

The most recent version of the code reads a meter scale input from a potentiometer attached to pin A2. The D3 pin provides a PWM output proportional to the absolute value of the input voltage within the specified range.

![Retro CV Meter and Trinket M0 Glamour Rendering](https://github.com/CedarGroveStudios/RetroMeter/blob/master/retro%20meter%20v02%20glamour.png)
