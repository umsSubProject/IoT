#include <Ultra.h>

Ultra::Ultra(int echo, int trig): echo(echo), trig(trig) {
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  on_f = NULL;
  off_f = NULL;
  state = false;  
}

int Ultra::getDistance() {
  digitalWrite(trig, HIGH);
  delayMicroseconds(100);
  digitalWrite(trig, LOW);

  int distance = pulseIn(echo, HIGH) / 58;    // 실수 계산보다, 정수 계산이 더 빠름.
  return distance;
}

void Ultra::setThreshold(int t, ultra_callback_t on_f, ultra_callback_t off_f) {
  threshold = t;
  this->on_f = on_f;
  this->off_f = off_f;
}

int Ultra::run() {
  int distance = getDistance();
  if(!state && distance <=threshold) {
    state = true;
    if(on_f != NULL) {
      on_f();
    }
  } else if(state && (distance == 0 || distance > (threshold+2))) {    // 기준 거리를 벗어난 경우
    state = false;
    if(off_f != NULL) {
      off_f();
    }
  }

  if(distance == 0 || distance > threshold) {
    return 0;
  }
  
  return distance;
}