EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "FlightBridge PCB"
Date "2021-03-30"
Rev "1"
Comp "METR4810 Team 8"
Comment1 "Connor Raggatt"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Notes 1600 1450 0    50   ~ 0
To/from Raspberry Pi\n
Text Notes 5400 700  0    50   ~ 0
Rad-hard Supervisor IC\n
Text Notes 9200 1350 0    50   ~ 0
To/From Flight Controller\n
$Comp
L Device:Crystal Y1
U 1 1 606826B2
P 4900 1750
F 0 "Y1" V 4854 1881 50  0000 L CNN
F 1 "Crystal" V 4945 1881 50  0000 L CNN
F 2 "Crystal:Crystal_SMD_HC49-SD" H 4900 1750 50  0001 C CNN
F 3 "~" H 4900 1750 50  0001 C CNN
	1    4900 1750
	0    1    1    0   
$EndComp
$Comp
L Device:C C1
U 1 1 60685F65
P 4550 1600
F 0 "C1" V 4298 1600 50  0000 C CNN
F 1 "22pF" V 4389 1600 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 4588 1450 50  0001 C CNN
F 3 "~" H 4550 1600 50  0001 C CNN
	1    4550 1600
	0    1    1    0   
$EndComp
$Comp
L Device:C C2
U 1 1 606881D4
P 4550 1900
F 0 "C2" V 4300 1900 50  0000 C CNN
F 1 "22pF" V 4400 1900 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 4588 1750 50  0001 C CNN
F 3 "~" H 4550 1900 50  0001 C CNN
	1    4550 1900
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4700 1600 4900 1600
Wire Wire Line
	4900 1900 4700 1900
Wire Wire Line
	4900 1900 5300 1900
Wire Wire Line
	5300 1900 5300 1850
Connection ~ 4900 1900
Wire Wire Line
	5300 1650 5300 1600
Wire Wire Line
	5300 1600 4900 1600
Connection ~ 4900 1600
Wire Wire Line
	4400 1600 4400 1750
Wire Wire Line
	4200 1750 4400 1750
Connection ~ 4400 1750
Wire Wire Line
	4400 1750 4400 1900
$Comp
L power:GND #PWR0101
U 1 1 6069D1AA
P 4200 1750
F 0 "#PWR0101" H 4200 1500 50  0001 C CNN
F 1 "GND" H 4205 1577 50  0000 C CNN
F 2 "" H 4200 1750 50  0001 C CNN
F 3 "" H 4200 1750 50  0001 C CNN
	1    4200 1750
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 2100 2050 2050
Wire Wire Line
	2050 2050 2000 2050
Wire Wire Line
	1950 2050 1950 2100
Wire Wire Line
	2000 2050 2000 2000
Connection ~ 2000 2050
Wire Wire Line
	2000 2050 1950 2050
Wire Wire Line
	1750 4700 1750 4800
Wire Wire Line
	1750 4800 1850 4800
Wire Wire Line
	2450 4800 2450 4700
Wire Wire Line
	1850 4700 1850 4800
Connection ~ 1850 4800
Wire Wire Line
	1850 4800 1950 4800
Wire Wire Line
	1950 4700 1950 4800
Connection ~ 1950 4800
Wire Wire Line
	1950 4800 2050 4800
Wire Wire Line
	2050 4700 2050 4800
Connection ~ 2050 4800
Wire Wire Line
	2150 4700 2150 4800
Connection ~ 2150 4800
Wire Wire Line
	2150 4800 2250 4800
Wire Wire Line
	2250 4700 2250 4800
Connection ~ 2250 4800
Wire Wire Line
	2250 4800 2350 4800
Wire Wire Line
	2350 4700 2350 4800
Connection ~ 2350 4800
Wire Wire Line
	2350 4800 2450 4800
$Comp
L MCU_Microchip_ATmega:ATmega128A-AU U1
U 1 1 6062B161
P 5900 3150
F 0 "U1" H 5900 850 50  0000 C CNN
F 1 "ATmega128A-AU" H 5900 750 50  0000 C CNN
F 2 "Package_QFP:TQFP-64_14x14mm_P0.8mm" H 5900 3150 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8151-8-bit-AVR-ATmega128A_Datasheet.pdf" H 5900 3150 50  0001 C CNN
	1    5900 3150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 606C4B95
