#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
const int tasterPin = 2;
const int reedPin = 3;
int tasterStatus = 0;
int reedStatus = 0;
  
void setup() {
  pinMode(tasterPin, INPUT);
  pinMode(reedPin, INPUT);
  Serial.begin(9600);
  Serial.println("Pi4IoT");
  mySerial.begin(115200);
  mySerial.println("Hello Viewer");
}

void loop() {
    if (mySerial.available()) {
        Serial.write(mySerial.read());
    }
    if (Serial.available()) {
        mySerial.write(Serial.read());
    }
    tasterStatus = digitalRead(tasterPin);
    if (tasterStatus == LOW){   
        mySerial.println("Taster");
        Serial.println("Taster");
        delay(500);
    } 
    reedStatus = digitalRead(reedPin);
    if (reedStatus == LOW){   
        mySerial.println("Reed Switch");
        Serial.println("Reed Switch");
        delay(500);
    }
}
