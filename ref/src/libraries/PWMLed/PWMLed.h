#pragma once

#include "Led.h"

class PWMLed: public Led {
  protected:
    int value;

  public:
    PWMLed(int pin, int vlaue=0);
    void setValue(int value);

};