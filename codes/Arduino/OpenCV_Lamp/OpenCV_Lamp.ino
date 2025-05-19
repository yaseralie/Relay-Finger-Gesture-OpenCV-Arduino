String readString;

void setup() {
  // Register relay (output)
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);

  delay(2000);
  //Matikan semua relay untuk awal
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
  delay(500);

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

    if (readString.indexOf("1on") >= 0)
    {
      digitalWrite(8, LOW);
      Serial.print("Lamp #1 turn ON");
    }

    if (readString.indexOf("1off") >= 0)
    {
      digitalWrite(8, HIGH);
      Serial.print("Lamp #1 turn OFF");
    }

    if (readString.indexOf("2on") >= 0)
    {
      digitalWrite(9, LOW);
      Serial.print("Lamp #2 turn ON");
    }

    if (readString.indexOf("2off") >= 0)
    {
      digitalWrite(9, HIGH);
      Serial.print("Lamp #2 turn OFF");
    }

    if (readString.indexOf("3on") >= 0)
    {
      digitalWrite(10, LOW);
      Serial.print("Lamp #3 turn ON");
    }

    if (readString.indexOf("3off") >= 0)
    {
      digitalWrite(10, HIGH);
      Serial.print("Lamp #3 turn OFF");
    }

    if (readString.indexOf("4on") >= 0)
    {
      digitalWrite(11, LOW);
      Serial.print("Lamp #4 turn ON");
    }

    if (readString.indexOf("4off") >= 0)
    {
      digitalWrite(11, HIGH);
      Serial.print("Lamp #4 turn OFF");
    }
    
    readString = "";
  }
}
