/*
    Serial Driver for AVR chips. 
*/ 

//Defininitions for Constants
#define SERIAL_TX_BUFFER_SIZE 16
#define SERIAL_RX_BUFFER_SIZE 16

class Serial
{
private:
    unsigned char rx_buffer[SERIAL_RX_BUFFER_SIZE];
    unsigned char tx_buffer[SERIAL_TX_BUFFER_SIZE];

    volatile int rx_buffer_index;
    volatile int tx_buffer_index;

public:
    void begin(unsigned long baud, unsigned long Fosc, int USART);
    void SendMessage(char* message);
    char message[SERIAL_RX_BUFFER_SIZE];
    bool SendingMessage = false;
    volatile unsigned int StrIndex = 0;
    //void SendLine()
};


