int analogPin = 3;
int data = 0;
void setup() 
{ 
  Serial.begin(9600);
}

void loop() 
{
  data = analogRead(analogPin);
  Serial.println(data);
  //Serial.println("hola");
  //Serial.println("Rick");
}
