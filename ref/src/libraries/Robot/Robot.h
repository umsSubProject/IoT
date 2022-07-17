#pragma once

#include <DcMotor.h>

class Robot{
protected:
  DcMotor l_motorl;
  DcMotor r_motorl;
  int speed;
public:
  Robot(int in1, int in2, int ena,    // l_motor
        int in3, int in4, int enb);   // r_motor
  int getSpeed() {return speed;}
  void setSpeed(int speed);
  void forward();
  void backward();
  void stop();
  void turn_left();
  void turn_right();
  
};