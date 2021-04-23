EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L pspice:VSOURCE V1
U 1 1 607B2248
P 3500 2900
F 0 "V1" H 3728 2946 50  0000 L CNN
F 1 "VSOURCE" H 3728 2855 50  0000 L CNN
F 2 "" H 3500 2900 50  0001 C CNN
F 3 "~" H 3500 2900 50  0001 C CNN
F 4 "V" H 3500 2900 50  0001 C CNN "Spice_Primitive"
F 5 "dc 8.5" H 3500 2900 50  0001 C CNN "Spice_Model"
F 6 "Y" H 3500 2900 50  0001 C CNN "Spice_Netlist_Enabled"
	1    3500 2900
	1    0    0    -1  
$EndComp
$Comp
L pspice:VSOURCE V2
U 1 1 607B3A7A
P 3500 4200
F 0 "V2" H 3728 4246 50  0000 L CNN
F 1 "VSOURCE" H 3728 4155 50  0000 L CNN
F 2 "" H 3500 4200 50  0001 C CNN
F 3 "~" H 3500 4200 50  0001 C CNN
F 4 "V" H 3500 4200 50  0001 C CNN "Spice_Primitive"
F 5 "pulse(0 3.3 5m 100u 100u 1 1.2)" H 3500 4200 50  0001 C CNN "Spice_Model"
F 6 "Y" H 3500 4200 50  0001 C CNN "Spice_Netlist_Enabled"
	1    3500 4200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR02
U 1 1 607B696D
P 3500 3200
F 0 "#PWR02" H 3500 2950 50  0001 C CNN
F 1 "GND" H 3505 3027 50  0000 C CNN
F 2 "" H 3500 3200 50  0001 C CNN
F 3 "" H 3500 3200 50  0001 C CNN
	1    3500 3200
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR03
U 1 1 607CB4AC
P 3500 4500
F 0 "#PWR03" H 3500 4250 50  0001 C CNN
F 1 "GND" H 3505 4327 50  0000 C CNN
F 2 "" H 3500 4500 50  0001 C CNN
F 3 "" H 3500 4500 50  0001 C CNN
	1    3500 4500
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 607C1717
P 4550 3300
F 0 "R4" H 4480 3254 50  0000 R CNN
F 1 "100k" H 4480 3345 50  0000 R CNN
F 2 "" V 4480 3300 50  0001 C CNN
F 3 "~" H 4550 3300 50  0001 C CNN
	1    4550 3300
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR05
U 1 1 607C305E
P 4550 4200
F 0 "#PWR05" H 4550 3950 50  0001 C CNN
F 1 "GND" H 4555 4027 50  0000 C CNN
F 2 "" H 4550 4200 50  0001 C CNN
F 3 "" H 4550 4200 50  0001 C CNN
	1    4550 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4550 3150 4550 2600
Wire Wire Line
	3500 2600 4550 2600
$Comp
L Device:R R5
U 1 1 607D742F
P 3950 3900
F 0 "R5" V 3743 3900 50  0000 C CNN
F 1 "1k" V 3834 3900 50  0000 C CNN
F 2 "" V 3880 3900 50  0001 C CNN
F 3 "~" H 3950 3900 50  0001 C CNN
	1    3950 3900
	0    1    1    0   
$EndComp
Wire Wire Line
	3500 3900 3800 3900
Wire Wire Line
	4100 3900 4250 3900
Wire Wire Line
	4550 3450 4550 3550
Wire Wire Line
	4550 4100 4550 4150
$Comp
L Transistor_BJT:2N3904 Q1
U 1 1 607E584B
P 4450 3900
F 0 "Q1" H 4641 3946 50  0000 L CNN
F 1 "BC849C" H 4641 3855 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 4650 3825 50  0001 L CIN
F 3 "https://www.onsemi.com/pub/Collateral/2N3903-D.PDF" H 4450 3900 50  0001 L CNN
F 4 "X" H 4450 3900 50  0001 C CNN "Spice_Primitive"
F 5 "BC849C" H 4450 3900 50  0001 C CNN "Spice_Model"
F 6 "Y" H 4450 3900 50  0001 C CNN "Spice_Netlist_Enabled"
F 7 "C:\\Users\\Connor\\Downloads\\BC849C.txt" H 4450 3900 50  0001 C CNN "Spice_Lib_File"
	1    4450 3900
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:BUZ11 Q2
U 1 1 607E930E
P 5550 3750
F 0 "Q2" H 5755 3796 50  0000 L CNN
F 1 "IFR3808" H 5755 3705 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 5800 3675 50  0001 L CIN
F 3 "https://media.digikey.com/pdf/Data%20Sheets/Fairchild%20PDFs/BUZ11.pdf" H 5550 3750 50  0001 L CNN
F 4 "X" H 5550 3750 50  0001 C CNN "Spice_Primitive"
F 5 "irf3808" H 5550 3750 50  0001 C CNN "Spice_Model"
F 6 "Y" H 5550 3750 50  0001 C CNN "Spice_Netlist_Enabled"
F 7 "C:\\Users\\Connor\\Downloads\\irf3808.spi" H 5550 3750 50  0001 C CNN "Spice_Lib_File"
F 8 "2 1 3" H 5550 3750 50  0001 C CNN "Spice_Node_Sequence"
	1    5550 3750
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 607E9D34
P 5650 3050
F 0 "R1" H 5580 3004 50  0000 R CNN
F 1 "0.12" H 5580 3095 50  0000 R CNN
F 2 "" V 5580 3050 50  0001 C CNN
F 3 "~" H 5650 3050 50  0001 C CNN
	1    5650 3050
	-1   0    0    1   
$EndComp
Wire Wire Line
	4550 2600 5650 2600
Wire Wire Line
	5650 2600 5650 2900
Connection ~ 4550 2600
Wire Wire Line
	5650 3200 5650 3550
Wire Wire Line
	5650 3950 5650 4150
Wire Wire Line
	5650 4150 4550 4150
Connection ~ 4550 4150
Wire Wire Line
	4550 4150 4550 4200
Wire Wire Line
	4550 3550 5050 3550
Wire Wire Line
	5050 3550 5050 3750
Wire Wire Line
	5050 3750 5350 3750
Connection ~ 4550 3550
Wire Wire Line
	4550 3550 4550 3700
$EndSCHEMATC