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
Text Notes 5400 1350 0    50   ~ 0
Rad-hard Supervisor IC\n
Text Notes 9200 1350 0    50   ~ 0
To/From Flight Controller\n
$Comp
L Device:Crystal Y1
U 1 1 606826B2
P 4900 2400
F 0 "Y1" V 4854 2531 50  0000 L CNN
F 1 "Crystal" V 4945 2531 50  0000 L CNN
F 2 "Crystal:Crystal_SMD_HC49-SD" H 4900 2400 50  0001 C CNN
F 3 "~" H 4900 2400 50  0001 C CNN
	1    4900 2400
	0    1    1    0   
$EndComp
$Comp
L Device:C C1
U 1 1 60685F65
P 4550 2250
F 0 "C1" V 4298 2250 50  0000 C CNN
F 1 "22pF" V 4389 2250 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 4588 2100 50  0001 C CNN
F 3 "~" H 4550 2250 50  0001 C CNN
	1    4550 2250
	0    1    1    0   
$EndComp
$Comp
L Device:C C2
U 1 1 606881D4
P 4550 2550
F 0 "C2" V 4300 2550 50  0000 C CNN
F 1 "22pF" V 4400 2550 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 4588 2400 50  0001 C CNN
F 3 "~" H 4550 2550 50  0001 C CNN
	1    4550 2550
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4700 2250 4900 2250
Wire Wire Line
	4900 2550 4700 2550
Wire Wire Line
	4900 2550 5300 2550
Wire Wire Line
	5300 2550 5300 2500
Connection ~ 4900 2550
Wire Wire Line
	5300 2300 5300 2250
Wire Wire Line
	5300 2250 4900 2250
Connection ~ 4900 2250
Wire Wire Line
	4400 2250 4400 2400
Wire Wire Line
	4200 2400 4400 2400
Connection ~ 4400 2400
Wire Wire Line
	4400 2400 4400 2550
$Comp
L power:GND #PWR0101
U 1 1 6069D1AA
P 4200 2400
F 0 "#PWR0101" H 4200 2150 50  0001 C CNN
F 1 "GND" H 4205 2227 50  0000 C CNN
F 2 "" H 4200 2400 50  0001 C CNN
F 3 "" H 4200 2400 50  0001 C CNN
	1    4200 2400
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
	2250 2100 2250 2050
Wire Wire Line
	2350 2050 2350 2100
Wire Wire Line
	2300 2050 2300 2000
Wire Wire Line
	2250 2050 2300 2050
Wire Wire Line
	2300 2050 2350 2050
Connection ~ 2300 2050
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
	2050 4800 2100 4800
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
L power:GND #PWR0102
U 1 1 606B720B
P 2100 4800
F 0 "#PWR0102" H 2100 4550 50  0001 C CNN
F 1 "GND" H 2105 4627 50  0000 C CNN
F 2 "" H 2100 4800 50  0001 C CNN
F 3 "" H 2100 4800 50  0001 C CNN
	1    2100 4800
	1    0    0    -1  
$EndComp
Connection ~ 2100 4800
Wire Wire Line
	2100 4800 2150 4800
$Comp
L MCU_Microchip_ATmega:ATmega128A-AU U1
U 1 1 6062B161
P 5900 3800
F 0 "U1" H 5900 1500 50  0000 C CNN
F 1 "ATmega128A-AU" H 5900 1400 50  0000 C CNN
F 2 "Package_QFP:TQFP-64_14x14mm_P0.8mm" H 5900 3800 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8151-8-bit-AVR-ATmega128A_Datasheet.pdf" H 5900 3800 50  0001 C CNN
	1    5900 3800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0103
U 1 1 606C4B95
P 5900 5800
F 0 "#PWR0103" H 5900 5550 50  0001 C CNN
F 1 "GND" H 5905 5627 50  0000 C CNN
F 2 "" H 5900 5800 50  0001 C CNN
F 3 "" H 5900 5800 50  0001 C CNN
	1    5900 5800
	1    0    0    -1  
