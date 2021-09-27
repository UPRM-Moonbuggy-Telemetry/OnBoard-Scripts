#include "elapsedMillis-1.0.4/elapsedMillis.h"

elapsedMillis start_time;
 
// OLD BUGGY SKETCH //

// Constants for all strain sensor:
const float INPUT_V = 5.0;
const float GAUGE_FACTOR = 2.0;
const float UNSTRAINED_OUTPUT_V = 0; // this is 50% value of the output voltage
const float factor_V = 5/1023;

// Callibrated voltage for each strain sensor:
float SCF_1_Vr = 0; 



// Initialization of pins
// select the input pin for the Strain Gauge (Analogo)
int strain_center_front_1 = A0;   //sensorPin


// Values to read by input:

// variables to store the second values
// coming from Strain Sensors
int strain_center_front_1_aSignal = 0; // sensorvalue10

//variables de % de voltaje:

int strain_center_front_1_aSignalPercent = 0;


// strain total for each strain sensor:
String strain_center_front_1_total = "";


void setup() {
  Serial.begin (9600);
} 


void loop() 
{
  
  // aSignal means = analog signal, it does not have a value persay
  strain_center_front_1_aSignal = analogRead(strain_center_front_1);

  
  // The 0 to 700 analog value represents the voltage from 0V to aproximately ~3.5V
  strain_center_front_1_aSignalPercent =  map(strain_center_front_1_aSignal, 0, 1023, 0, 100);


  // This is to test one of the sensors output value.
  Serial.print("aSignal: ");
  Serial.print(strain_center_front_1_aSignal);
  Serial.print("|");
  Serial.print(strain_center_front_1_aSignalPercent);
  Serial.println("%");
  
  SCF_1_Vr = ((strain_center_front_1_aSignalPercent*factor_V)/INPUT_V) - (UNSTRAINED_OUTPUT_V/INPUT_V);
  strain_center_front_1_total = (String)(-(4*SCF_1_Vr)/(GAUGE_FACTOR*(1+2*(SCF_1_Vr))));
 
  Serial.flush();
  Serial.print(strain_center_front_1_total);
  //Serial.write(frequency1 + "," + strain_center_front_1_total);
  Serial.flush();
}
