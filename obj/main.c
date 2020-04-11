#include <wiringPi.h>
#include <wiringPiSPI.h>

#include <stdio.h>		//printf()
#include <stdlib.h>		//exit()
#include <time.h>  

#include "LCD_Driver.h"
#include "LCD_GUI.h"
#include "LCD_BMP.h"
#include "DEV_Config.h"
#include "KEY_APP.h"

int main(void)
{
	//1.System Initialization
	if(DEV_ModuleInit())
		exit(0);
	
	//2.show
	printf("**********Init LCD**********\r\n");
	LCD_SCAN_DIR LCD_ScanDir = SCAN_DIR_DFT;//SCAN_DIR_DFT = D2U_L2R
	LCD_Init(LCD_ScanDir );	
	
	printf("show bmp\r\n");
	LCD_ShowBmp(0);
	DEV_Delay_ms(5000);
	
	for(int i = 0;i<15;i++){
		LCD_ShowBmp(1);
		DEV_Delay_ms(500);
		LCD_ShowBmp(2);
		DEV_Delay_ms(500);
	}
	LCD_ShowBmp(0);
    /*
    KEY_Listen();
	//3.System Exit
	DEV_ModuleExit();
	*/
	return 0;
}
