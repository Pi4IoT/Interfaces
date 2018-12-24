#include <SoftwareSerial.h>

#define RN_42_Rx 10
#define RN_42_Tx 11

SoftwareSerial mySerial(RN_42_Rx, RN_42_Tx); // RX, TX
char myChar ;

void setup() {
  Serial.begin(115200);   
  Serial.println("Monitor:");

  mySerial.begin(115200);
  mySerial.println("Arduino -> RN-42"); //Kommt immer an
}

void loop(){

  if (mySerial.available())
    Serial.write(mySerial.read());
  if (Serial.available())
    mySerial.write(Serial.read());
   
}
