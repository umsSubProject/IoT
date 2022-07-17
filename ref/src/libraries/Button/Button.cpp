#include "Button.h"

Button::Button(int pin): pin(pin) {
  pinMode(pin, INPUT_PULLUP);
  callback = NULL;
}

void Button::setCallback(button_callback_t callback) {
  this -> callback = callback;
}


void Button::check() {      // 버튼이 눌러졌는지 체크
  bool o_sw, n_sw;
  
  o_sw = digitalRead(pin);
  delay(10);    // 채터링 방지
  n_sw = digitalRead(pin);

  if(o_sw == 1 && n_sw == 0){     // 버튼을 누른 시점
    if(callback != NULL) {
      callback();
    }
  }
}

int Button::read() {    // 누른 경우 H, 뗀 경우 L 리턴
  return !digitalRead(pin);
}

void Button::attachInterrupt(button_callback_t callback, int mode) {
  ::attachInterrupt(digitalPinToInterrupt(pin), callback, mode);
}

bool Button::debounce() {
  unsigned long t2 = millis();
  if((t2-t1) < 200) return false;

  t1 = t2;
  return true;
}