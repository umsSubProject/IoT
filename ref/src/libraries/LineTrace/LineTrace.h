#pragma once

#include <Arduino.h>

class LineTrace {
  protected:

    // int speed;
    int SL = 1;
    int SC = 1;
    int SR = 1;

    // int L_Line = A5; // 왼쪽 라인트레이서
    // int C_Line = A4; // 가운데 라인트레이서
    // int R_Line = A2; // 오른쪽 라인트레이서
  
    int L = digitalRead(A5); // 왼쪽 라인트레이서
    int C = digitalRead(A4); // 가운데 라인트레이서
    int R = digitalRead(A2); // 오른쪽 라인트레이서
  public:
    LineTrace();
    String LineValuePrint();
    int setValue(int L, int C, int R);
    bool forward_bool(int L, int C, int R);
    bool right_bool(int L, int C, int R);
    bool left_bool(int L, int C, int R);
    bool stop_bool(int L, int C, int R);
    void ErrFix(int L, int C, int R);
    void setSpeed(int speed);
    bool pause(int L, int C, int R);
};