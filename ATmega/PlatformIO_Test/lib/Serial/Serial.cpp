/*
    Serial Driver for AVR Chips
*/

#include "Serial.h"
#include <avr/io.h>
#include <string.h>

// Public Methods

void Serial::begin(unsigned long baud, unsigned long Fosc, int USART)
{
    #define BAUD_PRESCALE (((F_CPU / (baud * Fosc))) - 1) 

    if (USART == 0)
    {
        UCSR0B |= (1 << RXEN0) | (1 << TXEN0);   // Turn on the transmission and reception circuitry 
        UCSR0C |= (1 << UCSZ00) | (1 << UCSZ01); // Use 8-bit character sizes 

        UBRR0H = (BAUD_PRESCALE >> 8); // Load upper 8-bits of the baud rate value into the high byte of the UBRR register 
        UBRR0L = BAUD_PRESCALE; // Load lower 8-bits of the baud rate value into the low byte of the UBRR register
    }
    
}

void Serial::SendMessage(char* mess)
{
    //Sends Message over serial, handled in ISR in main program
    strcpy(Serial::message, mess);
    Serial::StrIndex = 0;
    Serial::SendingMessage = true;
    UCSR0B |= (1 << UDRIE0);

}