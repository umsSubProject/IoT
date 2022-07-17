#pragma once

#include <PWMLed.h>

class ColorLed {
protected:
  PWMLed red;
  PWMLed blue;
  PWMLed green;

public:
  ColorLed(int red, int green, int blue);
  void rgb(int r, int g, int b);
  void off();
  void random();
};