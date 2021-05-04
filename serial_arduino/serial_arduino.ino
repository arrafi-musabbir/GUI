String incomingByte = "" ;  
  
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

  while(1)
  {
    Serial.println("ready");
    if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');

    if(incomingByte.length() >= 20) {
      Serial.println("successful");
      for(int i=0;i<5;i++){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(500);
      digitalWrite(LED_BUILTIN, LOW);
      delay(500);}
      break;
    }

    else{

     Serial.println("invald input");

    }

  }

  }
  
}

void loop() {
  
}
  