$EndComp
$Comp
L Connector:AVR-ISP-6 J2
U 1 1 606E7267
P 4050 6200
F 0 "J2" H 3721 6296 50  0000 R CNN
F 1 "AVR-ISP-6" H 3721 6205 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical" V 3800 6250 50  0001 C CNN
F 3 " ~" H 2775 5650 50  0001 C CNN
	1    4050 6200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 606F1CF2
P 3950 6600
F 0 "#PWR0104" H 3950 6350 50  0001 C CNN
F 1 "GND" H 3955 6427 50  0000 C CNN
F 2 "" H 3950 6600 50  0001 C CNN
F 3 "" H 3950 6600 50  0001 C CNN
	1    3950 6600
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
P 2300 2000
F 0 "#PWR0106" H 2300 1850 50  0001 C CNN
F 1 "+3V3" H 2315 2173 50  0000 C CNN
F 2 "" H 2300 2000 50  0001 C CNN
F 3 "" H 2300 2000 50  0001 C CNN
	1    2300 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 1800 5950 1800
$Comp
L power:+3V3 #PWR0107
U 1 1 607020A3
P 5950 1750
F 0 "#PWR0107" H 5950 1600 50  0001 C CNN
F 1 "+3V3" H 5965 1923 50  0000 C CNN
F 2 "" H 5950 1750 50  0001 C CNN
F 3 "" H 5950 1750 50  0001 C CNN
	1    5950 1750
	1    0    0    -1  
$EndComp
Connection ~ 5950 1800
Wire Wire Line
	5950 1800 6000 1800
Wire Wire Line
	5950 1750 5950 1800
$Comp
L power:+3V3 #PWR0108
U 1 1 6070634D
P 3950 5700
F 0 "#PWR0108" H 3950 5550 50  0001 C CNN
F 1 "+3V3" H 3965 5873 50  0000 C CNN
F 2 "" H 3950 5700 50  0001 C CNN
F 3 "" H 3950 5700 50  0001 C CNN
	1    3950 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	4450 6950 4650 6950
$Comp
L Device:R R1
U 1 1 607096A1
P 4650 6750
F 0 "R1" H 4720 6796 50  0000 L CNN
F 1 "1K" H 4720 6705 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 4580 6750 50  0001 C CNN
F 3 "~" H 4650 6750 50  0001 C CNN
	1    4650 6750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 6900 4650 6950
Connection ~ 4650 6950
Wire Wire Line
	4650 6950 4800 6950
$Comp
L power:+3V3 #PWR0109
U 1 1 6070A750
P 4650 6550
F 0 "#PWR0109" H 4650 6400 50  0001 C CNN
F 1 "+3V3" H 4665 6723 50  0000 C CNN
F 2 "" H 4650 6550 50  0001 C CNN
F 3 "" H 4650 6550 50  0001 C CNN
	1    4650 6550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 6550 4650 6600
Text GLabel 4800 6950 2    50   BiDi ~ 0
~RST~
Wire Wire Line
	4450 6300 4450 6950
Text GLabel 4450 6200 2    50   BiDi ~ 0
SCK
Text GLabel 4450 6000 2    50   BiDi ~ 0
MISO
Text GLabel 4450 6100 2    50   BiDi ~ 0
MOSI
Text GLabel 6500 3200 2    50   BiDi ~ 0
MOSI
Text GLabel 6500 3300 2    50   BiDi ~ 0
MISO
Text GLabel 6500 3100 2    50   BiDi ~ 0
SCK
Text GLabel 5300 2100 0    50   BiDi ~ 0
~RST~
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
L Connector_Generic:Conn_01x05 J3
U 1 1 606579CB
P 9750 1800
F 0 "J3" H 9830 1842 50  0000 L CNN
F 1 "Conn_01x05" H 9830 1751 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Horizontal" H 9750 1800 50  0001 C CNN
F 3 "~" H 9750 1800 50  0001 C CNN
	1    9750 1800
	1    0    0    -1  