P 5900 5150
F 0 "#PWR0103" H 5900 4900 50  0001 C CNN
F 1 "GND" H 5905 4977 50  0000 C CNN
F 2 "" H 5900 5150 50  0001 C CNN
F 3 "" H 5900 5150 50  0001 C CNN
	1    5900 5150
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR0105
U 1 1 606FD7AE
P 2000 2000
F 0 "#PWR0105" H 2000 1850 50  0001 C CNN
F 1 "+5V" H 2015 2173 50  0000 C CNN
F 2 "" H 2000 2000 50  0001 C CNN
F 3 "" H 2000 2000 50  0001 C CNN
	1    2000 2000
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0106
U 1 1 606FE134
P 2850 5500
F 0 "#PWR0106" H 2850 5350 50  0001 C CNN
F 1 "+3V3" H 2865 5673 50  0000 C CNN
F 2 "" H 2850 5500 50  0001 C CNN
F 3 "" H 2850 5500 50  0001 C CNN
	1    2850 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 1150 5950 1150
$Comp
L power:+3V3 #PWR0107
U 1 1 607020A3
P 5950 1100
F 0 "#PWR0107" H 5950 950 50  0001 C CNN
F 1 "+3V3" H 5965 1273 50  0000 C CNN
F 2 "" H 5950 1100 50  0001 C CNN
F 3 "" H 5950 1100 50  0001 C CNN
	1    5950 1100
	1    0    0    -1  
$EndComp
Connection ~ 5950 1150
Wire Wire Line
	5950 1150 6000 1150
Wire Wire Line
	5950 1100 5950 1150
Text GLabel 5100 4050 0    50   BiDi ~ 0
MOSI
Text GLabel 5100 4250 0    50   BiDi ~ 0
MISO
Text GLabel 6500 2450 2    50   BiDi ~ 0
SCK
Text GLabel 5300 1450 0    50   BiDi ~ 0
~RST~
$Comp
L power:+5V #PWR0110
U 1 1 60658AB4
P 9550 1600
F 0 "#PWR0110" H 9550 1450 50  0001 C CNN
F 1 "+5V" V 9565 1728 50  0000 L CNN
F 2 "" H 9550 1600 50  0001 C CNN
F 3 "" H 9550 1600 50  0001 C CNN
	1    9550 1600
	0    -1   -1   0   
$EndComp
Text GLabel 1350 2500 0    50   Output ~ 0
UART_SBUS
Text GLabel 1350 2600 0    50   Input ~ 0
UART_TELEM_PI
Text GLabel 5100 4150 0    50   Input ~ 0
UART_SBUS
Text GLabel 9550 1800 0    50   Input ~ 0
UART_SBUS
Text GLabel 1350 3600 0    50   Output ~ 0
ABORT
Text GLabel 6500 3250 2    50   Input ~ 0
ABORT
Text GLabel 6500 3350 2    50   Input ~ 0
SUPERVISOR_RESET
$Comp
L Device:LED D5
U 1 1 607447AE
P 10350 6000
F 0 "D5" V 10389 5882 50  0000 R CNN
F 1 "LED" V 10298 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 10350 6000 50  0001 C CNN
F 3 "~" H 10350 6000 50  0001 C CNN
	1    10350 6000
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R6
U 1 1 60745DF5
P 10350 5650
F 0 "R6" H 10420 5696 50  0000 L CNN
F 1 "300" H 10420 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 10280 5650 50  0001 C CNN
F 3 "~" H 10350 5650 50  0001 C CNN
	1    10350 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:R R5
U 1 1 60745A0F
P 10000 5650
F 0 "R5" H 10070 5696 50  0000 L CNN
F 1 "300" H 10070 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 9930 5650 50  0001 C CNN
F 3 "~" H 10000 5650 50  0001 C CNN
	1    10000 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 607450B4
P 9650 5650
F 0 "R4" H 9720 5696 50  0000 L CNN
F 1 "300" H 9720 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 9580 5650 50  0001 C CNN
F 3 "~" H 9650 5650 50  0001 C CNN
	1    9650 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D4
