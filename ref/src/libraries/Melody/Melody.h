#pragma once

#include <Arduino.h>


class Melody {
protected:
  int pin;
  int *notes;
  int *durations;
  int length;
  long old_time;
  int note_duration;
  boolean b_play;
  int cur_ix;

public:
  Melody(int pin, int *tones, int *durations, int lenght);
  void stop();
  void play();
  void run();
  int toggle(bool bpause=false);
  void replay();
  int getNote();
};