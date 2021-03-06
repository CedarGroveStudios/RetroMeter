EESchema Schematic File Version 4
LIBS:2018-08-20 analog Trinket sub-cache
EELAYER 26 0
EELAYER END
$Descr USLetter 11000 8500
encoding utf-8
Sheet 1 1
Title "Retro CV Meter Analog Trinket Substitute Sub-Module"
Date "2018-10-06"
Rev "v02"
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Notes 7425 4300 0    70   ~ 0
RETRO CV METER\nANALOG TRINKET SUBSTITUTE
$Comp
L power:GND #PWR05
U 1 1 5B76E763
P 4300 6875
F 0 "#PWR05" H 4300 6625 50  0001 C CNN
F 1 "GND" H 4305 6702 50  0000 C CNN
F 2 "" H 4300 6875 50  0001 C CNN
F 3 "" H 4300 6875 50  0001 C CNN
	1    4300 6875
	1    0    0    -1  
$EndComp
Connection ~ 4750 2550
Text Notes 4475 2875 0    50   ~ 0
gain = 1.0\ninverter stage
Text Notes 3225 7125 0    50   ~ 0
Power Management
$Comp
L device:R R1
U 1 1 5B7B9582
P 3500 2450
F 0 "R1" V 3293 2450 50  0000 C CNN
F 1 "10K" V 3384 2450 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3430 2450 50  0001 C CNN
F 3 "" H 3500 2450 50  0001 C CNN
	1    3500 2450
	0    1    1    0   
$EndComp
$Comp
L device:R R2
U 1 1 5B7B9643
P 4300 1950
F 0 "R2" V 4093 1950 50  0000 C CNN
F 1 "10K" V 4184 1950 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 4230 1950 50  0001 C CNN
F 3 "" H 4300 1950 50  0001 C CNN
	1    4300 1950
	0    1    1    0   
$EndComp
Wire Wire Line
	4150 1950 3850 1950
Wire Wire Line
	3850 2450 4050 2450
Wire Wire Line
	3650 2450 3850 2450
Connection ~ 3850 2450
$Comp
L power:+3V3 #PWR09
U 1 1 5B7D8386
P 4900 5975
F 0 "#PWR09" H 4900 5825 50  0001 C CNN
F 1 "+3V3" H 4915 6148 50  0000 C CNN
F 2 "" H 4900 5975 50  0001 C CNN
F 3 "" H 4900 5975 50  0001 C CNN
	1    4900 5975
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR06
U 1 1 5B7F56F9
P 4250 3325
F 0 "#PWR06" H 4250 3075 50  0001 C CNN
F 1 "GND" H 4255 3152 50  0000 C CNN
F 2 "" H 4250 3325 50  0001 C CNN
F 3 "" H 4250 3325 50  0001 C CNN
	1    4250 3325
	1    0    0    -1  
$EndComp
$Comp
L power:+BATT #PWR03
U 1 1 5B823DF6
P 3700 5975
F 0 "#PWR03" H 3700 5825 50  0001 C CNN
F 1 "+BATT" H 3715 6148 50  0000 C CNN
F 2 "" H 3700 5975 50  0001 C CNN
F 3 "" H 3700 5975 50  0001 C CNN
	1    3700 5975
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 2550 4750 2550
Wire Wire Line
	4750 1950 4450 1950
Wire Wire Line
	4750 1950 4750 2550
Wire Wire Line
	3850 1950 3850 2450
Wire Wire Line
	3350 2450 3050 2450
Wire Wire Line
	4750 2550 5200 2550
Text Label 3125 2450 0    50   ~ 0
A1
Text Label 5000 2550 0    50   ~ 0
A0~~
$Comp
L Adafruit:Trinket_M0 U3
U 1 1 5B8AF4A6
P 4275 4600
F 0 "U3" H 4275 5065 50  0000 C CNN
F 1 "Trinket_M0" H 4275 4974 50  0000 C CNN
F 2 "Adafruit:Trinket_M0_no_holes" H 4275 4950 50  0001 C CNN
F 3 "" H 4275 4950 50  0001 C CNN
	1    4275 4600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3775 4400 3625 4400
