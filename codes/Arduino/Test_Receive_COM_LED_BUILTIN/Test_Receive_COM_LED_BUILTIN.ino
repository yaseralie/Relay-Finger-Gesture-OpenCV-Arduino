String readString;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  while (Serial.available()) {
    delay(3);
    char c = Serial.read();
    readString += c;
  }

  if (readString.length() > 0) {
    Serial.println(readString);

    if (readString.indexOf("on") >= 0)
    {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.print("Lamp turn ON");
    }

    if (readString.indexOf("off") >= 0)
    {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.print("Lamp turn OFF");
    }
    readString = "";
  }
}
