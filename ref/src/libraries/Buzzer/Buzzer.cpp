#include <Buzzer.h>

Buzzer::Buzzer(int pin): pin(pin) {
  state = LOW;
  off_time = 0;
  on_time = 100;
  old_time = millis();
  pinMode(pin, OUTPUT);
}

void Buzzer::run() {
  unsigned long cur, diff;

  if(bstop) return;

  cur = millis();
  diff = cur - old_time;
  
  if(state) {
    if(diff > on_time) {
      digitalWrite(pin, LOW);
      state = LOW;
      old_time = cur;
      bstop = true;
    }
  } else {
    if(diff > off_time) {
      digitalWrite(pin, HIGH);
      state = HIGH;
      old_time = cur;
    }
  }
}

void Buzzer::setOfftime(int off_time) {
  this->off_time = off_time;
  bstop = false;

}