U 1 1 60743E5B
P 10000 6000
F 0 "D4" V 10039 5882 50  0000 R CNN
F 1 "LED" V 9948 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 10000 6000 50  0001 C CNN
F 3 "~" H 10000 6000 50  0001 C CNN
	1    10000 6000
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D3
U 1 1 607403B4
P 9650 6000
F 0 "D3" V 9689 5882 50  0000 R CNN
F 1 "LED" V 9598 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 9650 6000 50  0001 C CNN
F 3 "~" H 9650 6000 50  0001 C CNN
	1    9650 6000
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R3
U 1 1 60753676
P 9300 5650
F 0 "R3" H 9370 5696 50  0000 L CNN
F 1 "300" H 9370 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 9230 5650 50  0001 C CNN
F 3 "~" H 9300 5650 50  0001 C CNN
	1    9300 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 6075367C
P 8950 5650
F 0 "R2" H 9020 5696 50  0000 L CNN
F 1 "300" H 9020 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 8880 5650 50  0001 C CNN
F 3 "~" H 8950 5650 50  0001 C CNN
	1    8950 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D2
U 1 1 60753682
P 9300 6000
F 0 "D2" V 9339 5882 50  0000 R CNN
F 1 "LED" V 9248 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 9300 6000 50  0001 C CNN
F 3 "~" H 9300 6000 50  0001 C CNN
	1    9300 6000
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D1
U 1 1 60753688
P 8950 6000
F 0 "D1" V 8989 5882 50  0000 R CNN
F 1 "LED" V 8898 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 8950 6000 50  0001 C CNN
F 3 "~" H 8950 6000 50  0001 C CNN
	1    8950 6000
	0    -1   -1   0   
$EndComp
Text Notes 9300 5200 0    50   ~ 0
Indicator LEDs\n
$Comp
L power:+5V #PWR0114
U 1 1 6077299F
P 10350 5500
F 0 "#PWR0114" H 10350 5350 50  0001 C CNN
F 1 "+5V" H 10365 5673 50  0000 C CNN
F 2 "" H 10350 5500 50  0001 C CNN
F 3 "" H 10350 5500 50  0001 C CNN
	1    10350 5500
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0115
U 1 1 6077383E
P 10000 5500
F 0 "#PWR0115" H 10000 5350 50  0001 C CNN
F 1 "+3V3" H 10015 5673 50  0000 C CNN
F 2 "" H 10000 5500 50  0001 C CNN
F 3 "" H 10000 5500 50  0001 C CNN
	1    10000 5500
	1    0    0    -1  
$EndComp
Text GLabel 8950 5500 1    50   Input ~ 0
A
Text GLabel 9300 5500 1    50   Input ~ 0
R
Text GLabel 9650 5500 1    50   Input ~ 0
N
Text GLabel 6500 1650 2    50   Output ~ 0
A
Text GLabel 6500 1750 2    50   Output ~ 0
R
Text GLabel 6500 1850 2    50   Output ~ 0
N
$Comp
L power:GND #PWR0116
U 1 1 607762E8
P 8950 6150
F 0 "#PWR0116" H 8950 5900 50  0001 C CNN
F 1 "GND" H 8955 5977 50  0000 C CNN
F 2 "" H 8950 6150 50  0001 C CNN
F 3 "" H 8950 6150 50  0001 C CNN
	1    8950 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0117
U 1 1 60776F49
P 9300 6150
F 0 "#PWR0117" H 9300 5900 50  0001 C CNN
F 1 "GND" H 9305 5977 50  0000 C CNN
F 2 "" H 9300 6150 50  0001 C CNN
F 3 "" H 9300 6150 50  0001 C CNN
	1    9300 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0118
U 1 1 607776BF
P 9650 6150
F 0 "#PWR0118" H 9650 5900 50  0001 C CNN
F 1 "GND" H 9655 5977 50  0000 C CNN
F 2 "" H 9650 6150 50  0001 C CNN
F 3 "" H 9650 6150 50  0001 C CNN
	1    9650 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0119
U 1 1 60777F5D
P 10000 6150
F 0 "#PWR0119" H 10000 5900 50  0001 C CNN
F 1 "GND" H 10005 5977 50  0000 C CNN
F 2 "" H 10000 6150 50  0001 C CNN
F 3 "" H 10000 6150 50  0001 C CNN
	1    10000 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0120
