#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <Serial.h>
#include <string.h>

// # Defines
//#define USART_BAUDRATE 9600 
//#define BAUD_PRESCALE (((F_CPU / (USART_BAUDRATE * 16UL))) - 1) 
//#define F_CPU 8000000L

#define SENDER

//Prototype Definitions
//void SendMessage(char* message);

//Setup the Serial
Serial Serial0;

// char message[SERIAL_TX_BUFFER_SIZE] = "1234ABCD\r";
char message[SERIAL_TX_BUFFER_SIZE];

int main(void)
{
    // make the LED pin an output for PORTB5
    DDRB = 1 << 5;

    //Enable the Serial Ports
    strcpy(message, "1234ABCD\r\n");

    Serial0.begin(9600, F_CPU, 0);

    //Enable interrupts
    UCSR0B |= (1 << RXCIE0); // Enable the USART Recieve Complete interrupt (USART_RXC)

    sei();

    #ifdef SENDER
    Serial0.SendMessage(message);
    #endif

    for (;;){// Loop forever
    }   

    return 0;
}

// void SendMessage(char* message){

//     //SendingMessage = true;

//     for(unsigned int i = 0; i < strlen(message); i++){
//         while ((UCSR0A & (1 << UDRE0)) == 0) {}; // Do nothing until UDR is ready for more data to be written to it 
//         UDR0 = message[i]; // Echo back the received byte back to the computer   
//         _delay_ms(500); 
//         //Toggle the LED
//         PORTB ^= 1 << 5;
//     }
// }

ISR(USART_RX_vect){
    
    char ReceivedByte;
    ReceivedByte = UDR0;

    if (ReceivedByte == 'A')
    {
        //Toggle the LED
        PORTB ^= 1 << 5;

    }

    #ifndef SENDER
    //Echo back the recieved data
    while ((UCSR0A & (1 << UDRE0)) == 0) {}; // Do nothing until UDR is ready for more data to be written to it 
    UDR0 = ReceivedByte; // Echo back the received byte back to the computer 
    #endif

}

ISR(USART_UDRE_vect){

    //Check if sending a message on Serial0 and it is ready 
    // (helps for when there aremultiple UART)
    if (Serial0.SendingMessage){

        UDR0 = Serial0.tx_message[Serial0.StrIndex];
        Serial0.StrIndex = Serial0.StrIndex + 1;

    }

    if (Serial0.StrIndex == strlen(Serial0.tx_message)){

        Serial0.SendingMessage = false;
        UCSR0B ^= (1 << UDRIE0); //Disable the interrupt

    }

}