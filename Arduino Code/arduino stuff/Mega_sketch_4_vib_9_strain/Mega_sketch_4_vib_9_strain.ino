#include <elapsedMillis.h>
elapsedMillis start_time;
int frequency1=0;    // variable to store frequency value
int frequency2=0;    //variable to store frequency value
int frequency3=0;    //variable to store frequency value
int frequency4=0;    //variable to store frequency value
int vib_pin1=22;    // digital input pin for vibration sensor
int vib_pin2=24;    // digital input pin for vibration sensor
int vib_pin3=26;    // digital input pin for vibration sensor
int vib_pin4=28;    // digital input pin for vibration sensor
int val_vib_pin1=0;
int val_vib_pin2=0;
int val_vib_pin3=0;
int val_vib_pin4=0;
int counts_of_ones_1=0;
int counts_of_ones_2=0;
int counts_of_ones_3=0;
int counts_of_ones_4=0;
int sensorValue10 = 0; // variable to store the second value coming from the sensor
int sensorValue11 = 0;
int sensorValue12 = 0;
int sensorValue13 = 0;
int sensorValue14 = 0;
int sensorValue15 = 0;
int sensorValue16 = 0;
int sensorValue17 = 0;
int sensorValue18 = 0;
int sensorPin = A0;  // select the input pin for the Strain Gauge
int sensorPin1 = A1;
int sensorPin2 = A2;
int sensorPin3 = A3;
int sensorPin4 = A4;
int sensorPin5 = A5;
int sensorPin6 = A6;
int sensorPin7 = A7;
int sensorPin8 = A8;

void setup() {
  Serial.begin (9600);
  pinMode(vib_pin1,INPUT);
  pinMode(vib_pin2,INPUT);
  pinMode(vib_pin3,INPUT);
  pinMode(vib_pin4,INPUT);
}
void loop() 
{
  val_vib_pin1=digitalRead(vib_pin1);
  val_vib_pin2=digitalRead(vib_pin2);
  val_vib_pin3=digitalRead(vib_pin3);
  val_vib_pin4=digitalRead(vib_pin4);
  start_time=0;
  while ((start_time) <= 200)
  {
    if ( val_vib_pin1 == 1) {
      counts_of_ones_1 = counts_of_ones_1 + 1;
    }
    if ( val_vib_pin2 == 1) {
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
frequency1= counts_of_ones_1/(.2);
frequency2= counts_of_ones_2 /(.200);
frequency3= counts_of_ones_3/(.200);
frequency4= counts_of_ones_4/(.200);

Serial.print(frequency1);
Serial.print(",");
Serial.print(frequency2);
Serial.print(",");
Serial.print(frequency3);
Serial.print(",");
Serial.print(frequency4);
Serial.print(",");

sensorValue10 = analogRead(sensorPin);
sensorValue11 = analogRead(sensorPin1);
sensorValue12 = analogRead(sensorPin2);
sensorValue13 = analogRead(sensorPin3);
sensorValue14 = analogRead(sensorPin4);
sensorValue15 = analogRead(sensorPin5);
sensorValue16 = analogRead(sensorPin6);
sensorValue17 = analogRead(sensorPin7);
sensorValue18 = analogRead(sensorPin8);


Serial.print(sensorValue10);
Serial.print(",");
Serial.print(sensorValue11); 
Serial.print(",");
Serial.print(sensorValue12); 
Serial.print(",");
Serial.print(sensorValue13);
Serial.print(","); 
Serial.print(sensorValue14);
Serial.print(",");
Serial.print(sensorValue15); 
Serial.print(",");
Serial.print(sensorValue16); 
Serial.print(",");
Serial.print(sensorValue17); 
Serial.print(",");
Serial.println(sensorValue18);


}