U 1 1 607780E7
P 10350 6150
F 0 "#PWR0120" H 10350 5900 50  0001 C CNN
F 1 "GND" H 10355 5977 50  0000 C CNN
F 2 "" H 10350 6150 50  0001 C CNN
F 3 "" H 10350 6150 50  0001 C CNN
	1    10350 6150
	1    0    0    -1  
$EndComp
Wire Wire Line
	8950 5800 8950 5850
Wire Wire Line
	9300 5800 9300 5850
Wire Wire Line
	9650 5800 9650 5850
Wire Wire Line
	10000 5800 10000 5850
Wire Wire Line
	10350 5800 10350 5850
Text GLabel 6500 1950 2    50   Output ~ 0
~POWER_EN~
$Comp
L Device:C C3
U 1 1 607B28FC
P 1700 5650
F 0 "C3" H 1815 5696 50  0000 L CNN
F 1 "1uf" H 1815 5605 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 1738 5500 50  0001 C CNN
F 3 "~" H 1700 5650 50  0001 C CNN
	1    1700 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:C C4
U 1 1 607B3034
P 2600 5650
F 0 "C4" H 2715 5696 50  0000 L CNN
F 1 "1uf" H 2715 5605 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 2638 5500 50  0001 C CNN
F 3 "~" H 2600 5650 50  0001 C CNN
	1    2600 5650
	1    0    0    -1  
$EndComp
Wire Wire Line
	1700 5500 1850 5500
Wire Wire Line
	2450 5500 2600 5500
Wire Wire Line
	2600 5800 2150 5800
Wire Wire Line
	1700 5800 2150 5800
Connection ~ 2150 5800
$Comp
L power:GND #PWR01
U 1 1 607C3211
P 2150 5800
F 0 "#PWR01" H 2150 5550 50  0001 C CNN
F 1 "GND" H 2155 5627 50  0000 C CNN
F 2 "" H 2150 5800 50  0001 C CNN
F 3 "" H 2150 5800 50  0001 C CNN
	1    2150 5800
	1    0    0    -1  
$EndComp
Text Notes 1850 5150 0    50   ~ 0
3.3V Regulator\n
Text Notes 5150 5750 0    50   ~ 0
ATmega ISP Header\n
Text GLabel 5750 6500 2    50   BiDi ~ 0
MOSI
Text GLabel 5750 6400 2    50   BiDi ~ 0
MISO
Text GLabel 5750 6600 2    50   BiDi ~ 0
SCK
Wire Wire Line
	5750 6700 5750 7350
Text GLabel 6100 7350 2    50   BiDi ~ 0
~RST~
Wire Wire Line
	5950 6950 5950 7000
$Comp
L power:+3V3 #PWR0109
U 1 1 6070A750
P 5950 6950
F 0 "#PWR0109" H 5950 6800 50  0001 C CNN
F 1 "+3V3" H 5965 7123 50  0000 C CNN
F 2 "" H 5950 6950 50  0001 C CNN
F 3 "" H 5950 6950 50  0001 C CNN
	1    5950 6950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5950 7350 6100 7350
Connection ~ 5950 7350
Wire Wire Line
	5950 7300 5950 7350
$Comp
L Device:R R1
U 1 1 607096A1
P 5950 7150
F 0 "R1" H 6020 7196 50  0000 L CNN
F 1 "1K" H 6020 7105 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 5880 7150 50  0001 C CNN
F 3 "~" H 5950 7150 50  0001 C CNN
	1    5950 7150
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 7350 5950 7350
$Comp
L power:+3V3 #PWR0108
U 1 1 6070634D
P 5250 6100
F 0 "#PWR0108" H 5250 5950 50  0001 C CNN
F 1 "+3V3" H 5265 6273 50  0000 C CNN
F 2 "" H 5250 6100 50  0001 C CNN
F 3 "" H 5250 6100 50  0001 C CNN
	1    5250 6100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 606F1CF2
