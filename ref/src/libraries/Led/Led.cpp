#include "Led.h"    // ""는 현재 디렉토리에서 찾음

Led::Led(int pin): pin(pin) {
  // this->pin = pin;
  pinMode(pin, OUTPUT);
}

void Led::on() {
  digitalWrite(pin, HIGH);
}

void Led::off() {
  digitalWrite(pin, LOW);
}

void Led::setValue(int value) {
  digitalWrite(pin, value);
}

void Led::toggle() {
  int v = digitalRead(pin);
  digitalWrite(pin, !v);
}