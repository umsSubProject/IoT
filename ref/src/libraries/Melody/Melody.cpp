#include <Melody.h>

Melody::Melody(int pin, int *notes, int *durations, int length): pin(pin), notes(notes), durations(durations), length(length){
  pinMode(pin, OUTPUT);
  cur_ix = -1;
  note_duration = 0;
  b_play = false;
  old_time = millis();
}

void Melody::stop() {
  b_play = false;
}

void Melody::play() {
  b_play = true;
  cur_ix = -1;
  note_duration = 0;
  old_time = millis();
}
void Melody::replay() {
  b_play=true;
}

int Melody::toggle(bool bpause) {
  if(b_play) {
    stop();
  } else {
    if(bpause) {
      replay();
    } else {
      play();
    }
  }
  return b_play;
}

int Melody::getNote() {
  if(!b_play) return 0;
  
  return notes[cur_ix];
}

void Melody::run() {
  if(!b_play) return;

  long current = millis();
  long diff = current - old_time;

  if(diff >= note_duration) {
    int pauseBetweenNotes = note_duration * 0.3;
    delay(pauseBetweenNotes);
    
    cur_ix = (cur_ix + 1)%length;
    note_duration = 1000 / durations[cur_ix];
    tone(pin, notes[cur_ix], note_duration);
    old_time = millis();
  }
}