P 5250 7000
F 0 "#PWR0104" H 5250 6750 50  0001 C CNN
F 1 "GND" H 5255 6827 50  0000 C CNN
F 2 "" H 5250 7000 50  0001 C CNN
F 3 "" H 5250 7000 50  0001 C CNN
	1    5250 7000
	1    0    0    -1  
$EndComp
$Comp
L Connector:AVR-ISP-6 J2
U 1 1 606E7267
P 5350 6600
F 0 "J2" H 5021 6696 50  0000 R CNN
F 1 "AVR-ISP-6" H 5021 6605 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical" V 5100 6650 50  0001 C CNN
F 3 " ~" H 4075 6050 50  0001 C CNN
	1    5350 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 4800 2100 4800
$Comp
L power:GND1 #PWR0121
U 1 1 607DB591
P 2100 4800
F 0 "#PWR0121" H 2100 4550 50  0001 C CNN
F 1 "GND1" H 2105 4627 50  0000 C CNN
F 2 "" H 2100 4800 50  0001 C CNN
F 3 "" H 2100 4800 50  0001 C CNN
	1    2100 4800
	1    0    0    -1  
$EndComp
Connection ~ 2100 4800
Wire Wire Line
	2100 4800 2150 4800
Text GLabel 950  5650 2    50   Output ~ 0
Vin
$Comp
L power:GND #PWR0122
U 1 1 607ED3C6
P 950 5750
F 0 "#PWR0122" H 950 5500 50  0001 C CNN
F 1 "GND" H 955 5577 50  0000 C CNN
F 2 "" H 950 5750 50  0001 C CNN
F 3 "" H 950 5750 50  0001 C CNN
	1    950  5750
	0    -1   -1   0   
$EndComp
Text GLabel 1500 5500 0    50   Input ~ 0
Vin
Wire Wire Line
	1500 5500 1700 5500
Connection ~ 1700 5500
Wire Wire Line
	2600 5500 2850 5500
Connection ~ 2600 5500
Text GLabel 1350 3700 0    50   Output ~ 0
SUPERVISOR_RESET
Text GLabel 1350 7250 0    50   Input ~ 0
~POWER_EN~
$Comp
L power:GND1 #PWR03
U 1 1 6081868E
P 9550 1700
F 0 "#PWR03" H 9550 1450 50  0001 C CNN
F 1 "GND1" V 9555 1572 50  0000 R CNN
F 2 "" H 9550 1700 50  0001 C CNN
F 3 "" H 9550 1700 50  0001 C CNN
	1    9550 1700
	0    1    1    0   
$EndComp
Text Notes 1800 6450 0    50   ~ 0
Power Switching Circuit\n\n\n
$Comp
L Device:R R10
U 1 1 6081F348
P 1550 7250
F 0 "R10" V 1343 7250 50  0000 C CNN
F 1 "1k" V 1434 7250 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 1480 7250 50  0001 C CNN
F 3 "~" H 1550 7250 50  0001 C CNN
	1    1550 7250
	0    1    1    0   
$EndComp
$Comp
L Transistor_BJT:BC849 Q2
U 1 1 6081DFF5
P 2000 7250
F 0 "Q2" H 2191 7296 50  0000 L CNN
F 1 "BC849" H 2191 7205 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 2200 7175 50  0001 L CIN
F 3 "http://www.infineon.com/dgdl/Infineon-BC847SERIES_BC848SERIES_BC849SERIES_BC850SERIES-DS-v01_01-en.pdf?fileId=db3a304314dca389011541d4630a1657" H 2000 7250 50  0001 L CNN
	1    2000 7250
	1    0    0    -1  
$EndComp
Wire Wire Line
	2650 6700 2650 6800
$Comp
L power:GND1 #PWR02
U 1 1 60819813
P 2650 6700
F 0 "#PWR02" H 2650 6450 50  0001 C CNN
F 1 "GND1" H 2655 6527 50  0000 C CNN
F 2 "" H 2650 6700 50  0001 C CNN
F 3 "" H 2650 6700 50  0001 C CNN
	1    2650 6700
	-1   0    0    1   
$EndComp
Wire Wire Line
	2100 7000 2100 7050
Connection ~ 2100 7000
Wire Wire Line
	2350 7000 2100 7000
Wire Wire Line
	2100 6850 2100 7000