$EndComp
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
$Comp
L power:GND #PWR0111
U 1 1 60659B5F
P 9550 1700
F 0 "#PWR0111" H 9550 1450 50  0001 C CNN
F 1 "GND" V 9555 1572 50  0000 R CNN
F 2 "" H 9550 1700 50  0001 C CNN
F 3 "" H 9550 1700 50  0001 C CNN
	1    9550 1700
	0    1    1    0   
$EndComp
Text GLabel 1350 2500 0    50   Output ~ 0
UART_SBUS
Text GLabel 1350 2600 0    50   Input ~ 0
UART_TELEM_PI
Text GLabel 5300 4800 0    50   Input ~ 0
UART_SBUS
Text GLabel 9550 1900 0    50   Input ~ 0
UART_SBUS
Text GLabel 9550 1800 0    50   Output ~ 0
UART_TELEM_FC
Text Notes 3650 5400 0    50   ~ 0
ATmega ISP Header\n
Text GLabel 6500 5100 2    50   Output ~ 0
UART_RESET
Text GLabel 9550 2000 0    50   Input ~ 0
UART_RESET
$Comp
L Device:R R7
U 1 1 606721A0
P 9750 2700
F 0 "R7" H 9820 2746 50  0000 L CNN
F 1 "0" H 9820 2655 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 9680 2700 50  0001 C CNN
F 3 "~" H 9750 2700 50  0001 C CNN
	1    9750 2700
	1    0    0    -1  
$EndComp
$Comp
L Device:R R8
U 1 1 60672D84
P 9750 3000
F 0 "R8" H 9820 3046 50  0000 L CNN
F 1 "0" H 9820 2955 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 9680 3000 50  0001 C CNN
F 3 "~" H 9750 3000 50  0001 C CNN
	1    9750 3000
	1    0    0    -1  
$EndComp
Text GLabel 9600 2850 0    50   Output ~ 0
UART_TELEM
Wire Wire Line
	9600 2850 9750 2850
Connection ~ 9750 2850
Text Notes 9200 2350 0    50   ~ 0
Telemetry Selector\n
Text GLabel 10050 2550 2    50   Input ~ 0
UART_TELEM_FC
Wire Wire Line
	9750 2550 10050 2550
$Comp
L Connector_Generic:Conn_01x03 J4
U 1 1 6067E30D
P 9550 3800
F 0 "J4" H 9630 3842 50  0000 L CNN
F 1 "Conn_01x03" H 9630 3751 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Horizontal" H 9550 3800 50  0001 C CNN
F 3 "~" H 9550 3800 50  0001 C CNN
	1    9550 3800
	1    0    0    -1  
$EndComp
Text Notes 9200 3400 0    50   ~ 0
External Telemetry Input\n
Text GLabel 9350 3900 0    50   Output ~ 0
UART_TELEM_EXT
$Comp
L power:+5V #PWR0112
U 1 1 6068215D
P 9350 3700
F 0 "#PWR0112" H 9350 3550 50  0001 C CNN
F 1 "+5V" V 9365 3828 50  0000 L CNN
F 2 "" H 9350 3700 50  0001 C CNN
F 3 "" H 9350 3700 50  0001 C CNN
	1    9350 3700
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0113
U 1 1 60682A5F
P 9350 3800
F 0 "#PWR0113" H 9350 3550 50  0001 C CNN
F 1 "GND" V 9355 3672 50  0000 R CNN
F 2 "" H 9350 3800 50  0001 C CNN
F 3 "" H 9350 3800 50  0001 C CNN
	1    9350 3800
	0    1    1    0   
$EndComp
Text GLabel 10050 3150 2    50   Input ~ 0
UART_TELEM_EXT
Wire Wire Line
	9750 3150 10050 3150
