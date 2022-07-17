#pragma once

#include <Arduino.h>

class DcMotor_4 {
protected:
  int RM_E = 5;
  int LM_E = 6;
  int RM_1 = 8;
  int RM_2 = 9;
  int LM_1 = 10;
  int LM_2 = 11;
  int speed;

public:
  DcMotor_4();
  int getSpeed() { return speed; }
  void setSpeed(int speed);
  void forward();
  void backward();
  void stop();
  void right();
  void left();
};