$Comp
L power:GND #PWR0123
U 1 1 6080DCA8
P 2100 7450
F 0 "#PWR0123" H 2100 7200 50  0001 C CNN
F 1 "GND" H 2105 7277 50  0000 C CNN
F 2 "" H 2100 7450 50  0001 C CNN
F 3 "" H 2100 7450 50  0001 C CNN
	1    2100 7450
	1    0    0    -1  
$EndComp
Text GLabel 2100 6550 1    50   Input ~ 0
Vin
$Comp
L Device:R R9
U 1 1 607FF366
P 2100 6700
F 0 "R9" H 2170 6746 50  0000 L CNN
F 1 "100k" H 2170 6655 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 2030 6700 50  0001 C CNN
F 3 "~" H 2100 6700 50  0001 C CNN
	1    2100 6700
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 607DA2F2
P 2650 7200
F 0 "#PWR0102" H 2650 6950 50  0001 C CNN
F 1 "GND" H 2655 7027 50  0000 C CNN
F 2 "" H 2650 7200 50  0001 C CNN
F 3 "" H 2650 7200 50  0001 C CNN
	1    2650 7200
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:IRF3205 Q1
U 1 1 607CA13D
P 2550 7000
F 0 "Q1" H 2755 7046 50  0000 L CNN
F 1 "IRF3205" H 2755 6955 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 2800 6925 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf3205.pdf" H 2550 7000 50  0001 L CNN
	1    2550 7000
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J5
U 1 1 60851DA0
P 750 5750
F 0 "J5" H 668 5425 50  0000 C CNN
F 1 "Conn_01x03" H 668 5516 50  0000 C CNN
F 2 "FlightBridgePCB:ELECTRICAL_Connection" H 750 5750 50  0001 C CNN
F 3 "~" H 750 5750 50  0001 C CNN
	1    750  5750
	-1   0    0    1   
$EndComp
$Comp
L power:GND1 #PWR0111
U 1 1 60852C30
P 950 5850
F 0 "#PWR0111" H 950 5600 50  0001 C CNN
F 1 "GND1" V 955 5722 50  0000 R CNN
F 2 "" H 950 5850 50  0001 C CNN
F 3 "" H 950 5850 50  0001 C CNN
	1    950  5850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1700 7250 1800 7250
Wire Wire Line
	1400 7250 1350 7250
$Comp
L Connector:Raspberry_Pi_2_3 J1
U 1 1 60669113
P 2150 3400
F 0 "J1" H 2150 5200 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 2150 5100 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 2150 3400 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 2150 3400 50  0001 C CNN
	1    2150 3400
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR06
U 1 1 6090A8C1
P 6700 800
F 0 "#PWR06" H 6700 650 50  0001 C CNN
F 1 "+3V3" H 6715 973 50  0000 C CNN
F 2 "" H 6700 800 50  0001 C CNN
F 3 "" H 6700 800 50  0001 C CNN
	1    6700 800 
	1    0    0    -1  
$EndComp
$Comp
L Device:C C7
U 1 1 6090DDD0
P 6700 950
F 0 "C7" H 6815 996 50  0000 L CNN
F 1 "1u" H 6815 905 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 6738 800 50  0001 C CNN
F 3 "~" H 6700 950 50  0001 C CNN
	1    6700 950 
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR07
U 1 1 6090EB35
P 6700 1100
F 0 "#PWR07" H 6700 850 50  0001 C CNN
F 1 "GND" H 6705 927 50  0000 C CNN
F 2 "" H 6700 1100 50  0001 C CNN
F 3 "" H 6700 1100 50  0001 C CNN
	1    6700 1100
	1    0    0    -1  
$EndComp
$Comp
L Device:C C8
U 1 1 6090F0EF
P 7000 950
F 0 "C8" H 7115 996 50  0000 L CNN
F 1 "1u" H 7115 905 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 7038 800 50  0001 C CNN
F 3 "~" H 7000 950 50  0001 C CNN
	1    7000 950 
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 800  6700 800 
Connection ~ 6700 800 
Wire Wire Line
	7000 1100 6700 1100