Text GLabel 6500 5000 2    50   Input ~ 0
UART_TELEM
Text GLabel 5300 4900 0    50   Output ~ 0
UART_TELEM_PI
Text GLabel 1350 3600 0    50   Output ~ 0
ABORT
Text GLabel 1350 3700 0    50   Output ~ 0
SUPERVISOR_RESET
Text GLabel 6500 3900 2    50   Input ~ 0
ABORT
Text GLabel 6500 4000 2    50   Input ~ 0
SUPERVISOR_RESET
$Comp
L Device:LED D5
U 1 1 607447AE
P 9200 6000
F 0 "D5" V 9239 5882 50  0000 R CNN
F 1 "LED" V 9148 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 9200 6000 50  0001 C CNN
F 3 "~" H 9200 6000 50  0001 C CNN
	1    9200 6000
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R6
U 1 1 60745DF5
P 9200 5650
F 0 "R6" H 9270 5696 50  0000 L CNN
F 1 "300" H 9270 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 9130 5650 50  0001 C CNN
F 3 "~" H 9200 5650 50  0001 C CNN
	1    9200 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:R R5
U 1 1 60745A0F
P 8850 5650
F 0 "R5" H 8920 5696 50  0000 L CNN
F 1 "300" H 8920 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 8780 5650 50  0001 C CNN
F 3 "~" H 8850 5650 50  0001 C CNN
	1    8850 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 607450B4
P 8500 5650
F 0 "R4" H 8570 5696 50  0000 L CNN
F 1 "300" H 8570 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 8430 5650 50  0001 C CNN
F 3 "~" H 8500 5650 50  0001 C CNN
	1    8500 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D4
U 1 1 60743E5B
P 8850 6000
F 0 "D4" V 8889 5882 50  0000 R CNN
F 1 "LED" V 8798 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 8850 6000 50  0001 C CNN
F 3 "~" H 8850 6000 50  0001 C CNN
	1    8850 6000
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D3
U 1 1 607403B4
P 8500 6000
F 0 "D3" V 8539 5882 50  0000 R CNN
F 1 "LED" V 8448 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 8500 6000 50  0001 C CNN
F 3 "~" H 8500 6000 50  0001 C CNN
	1    8500 6000
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R3
U 1 1 60753676
P 8150 5650
F 0 "R3" H 8220 5696 50  0000 L CNN
F 1 "300" H 8220 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 8080 5650 50  0001 C CNN
F 3 "~" H 8150 5650 50  0001 C CNN
	1    8150 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 6075367C
P 7800 5650
F 0 "R2" H 7870 5696 50  0000 L CNN
F 1 "300" H 7870 5605 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" V 7730 5650 50  0001 C CNN
F 3 "~" H 7800 5650 50  0001 C CNN
	1    7800 5650
	1    0    0    -1  
$EndComp
$Comp
L Device:LED D2
U 1 1 60753682
P 8150 6000
F 0 "D2" V 8189 5882 50  0000 R CNN
F 1 "LED" V 8098 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 8150 6000 50  0001 C CNN
F 3 "~" H 8150 6000 50  0001 C CNN
	1    8150 6000
	0    -1   -1   0   
$EndComp
$Comp
L Device:LED D1
U 1 1 60753688
P 7800 6000
F 0 "D1" V 7839 5882 50  0000 R CNN
F 1 "LED" V 7748 5882 50  0000 R CNN
F 2 "LED_SMD:LED_0805_2012Metric_Castellated" H 7800 6000 50  0001 C CNN
F 3 "~" H 7800 6000 50  0001 C CNN
	1    7800 6000
	0    -1   -1   0   
$EndComp
Text Notes 8250 6500 0    50   ~ 0
Indicator LEDs\n
$Comp
L power:+5V #PWR0114
U 1 1 6077299F
P 9200 5500
F 0 "#PWR0114" H 9200 5350 50  0001 C CNN
F 1 "+5V" H 9215 5673 50  0000 C CNN
F 2 "" H 9200 5500 50  0001 C CNN
F 3 "" H 9200 5500 50  0001 C CNN
	1    9200 5500
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0115
U 1 1 6077383E
P 8850 5500
F 0 "#PWR0115" H 8850 5350 50  0001 C CNN
F 1 "+3V3" H 8865 5673 50  0000 C CNN
F 2 "" H 8850 5500 50  0001 C CNN
F 3 "" H 8850 5500 50  0001 C CNN
	1    8850 5500
	1    0    0    -1  
