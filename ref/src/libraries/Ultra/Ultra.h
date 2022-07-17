#pragma once

#include <Arduino.h>

typedef void (*ultra_callback_t)();

class Ultra {
protected:
  int trig;
  int echo;
  int threshold;            // 기준 거리
  ultra_callback_t on_f;    // 기준 거리 내로 진입한 경우 호출 할 함수
  ultra_callback_t off_f;   // 기준 거리를 벗어난 경우 호출 할 함수
  int state;    // 벗어난 경우 false, 진입한 경우 True

public:
  Ultra(int echo, int trig);
  int getDistance();
  void setThreshold(int t, ultra_callback_t on_f, ultra_callback_t off_f);
  int run();
};