Connection ~ 6700 1100
$Comp
L Device:C C5
U 1 1 6091AF55
P 3150 2000
F 0 "C5" H 3265 2046 50  0000 L CNN
F 1 "1u" H 3265 1955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 3188 1850 50  0001 C CNN
F 3 "~" H 3150 2000 50  0001 C CNN
	1    3150 2000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR05
U 1 1 6091AF5B
P 3150 2150
F 0 "#PWR05" H 3150 1900 50  0001 C CNN
F 1 "GND" H 3155 1977 50  0000 C CNN
F 2 "" H 3150 2150 50  0001 C CNN
F 3 "" H 3150 2150 50  0001 C CNN
	1    3150 2150
	1    0    0    -1  
$EndComp
$Comp
L Device:C C6
U 1 1 6091AF61
P 3450 2000
F 0 "C6" H 3565 2046 50  0000 L CNN
F 1 "1u" H 3565 1955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 3488 1850 50  0001 C CNN
F 3 "~" H 3450 2000 50  0001 C CNN
	1    3450 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	3450 1850 3150 1850
Wire Wire Line
	3450 2150 3150 2150
Connection ~ 3150 2150
$Comp
L power:+5V #PWR04
U 1 1 6091C5FE
P 3150 1850
F 0 "#PWR04" H 3150 1700 50  0001 C CNN
F 1 "+5V" H 3165 2023 50  0000 C CNN
F 2 "" H 3150 1850 50  0001 C CNN
F 3 "" H 3150 1850 50  0001 C CNN
	1    3150 1850
	1    0    0    -1  
$EndComp
Connection ~ 3150 1850
Wire Wire Line
	5300 4150 5200 4150
Wire Wire Line
	5100 4050 5200 4050
Wire Wire Line
	5200 4050 5200 4150
Connection ~ 5200 4150
Wire Wire Line
	5200 4150 5100 4150
Wire Wire Line
	5100 4250 5300 4250
$Comp
L Regulator_Linear:MCP1700-3302E_TO92 U2
U 1 1 609851B3
P 2150 5500
F 0 "U2" H 2150 5258 50  0000 C CNN
F 1 "MCP1700-3302E_TO92" H 2150 5349 50  0000 C CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 2150 5300 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20001826D.pdf" H 2150 5500 50  0001 C CNN
	1    2150 5500
	1    0    0    1   
$EndComp
$Comp
L Connector_Generic:Conn_01x03 J3
U 1 1 609C188B
P 9750 1700
F 0 "J3" H 9830 1742 50  0000 L CNN
F 1 "Conn_01x03" H 9830 1651 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Horizontal" H 9750 1700 50  0001 C CNN
F 3 "~" H 9750 1700 50  0001 C CNN
	1    9750 1700
	1    0    0    -1  
$EndComp
Text GLabel 2950 2800 2    50   Output ~ 0
SDA
Text GLabel 2950 2900 2    50   Output ~ 0
SCL
Text Notes 9200 2300 0    50   ~ 0
Pi I2C breakout\n\n
$Comp
L Connector_Generic:Conn_01x04 J4
U 1 1 60A1AD24
P 9750 2550
F 0 "J4" H 9830 2542 50  0000 L CNN
F 1 "Conn_01x04" H 9830 2451 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Horizontal" H 9750 2550 50  0001 C CNN
F 3 "~" H 9750 2550 50  0001 C CNN
	1    9750 2550
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0112
U 1 1 60A1E0CF
P 9550 2450
F 0 "#PWR0112" H 9550 2300 50  0001 C CNN
F 1 "+3V3" H 9565 2623 50  0000 C CNN
F 2 "" H 9550 2450 50  0001 C CNN
F 3 "" H 9550 2450 50  0001 C CNN
	1    9550 2450
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0113
U 1 1 60A26F57
P 9350 2550
F 0 "#PWR0113" H 9350 2300 50  0001 C CNN
F 1 "GND" H 9355 2377 50  0000 C CNN
F 2 "" H 9350 2550 50  0001 C CNN
F 3 "" H 9350 2550 50  0001 C CNN
	1    9350 2550
	0    1    -1   0   
$EndComp
Wire Wire Line
	9550 2550 9350 2550
Text GLabel 9550 2650 0    50   Input ~ 0
SDA
Text GLabel 9550 2750 0    50   Input ~ 0
SCL
$EndSCHEMATC
