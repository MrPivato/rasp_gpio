#importa as livrarias  necessarias
import RPi.GPIO as GPIO # da GPIO
import time             # do tempo
import signal           # eventos assincronos
import sys              # info sobre o interpretador

# usar os pinos numerados
GPIO.setmode(GPIO.BCM)

# define os pinos a serem usados
pinTrig = 18
pinEcho = 24

def close(signal, frame):
	GPIO.cleanup() 
	sys.exit(0)

signal.signal(signal.SIGINT, close)

# seta os pinos de input e output
GPIO.setup(pinTrig, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

while True:
	
        # <ping>
	GPIO.output(pinTrig, True)
	time.sleep(0.75)
        GPIO.output(pinTrig, False)

	startTime = time.time()
	stopTime = time.time()
        # </ping>

        # <pong>
	while 0 == GPIO.input(pinEcho):
		startTime = time.time()

	while 1 == GPIO.input(pinEcho):
		stopTime = time.time()
        # </pong>

        # calcula distancia
	TimeElapsed = stopTime - startTime # T2 - t1
	distance = (TimeElapsed * 34300) / 2

        # escreve a distancia
	print ("Dist: %.1f cm" % distance)
time.sleep(0.75)
