#pragma once

#include <Arduino.h>

class Buzzer{
  protected:
    int pin;                  // 핀번호
    int state;                // 소리 출력 상태
    int off_time;             // 꺼져야 할 시간 간격
    int on_time;             // 꺼져야 할 시간 간격
    unsigned long old_time;   // 이전 상태 변화 시간
    bool bstop;

  public:
    Buzzer(int pin);
    void run();
    void stop() {
      bstop = true;
      digitalWrite(pin, LOW);
      };
    void setOfftime(int off_time);
};