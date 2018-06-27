// define pinos a serem usados
#define trigPin 8
#define echoPin 7

// define as vars que serao usadas
long dist, duration;

void setup() {
	
	// comeca o serial e comunic. com o console
	Serial.begin(9600);

	// define os pinos de saida e entrada
	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);	

}

void loop() {

	// <ping>
	digitalWrite(trigPin, LOW);
	delay(3);

	digitalWrite(trigPin, HIGH);
	delay(6);

	digitalWrite(trigPin, LOW);
	// </ping>
	
	// <pong>
	duration = pulseIn(echoPin, HIGH);	
	// </pong>

	// calcula a distancia
	dist = (duration/2) / 29;

	// check se esta no alcance
	if (dist >= 300 || dist <= 0){

		// nao devolve valor
		Serial.println("---");
	
	} else {

		// escreve a distancia
		Serial.print(dist);
		Serial.println(" cm(s)")

	}

	delay(75);
}
