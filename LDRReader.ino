void setup() {
  // put your setup code here, to run once:
pinMode(8, INPUT);
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
while(1)
{
  if(digitalRead(8)==0)
    Serial.println('0');
  else
    Serial.println('1');
  //delay(5);
    
}
}
