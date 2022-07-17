#include <ColorLed.h>

ColorLed::ColorLed(int red, int green, int blue):
  red(red), green(green), blue(blue) {

}

void ColorLed::rgb(int r, int g, int b) {
  red.setValue(r);
  green.setValue(g);
  blue.setValue(b);
}
  
void ColorLed::off(){
  // red.off();
  // green.off();
  // blue.off();

  rgb(0,0,0);
}

void ColorLed::random(){
  int r = ::random(256);
  int g = ::random(256);
  int b = ::random(256);
}