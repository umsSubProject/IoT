#include "PWMLed.h"

PWMLed::PWMLed(int pin, int value): Led(pin), value(value) {        // : 공백 시 Led() 생략됨
  analogWrite(pin, value);
}

void PWMLed::setValue(int value) {
  this -> value = value;
  analogWrite(pin, value);
}