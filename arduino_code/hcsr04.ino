#define trigPin 8
#define echoPin 7

void setup() {

	Serial.begin(9600);
	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);

}

void loop() {

	long duration, dist;

	digitalWrite(trigPin, LOW);
	delay(3);

	digitalWrite(trigPin, HIGH);
	delay(10);

	digitalWrite(trigPin, LOW);

	duration = pulseIn(echoPin, HIGH);	

	dist = (duration/2) / 29;

	if (dist >= 300 || dist <= 0){

		Serial.println("---");
	
	} else {

		Serial.print(dist);
		Serial.println(" cm(s)")

	}

	delay(200);

}