Wire Wire Line
	3625 4400 3625 4175
Wire Wire Line
	3775 4500 3625 4500
Wire Wire Line
	3625 4500 3625 5000
Wire Wire Line
	4775 4600 5100 4600
Wire Wire Line
	4775 4700 5100 4700
Wire Wire Line
	4775 4800 4900 4800
Wire Wire Line
	4900 4800 4900 4500
$Comp
L power:GND #PWR02
U 1 1 5B8C4AC3
P 3625 5000
F 0 "#PWR02" H 3625 4750 50  0001 C CNN
F 1 "GND" H 3630 4827 50  0000 C CNN
F 2 "" H 3625 5000 50  0001 C CNN
F 3 "" H 3625 5000 50  0001 C CNN
	1    3625 5000
	1    0    0    -1  
$EndComp
$Comp
L power:+BATT #PWR01
U 1 1 5B8C4B34
P 3625 4175
F 0 "#PWR01" H 3625 4025 50  0001 C CNN
F 1 "+BATT" H 3640 4348 50  0000 C CNN
F 2 "" H 3625 4175 50  0001 C CNN
F 3 "" H 3625 4175 50  0001 C CNN
	1    3625 4175
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR08
U 1 1 5B8C4BA5
P 4900 4200
F 0 "#PWR08" H 4900 4050 50  0001 C CNN
F 1 "+3V3" H 4915 4373 50  0000 C CNN
F 2 "" H 4900 4200 50  0001 C CNN
F 3 "" H 4900 4200 50  0001 C CNN
	1    4900 4200
	1    0    0    -1  
$EndComp
Text Label 5000 4700 0    50   ~ 0
A1
Text Label 4975 4600 0    50   ~ 0
A0~~
NoConn ~ 4775 4400
NoConn ~ 3775 4800
Wire Wire Line
	3775 4600 3700 4600
Wire Wire Line
	3700 4600 3700 4700
Wire Wire Line
	3700 4975 4900 4975
Wire Wire Line
	4900 4975 4900 4800
Connection ~ 4900 4800
Wire Wire Line
	3775 4700 3700 4700
Connection ~ 3700 4700
Wire Wire Line
	3700 4700 3700 4975
Wire Wire Line
	4775 4500 4900 4500
Connection ~ 4900 4500
Wire Wire Line
	4900 4500 4900 4200
$Comp
L device:C_Small C1
U 1 1 5B7BB862
P 4300 1600
F 0 "C1" V 4071 1600 50  0000 C CNN
F 1 "10uF" V 4162 1600 50  0000 C CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 4300 1600 50  0001 C CNN
F 3 "" H 4300 1600 50  0001 C CNN
	1    4300 1600
	0    1    1    0   
$EndComp
$Comp
L regul:LT1761-5 U2
U 1 1 5B7BCC66
P 4300 6225
F 0 "U2" H 4300 6592 50  0000 C CNN
F 1 "MIC5225-3V" H 4300 6501 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-23-5_HandSoldering" H 4350 5975 50  0001 L CNN
F 3 "http://cds.linear.com/docs/en/datasheet/1761sff.pdf" H 4300 6225 50  0001 C CNN
	1    4300 6225
	1    0    0    -1  
$EndComp
NoConn ~ 4700 6225
$Comp
L device:CP1_Small C3
U 1 1 5B7BDFF1
P 4900 6525
F 0 "C3" H 4991 6571 50  0000 L CNN
F 1 "10uF" H 4991 6480 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 4900 6525 50  0001 C CNN
F 3 "" H 4900 6525 50  0001 C CNN
	1    4900 6525
	1    0    0    -1  
$EndComp
$Comp
L device:CP1_Small C2
U 1 1 5B7BE05B
P 3700 6525
F 0 "C2" H 3500 6600 50  0000 L CNN
F 1 "10uF" H 3425 6525 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3700 6525 50  0001 C CNN
F 3 "" H 3700 6525 50  0001 C CNN
	1    3700 6525
	1    0    0    -1  
