#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <Serial.h>
#include <string.h>

//Defines
#define USART_BAUDRATE 9600 
#define BAUD_PRESCALE (((F_CPU / (USART_BAUDRATE * 16UL))) - 1) 
//#define F_CPU 8000000UL

int main(void)
{
    // make the LED pin an output for PORTB5
    DDRA = 0xFF;
    DDRC = 0x00;
    uint8_t pinValue = PINC & (1<<PINC0);
    
    while(1){

        pinValue = PINC & (1<<PINC0);

        if(pinValue){
            _delay_ms(2000);
            PORTA = (1 << PORTA5)|(1 << PORTA4);
            _delay_ms(500);
            PORTA = 0x00;
            _delay_ms(500);
        }

    }

}
