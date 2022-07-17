#pragma once

#include <Arduino.h>

class DcMotor {
protected:
  int en;
  int in1;
  int in2;
  int speed;

public:
  DcMotor(int in1, int in2, int en);
  int getSpeed() { return speed; }
  void setSpeed(int speed);
  void forward();
  void backward();
  void stop();
};