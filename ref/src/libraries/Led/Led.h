#pragma once      // 중복된 include를 한 번만 실행하게 해줌

#include <Arduino.h>    // <>는 includePath 경로에서 찾음

class Led {
  protected:
    int pin;    // 연결할 핀 번호

  public:
    Led(int pin);

    void on();
    void off();
    void setValue(int value);
    void toggle();
};