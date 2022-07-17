#include <LineTrace.h>
#include <SoftwareSerial.h>

LineTrace::LineTrace(){
  // int speed = 0;
  // int L = digitalRead(A5); // 왼쪽 라인트레이서
  // int C = digitalRead(A4); // 가운데 라인트레이서
  // int R = digitalRead(A2); // 오른쪽 라인트레이서
}
// void LineTrace::setSpeed(int speed){
//   this->speed=speed;
//   DcMotor_4().setSpeed(speed);
// }
// String LineTrace::LineValuePrint(int L, int C, int R){
//   Serial.print("digital : "); Serial.print(L); Serial.print(", "); Serial.print(C); Serial.print(", "); Serial.print(R); Serial.print("  \n ");
//   // Serial.print('\n')
// }

void LineTrace::ErrFix(int L, int C, int R){
  if ( L == 1 && C == 1 && R == 1 ) {   // 0 0 0
    L = SL; C = SC; R = SR;
  }
  else if ( L == 1 && C == 0 && R == 1 ) {   // 1 0 1
    L = SL; C = SC; R = SR;
  }
}

bool LineTrace::forward_bool(int L, int C, int R){

  if (L == 0 && C == 1 && R == 0 || L == 0 && C == 0 && R == 0) {  // 0 1 0
    // car.forward(speed);
    // Serial.println("직진");
    return true;
  } else {
    return false;
  }
}

bool LineTrace::right_bool(int L, int C, int R){
  if (L == 0 && C == 0 && R == 1 || L == 0 && C == 1 && R == 1 ){   // 0 1 1, 0 0 1
    // car.right(speed);
    // Serial.println("우회전");
    return true;
  } else {
    return false;
  }
}

bool LineTrace::left_bool(int L, int C, int R){
  if (L == 1 && C == 0 && R == 0 || L == 1 && C == 1 && R == 0 ){     // 1 1 0, 1 0 0
    // car.left(speed);
    // Serial.println("좌회전");
    return true;
  } else {
    return false;
  }
}

bool LineTrace::stop_bool(int L, int C, int R){
  if ( L == 1 && C == 1 && R == 1 ) {       //  1 1 1
    // car.stop();
    // Serial.println("정지");
    return true;
  } else {
    return false;
  }
}

bool LineTrace::pause(int L, int C, int R){
  if ( L == 1 && C == 0 && R == 1  ) {       //  1 1 1
    // Serial.println("정지");
    return true;
  } else {
    return false;
  }
}