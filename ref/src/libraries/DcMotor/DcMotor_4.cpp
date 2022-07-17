#include <DcMotor_4.h>

// DcMotor_4::DcMotor_4(int RM_E, int RM_1, int RM_2, int LM_E, int LM_1, int LM_2): RM_1(RM_1), RM_2(RM_2), RM_E(RM_E), LM_1(LM_1), LM_2(LM_2), LM_E(LM_E) {
DcMotor_4::DcMotor_4(){
  speed = 120;
  pinMode(RM_E, OUTPUT);
  pinMode(RM_1, OUTPUT);
  pinMode(RM_2, OUTPUT);
  pinMode(LM_E, OUTPUT);
  pinMode(LM_1, OUTPUT);
  pinMode(LM_2, OUTPUT);

  Serial.begin(9600);
  Serial.println("pinMode on");
}

void DcMotor_4::setSpeed(int speed){
  this->speed=speed;
  analogWrite(RM_E,speed);
  analogWrite(LM_E,speed);
}

void DcMotor_4::forward() {
  digitalWrite(RM_1, HIGH);
  digitalWrite(RM_2, !HIGH);
  digitalWrite(LM_1, HIGH);
  digitalWrite(LM_2, !HIGH);

  analogWrite(RM_E, speed);  // 우측 모터 속도값
  analogWrite(LM_E, speed);   // 좌측 모터 속도값
}

void DcMotor_4::backward() {
  digitalWrite(RM_1, LOW);
  digitalWrite(RM_2, !LOW);
  digitalWrite(LM_1, LOW);
  digitalWrite(LM_2, !LOW);

  analogWrite(RM_E, speed);  // 우측 모터 속도값
  analogWrite(LM_E, speed);   // 좌측 모터 속도값
}

void DcMotor_4::stop() {
  digitalWrite(RM_1, HIGH);
  digitalWrite(RM_2, !HIGH);
  digitalWrite(LM_1, HIGH);
  digitalWrite(LM_2, !HIGH);

  analogWrite(RM_E, 0);  // 우측 모터 속도값
  analogWrite(LM_E, 0);   // 좌측 모터 속도값
}

void DcMotor_4::right(){
  digitalWrite(RM_1, LOW);
  digitalWrite(RM_2, !LOW);
  digitalWrite(LM_1, HIGH);
  digitalWrite(LM_2, !HIGH);

  analogWrite(RM_E, max(speed * 0.2, 50));  // 우측 모터 속도값
  analogWrite(LM_E, min(speed * 1.2, 255));   // 좌측 모터 속도값
}

void DcMotor_4::left(){
  digitalWrite(RM_1, HIGH);
  digitalWrite(RM_2, !HIGH);
  digitalWrite(LM_1, LOW);
  digitalWrite(LM_2, !LOW);

  analogWrite(RM_E, min(speed * 1.2, 255));  // 우측 모터 속도값
  analogWrite(LM_E, max(speed * 0.2, 50));   // 좌측 모터 속도값
}