$EndComp
Wire Wire Line
	4900 5975 4900 6125
Wire Wire Line
	4900 6625 4900 6775
Wire Wire Line
	4900 6775 4300 6775
Wire Wire Line
	4300 6775 4300 6875
Wire Wire Line
	4300 6775 4300 6525
Connection ~ 4300 6775
Wire Wire Line
	4700 6125 4900 6125
Connection ~ 4900 6125
Wire Wire Line
	4900 6125 4900 6425
Wire Wire Line
	4750 1950 4750 1600
Wire Wire Line
	4750 1600 4400 1600
Connection ~ 4750 1950
Wire Wire Line
	4200 1600 3850 1600
Wire Wire Line
	3850 1600 3850 1950
Connection ~ 3850 1950
Wire Wire Line
	4300 6775 3700 6775
Wire Wire Line
	3700 6775 3700 6625
Wire Wire Line
	3700 6425 3700 6325
Wire Wire Line
	3900 6125 3700 6125
Connection ~ 3700 6125
Wire Wire Line
	3700 6125 3700 5975
Wire Wire Line
	3900 6325 3700 6325
Connection ~ 3700 6325
Wire Wire Line
	3700 6325 3700 6125
$Comp
L device:R R4
U 1 1 5BB9CF76
P 3925 3225
F 0 "R4" V 3718 3225 50  0000 C CNN
F 1 "100K" V 3809 3225 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3855 3225 50  0001 C CNN
F 3 "" H 3925 3225 50  0001 C CNN
	1    3925 3225
	0    1    1    0   
$EndComp
$Comp
L linear:TLV2461 U1
U 1 1 5BB9F9B0
P 4350 2550
F 0 "U1" H 4375 2775 50  0000 C CNN
F 1 "TLV2461" H 4475 2700 50  0000 C CNN
F 2 "Housings_SOIC:SOIC-8_3.9x4.9mm_Pitch1.27mm" H 4400 2600 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm741.pdf" H 4500 2700 50  0001 C CNN
	1    4350 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4250 2400 4250 2325
$Comp
L power:+3V3 #PWR0101
U 1 1 5BBA1BCA
P 4250 2325
F 0 "#PWR0101" H 4250 2175 50  0001 C CNN
F 1 "+3V3" H 4265 2498 50  0000 C CNN
F 2 "" H 4250 2325 50  0001 C CNN
F 3 "" H 4250 2325 50  0001 C CNN
	1    4250 2325
	1    0    0    -1  
$EndComp
$Comp
L device:R R3
U 1 1 5BBA3DDC
P 3525 3225
F 0 "R3" V 3318 3225 50  0000 C CNN
F 1 "100K" V 3409 3225 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3455 3225 50  0001 C CNN
F 3 "" H 3525 3225 50  0001 C CNN
	1    3525 3225
	0    1    1    0   
$EndComp
$Comp
L power:+3V3 #PWR0102
U 1 1 5BBA3E56
P 3275 3000
F 0 "#PWR0102" H 3275 2850 50  0001 C CNN
F 1 "+3V3" H 3290 3173 50  0000 C CNN
F 2 "" H 3275 3000 50  0001 C CNN
F 3 "" H 3275 3000 50  0001 C CNN
	1    3275 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	3275 3225 3375 3225
Wire Wire Line
	3675 3225 3725 3225
Wire Wire Line
	4250 3225 4250 3325
Connection ~ 4250 3225
Connection ~ 3725 3225
Wire Wire Line
	3725 3225 3775 3225
Text Notes 3550 3400 0    50   ~ 0
+1.650V
Wire Wire Line
	3725 2650 4050 2650
Wire Wire Line
	4075 3225 4250 3225
Wire Wire Line
	4250 2700 4250 3225
Wire Wire Line
	3725 2650 3725 3225
Wire Wire Line
	3275 3000 3275 3225
$EndSCHEMATC
