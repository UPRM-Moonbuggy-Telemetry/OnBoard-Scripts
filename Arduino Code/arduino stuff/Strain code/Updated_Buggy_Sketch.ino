#include <elapsedMillis.h>

elapsedMillis start_time;
 
// OLD BUGGY SKETCH //

// Constants for all strain sensor:
const float INPUT_V = 5.0;
const float GAUGE_FACTOR = 2.0;
const float UNSTRAINED_OUTPUT_V = 1.75; // this is 50% value of the output voltage
const float factor_V = 5/1023;

// Callibrated voltage for each strain sensor:
float SCF_1_Vr = 0; 
float SCF_2_Vr = 0;
float SCF_3_Vr = 0;
float SCB_1_Vr = 0;
float SCB_2_Vr = 0;
float SCB_3_Vr = 0;
float SBS_1_Vr = 0;
float SBS_2_Vr = 0;
float SBS_3_Vr = 0;


// Input-pin values:
int val_vib_pin1 = 0;
int val_vib_pin2 = 0;
int val_vib_pin3 = 0;
int val_vib_pin4 = 0;

// For the vibration sensors (Digitales)
// digital input pin for vibration sensor
int vibration_backseat_top=22;    // vib_pin1 
int vibration_backseat_bottom=24;   
int vibration_front_right=26;    
int vibration_front_left=28;    // vib_pin4 

// Frequency for each vibration sensor
String frequency1="";    // variable to store frequency value
String frequency2="";    //variable to store frequency value
String frequency3="";    //variable to store frequency value
String frequency4="";    //variable to store frequency value

// Initialization of pins
// select the input pin for the Strain Gauge (Analogo)
int strain_center_front_1 = A0;   //sensorPin
int strain_center_front_2 = A1;
int strain_center_front_3 = A2;
int strain_center_back_1 = A3;
int strain_center_back_2 = A4;
int strain_center_back_3 = A5;
int strain_backseat_1 = A6;
int strain_backseat_2 = A7;
int strain_backseat_3 = A8;  //sensorPin8

// Values to read by input:

// variables to store second values
// coming from Vibration Sensors
int aSignal_vib_pin1=0; 
int aSignal_vib_pin2=0;
int aSignal_vib_pin3=0;
int aSignal_vib_pin4=0;

// variables to store the second values
// coming from Strain Sensors
int strain_center_front_1_aSignal = 0; // sensorvalue10
int strain_center_front_2_aSignal = 0;
int strain_center_front_3_aSignal = 0;
int strain_center_back_1_aSignal = 0;
int strain_center_back_2_aSignal = 0;
int strain_center_back_3_aSignal = 0;
int strain_backseat_1_aSignal = 0;
int strain_backseat_2_aSignal = 0;
int strain_backseat_3_aSignal = 0; //sensorvalue18

//variables de % de voltaje:

int strain_center_front_1_aSignalPercent = 0;
int strain_center_front_2_aSignalPercent = 0;
int strain_center_front_3_aSignalPercent = 0;
int strain_center_back_1_aSignalPercent = 0;
int strain_center_back_2_aSignalPercent = 0;
int strain_center_back_3_aSignalPercent = 0;
int strain_backseat_1_aSignalPercent = 0;
int strain_backseat_2_aSignalPercent = 0;
int strain_backseat_3_aSignalPercent = 0; 

// strain total for each strain sensor:
String strain_center_front_1_total = "";


void setup() {
  Serial.begin (9600);
  pinMode(vibration_backseat_top,INPUT); //vibration son digitales
  pinMode(vibration_backseat_bottom,INPUT);
  pinMode(vibration_front_right,INPUT);
  pinMode(vibration_front_left,INPUT);
} 


void loop() 
{
  
  start_time=0;
  int counts_of_ones_1=0;
  int counts_of_ones_2=0;
  int counts_of_ones_3=0;
  int counts_of_ones_4=0;

  while ((start_time) <= 500)
  {
    val_vib_pin1=digitalRead(vibration_backseat_top);
    val_vib_pin2=digitalRead(vibration_backseat_bottom);
    val_vib_pin3=digitalRead(vibration_front_right);
    val_vib_pin4=digitalRead(vibration_front_left);
    if ( val_vib_pin1 == 1) 
    {
      counts_of_ones_1 = counts_of_ones_1 + 1;
    }
    if ( val_vib_pin2 == 1) 
    {
      counts_of_ones_2 = counts_of_ones_2 + 1;
    }
    if ( val_vib_pin3 == 1) 
    {
      counts_of_ones_3 = counts_of_ones_3 + 1;
    }
    if ( val_vib_pin4 == 1) 
    {
      counts_of_ones_4 = counts_of_ones_4 + 1;
    }
  }

  frequency1 = (String)(counts_of_ones_1 / (.200));
  
  // aSignal means = analog signal, it does not have a value persay
  strain_center_front_1_aSignal = analogRead(strain_center_front_1);
  strain_center_front_2_aSignal = analogRead(strain_center_front_2);
  strain_center_front_3_aSignal = analogRead(strain_center_front_3);
  strain_center_back_1_aSignal = analogRead(strain_center_back_1);
  strain_center_back_2_aSignal = analogRead(strain_center_back_2);
  strain_center_back_3_aSignal = analogRead(strain_center_back_3);
  strain_backseat_1_aSignal = analogRead(strain_backseat_1);
  strain_backseat_2_aSignal = analogRead(strain_backseat_2);
  strain_backseat_3_aSignal = analogRead(strain_backseat_3);  
  
  // The 0 to 700 analog value represents the voltage from 0V to aproximately ~3.5V
  strain_center_front_1_aSignalPercent =  map(strain_center_front_1_aSignal, 0, 700, 0, 100);
  strain_center_front_2_aSignalPercent = map(strain_center_front_2_aSignal, 0, 700, 0, 100);
  strain_center_front_3_aSignalPercent = map(strain_center_front_3_aSignal, 0, 700, 0, 100);
  strain_center_back_1_aSignalPercent = map(strain_center_back_1_aSignal, 0, 700, 0, 100);
  strain_center_back_2_aSignalPercent = map(strain_center_back_2_aSignal, 0, 700, 0, 100);
  strain_center_back_3_aSignalPercent = map(strain_center_back_3_aSignal, 0, 700, 0, 100);
  strain_backseat_1_aSignalPercent = map(strain_backseat_1_aSignal, 0, 700, 0, 100);
  strain_backseat_2_aSignalPercent = map( strain_backseat_2_aSignal, 0, 700, 0, 100);
  strain_backseat_3_aSignalPercent = map(strain_backseat_3_aSignal, 0, 700, 0, 100); 


  // This is to test one of the sensors output value.
  Serial.print("aSignal: ");
  Serial.print(strain_center_front_1_aSignal);
  Serial.print("|");
  Serial.print(strain_center_front_1_aSignalPercent);
  Serial.println("%");
  
  SCF_1_Vr = ((strain_center_front_1_aSignalPercent*factor_V)/INPUT_V) - (UNSTRAINED_OUTPUT_V/INPUT_V);
  strain_center_front_1_total = (String)(-(4*SCF_1_Vr)/(GAUGE_FACTOR*(1+2*(SCF_1_Vr))));
 
  Serial.flush();
  Serial.print(frequency1 + "," + strain_center_front_1_total);
  Serial.write(frequency1 + "," + strain_center_front_1_total);
  Serial.flush();
}
