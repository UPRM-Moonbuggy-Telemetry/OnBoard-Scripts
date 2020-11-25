#define VIBRATION_SENSOR_PIN 3
 
int motion_detected = LOW;
 
void setup() {
 Serial.begin(115200); // cambiarlo dependiendo del pi
}
 
void loop() {
 motion_detected = digitalRead(VIBRATION_SENSOR_PIN);
 Serial.println(motion_detected);
 delay(100); // chequear con port del pi 
}

/*CODE-
int vibr_pin=3;
int LED_Pin=13;
void setup() {
  pinMode(vibr_pin,INPUT);
  pinMode(LED_Pin,OUTPUT);
  */
}

/*void loop() {
  int val;
  val=digitalRead(vibr_pin);
  if(val==1)
  {
    digitalWrite(LED_Pin,HIGH);
    delay(1000);
    digitalWrite(LED_Pin,LOW);
    delay(1000);
   }
   else
   digitalWrite(LED_Pin,LOW);
}
 


Pin- 
led-12
signal pin-3
*/
