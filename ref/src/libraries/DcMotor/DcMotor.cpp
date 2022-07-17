#include <DcMotor.h>

DcMotor::DcMotor(int in1, int in2, int en): in1(in1), in2(in2), en(en) {
  speed = 0;
  pinMode(en, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
}

void DcMotor::setSpeed(int speed){
  this->speed=speed;
  analogWrite(en,speed);
}

void DcMotor::forward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
}

void DcMotor::backward() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
}

void DcMotor::stop() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
}