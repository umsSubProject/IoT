#pragma once

#include <Arduino.h>
#include <SoftwareSerial.h>
#include <MiniCom.h>

typedef void (*btminicom_callback_t)(String message);

class BtMiniCom : public MiniCom {
  protected:
    SoftwareSerial btSerial;
    btminicom_callback_t callback;    // 메세지 수신 시 호출할 함수 포인터

  public:
    BtMiniCom(int rx, int tx, btminicom_callback_t callback);
    void init();
    String readLine();            // \r\n를 제외한 문자열을 리턴
    void send(String msg);   //메세지 전송
    void run();
};