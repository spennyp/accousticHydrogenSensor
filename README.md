# Accoustic Hydrogen Sensor
Code used to do analysis for acoustic hydrogen sensor project

## Analysis
This filder contain the analysis for the theoretical side of the project.
It contains the code to produce all plots found within the report.

## Data Aquisition
This code is run on the stm32L432 microcontroller to take the accoustic sensor input data, and temperature data and relay it to a computer.

### Set up
To get the mbed libraries run this command in the Data Aquisition folder
'''
$ mbed deploy
'''

Install the required packages if you dont have them (recommend to use a virtualenv), requirements.txt is located in \mbed-os
'''
$ pip install -r requirements.txt
'''


### Use
To compile code for the stm32L432 run, navigsate to the DataAquistion folder and run
'''
$ mbed compile
'''

Then, find your the DataAqusition.bin within ../accousticHydrogenSensor/DataAquisition/BUILD/NUCLEO_L432KC/GCC_ARM/
Plug in the microcontroller and drag this file


To view the data in terminal run
'''
$ mbed sterm
'''

To save this data to a file run 
'''
$ mbed sterm > fileName.txt
'''

Note: This can also easily be run on an arduino (take the code from main.c and change pin labeling and syntax)




