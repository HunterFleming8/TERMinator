#include <Servo.h>

Servo servoB;
Servo servoS;
Servo servoE;

int servoBPos=0;
int servoSPos=0;
int servoEPos=0;

void setup()
{
  servoB.attach(2);
  servoS.attach(4);
  servoE.attach(3);
}

void loop(){

{//Base servo
  for(servoBPos=0;servoBPos<180;servoBPos++)
  {
    servoB.write(servoBPos);
    delay(100);
  }
  for(servoBPos=180;servoBPos>0;servoBPos--)
  {
    servoB.write(servoBPos);
    delay(100);
  }
}
{ //Shoulder servo
    for(servoSPos=0;servoSPos<180;servosSPos++)
  {
    servoS.write(servoSPos);
    delay(100);
  }
  for(servoSPos=180;servoSPos>0;servoSPos--)
  {
    servoS.write(servoSPos);
    delay(100);
  }
}
{//Elbow motor
    for(servoEPos=0;servoEPos<180;servoEPos++)
  {
    servoE.write(servoEPos);
    delay(100);
  }
  for(servoEPos=180;servoEPos>0;servoEPos--)
  {
    servoE.write(servoEPos);
    delay(100);
  }
}}


