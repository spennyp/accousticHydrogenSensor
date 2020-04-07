#include "stdio.h"
#include "mbed.h"

AnalogIn sensor(A0);
AnalogIn temp1(A1);
AnalogIn temp2(A2);
int timeStep = 1; //Sec

// Read the output with mbed sterm in the terminal on your compute
// You can have it save to file by adding > fileName.txt to the end

int main() {
    printf("Sensor, thermocouple diff\n");
    while(1){
        float sensorPercent = sensor.read();
        float tDiff = temp1.read() - temp2.read();
        printf("%5.5f, ", sensorPercent);
        printf("%5.5f \n", tDiff);
        wait_us(timeStep * 1000000); 
    }
}

