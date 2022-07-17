#pragma once

#include <Arduino.h>

typedef void (*button_callback_t)();    // 함수에 대한 포인터를 button_callback_t로 정의

class Button{
  protected:
    int pin;
    // void (*callback)();   // 콜백 함수(함수에 대한 포인터)
    button_callback_t callback;
    unsigned long t1;     // unsigned : 부호가 없다 = 양수만 가능

  public:
    Button(int pin);
    void setCallback(button_callback_t callback);
    void check();
    int read();
    void attachInterrupt(button_callback_t callback, int mode);
    bool debounce();
};