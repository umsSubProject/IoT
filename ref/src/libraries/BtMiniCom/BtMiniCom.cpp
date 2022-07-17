#include <BtMiniCom.h>

BtMiniCom::BtMiniCom(int rx, int tx, btminicom_callback_t)
  : MiniCom(), btSerial(rx, tx), callback(callback){

}

void BtMiniCom::init() {
  MiniCom::init();
  btSerial.begin(9600);
}

String BtMiniCom::readLine(){
  String message="";
  while(btSerial.available()){
    char data = (char)btSerial.read();
    if(data == '\r') continue;
    if(data == '\n') break;

    message += data;
    delay(10);   // 수신 문자열 끊김을 방지
  }
  return message;
}

void BtMiniCom::send(String msg) {
  btSerial.println(msg);
}

void BtMiniCom::run() {
  String msg = readLine();
  if(msg != "" && callback != NULL) {
    callback(msg);
  }
  MiniCom::run();
}