const int outputPin = 8; // defines output as pin 8
const int on = 1000; // sets how long the sensor sends out a signal
const int off = 1000 - on; // sets how long the sensor stops in between signals
void setup() 
{
  pinMode(outputPin, OUTPUT);    // sets the pin 8 as output
}

void loop() 
{
  digitalWrite(outputPin, HIGH); // sets output on
  delay(on); // turns on signal for duration
  digitalWrite(outputPin, LOW); // sets ouput off
  delay(off); // turns off signal for duration
}
