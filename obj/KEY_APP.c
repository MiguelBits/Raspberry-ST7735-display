/*****************************************************************************
* |	This version:   V1.0
* | Date        :   2019-07-06
* | Info        :   Basic version
*
******************************************************************************/
#include "KEY_APP.h"
#include "LCD_GUI.h"
#include "LCD_Driver.h"
// #include "Debug.h"

// if use 2019-06-20-raspbian-buster
// sudo nano /boot/config.txt
// add:
// gpio=6,19,5,26,13,21,20,16=pu

void Draw_Init(void)
{
    LCD_Clear(BLACK);
}

void KEY_Listen(void)
{
    Draw_Init();
    for(;;) {
        if(GET_KEY_UP == 0) {
            printf("up");
	}
        if(GET_KEY_DOWN == 0) {
            printf("down");
        }
        if(GET_KEY_LEFT == 0) {
            printf("left");
        }
        if(GET_KEY_RIGHT == 0) {
            printf("right");
        }
        if(GET_KEY_PRESS == 0) {
            printf("press");
        }
        if(GET_KEY1 == 0) {
            printf("key1");
        }
        if(GET_KEY2 == 0) {
            printf("key2");
        }
        if(GET_KEY3 == 0) {
            printf("key3");
        }
    }
}
