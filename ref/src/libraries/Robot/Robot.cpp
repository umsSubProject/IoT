#include <Robot.h>

Robot::Robot(int in1, int in2, int ena, int in3, int in4, int enb): l_motorl(in1, in2, ena), r_motorl(in3, in4, enb) {
  speed = 0;
}


void Robot::setSpeed(int speed){
  this->speed=speed;
  l_motorl.setSpeed(speed);
  r_motorl.setSpeed(speed);
}

void Robot::forward(){
  l_motorl.forward();
  r_motorl.forward();
}

void Robot::backward(){
  l_motorl.backward();
  r_motorl.backward();
}

void Robot::stop(){
  l_motorl.stop();
  r_motorl.stop();
}

void Robot::turn_left(){
  l_motorl.backward();
  r_motorl.forward();
}

void Robot::turn_right(){
  l_motorl.forward();
  r_motorl.backward();
}