$EndComp
Text GLabel 7800 5500 1    50   Input ~ 0
A
Text GLabel 8150 5500 1    50   Input ~ 0
R
Text GLabel 8500 5500 1    50   Input ~ 0
N
Text GLabel 6500 2300 2    50   Output ~ 0
A
Text GLabel 6500 2400 2    50   Output ~ 0
R
Text GLabel 6500 2500 2    50   Output ~ 0
N
$Comp
L power:GND #PWR0116
U 1 1 607762E8
P 7800 6150
F 0 "#PWR0116" H 7800 5900 50  0001 C CNN
F 1 "GND" H 7805 5977 50  0000 C CNN
F 2 "" H 7800 6150 50  0001 C CNN
F 3 "" H 7800 6150 50  0001 C CNN
	1    7800 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0117
U 1 1 60776F49
P 8150 6150
F 0 "#PWR0117" H 8150 5900 50  0001 C CNN
F 1 "GND" H 8155 5977 50  0000 C CNN
F 2 "" H 8150 6150 50  0001 C CNN
F 3 "" H 8150 6150 50  0001 C CNN
	1    8150 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0118
U 1 1 607776BF
P 8500 6150
F 0 "#PWR0118" H 8500 5900 50  0001 C CNN
F 1 "GND" H 8505 5977 50  0000 C CNN
F 2 "" H 8500 6150 50  0001 C CNN
F 3 "" H 8500 6150 50  0001 C CNN
	1    8500 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0119
U 1 1 60777F5D
P 8850 6150
F 0 "#PWR0119" H 8850 5900 50  0001 C CNN
F 1 "GND" H 8855 5977 50  0000 C CNN
F 2 "" H 8850 6150 50  0001 C CNN
F 3 "" H 8850 6150 50  0001 C CNN
	1    8850 6150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0120
U 1 1 607780E7
P 9200 6150
F 0 "#PWR0120" H 9200 5900 50  0001 C CNN
F 1 "GND" H 9205 5977 50  0000 C CNN
F 2 "" H 9200 6150 50  0001 C CNN
F 3 "" H 9200 6150 50  0001 C CNN
	1    9200 6150
	1    0    0    -1  
$EndComp
Wire Wire Line
	7800 5800 7800 5850
Wire Wire Line
	8150 5800 8150 5850
Wire Wire Line
	8500 5800 8500 5850
Wire Wire Line
	8850 5800 8850 5850
Wire Wire Line
	9200 5800 9200 5850
Text Notes 8500 4400 0    50   ~ 0
Additional GPIO Output for Power Switching (if necessary)\n
Text GLabel 9350 4750 0    50   Input ~ 0
AUX1
$Comp
L power:GND #PWR0121
U 1 1 607AB92A
P 9350 4650
F 0 "#PWR0121" H 9350 4400 50  0001 C CNN
F 1 "GND" V 9355 4522 50  0000 R CNN
F 2 "" H 9350 4650 50  0001 C CNN
F 3 "" H 9350 4650 50  0001 C CNN
	1    9350 4650
	0    1    1    0   
$EndComp
$Comp
L Connector_Generic:Conn_01x04 J5
U 1 1 607AF92A
P 9550 4650
F 0 "J5" H 9630 4642 50  0000 L CNN
F 1 "Conn_01x04" H 9630 4551 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Horizontal" H 9550 4650 50  0001 C CNN
F 3 "~" H 9550 4650 50  0001 C CNN
	1    9550 4650
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR0122
U 1 1 607B06AF
P 9350 4550
F 0 "#PWR0122" H 9350 4400 50  0001 C CNN
F 1 "+3V3" V 9365 4678 50  0000 L CNN
F 2 "" H 9350 4550 50  0001 C CNN
F 3 "" H 9350 4550 50  0001 C CNN
	1    9350 4550
	0    -1   -1   0   
$EndComp
Text GLabel 9350 4850 0    50   Input ~ 0
AUX2
Text GLabel 6500 2600 2    50   Output ~ 0
AUX1
Text GLabel 6500 2700 2    50   Output ~ 0
AUX2
$EndSCHEMATC
