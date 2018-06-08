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

# seta input e output
GPIO.setup(pinTrig, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

while True:
	
        # ping
	GPIO.output(pinTrig, True)
        #
	time.sleep(0.75)
        #
        GPIO.output(pinTrig, False)

	startTime = time.time()
	stopTime = time.time()

        # pong
	while 0 == GPIO.input(pinEcho):
		startTime = time.time()

	while 1 == GPIO.input(pinEcho):
		stopTime = time.time()

        # calcula distancia
	TimeElapsed = stopTime - startTime
	distance = (TimeElapsed * 34300) / 2

	print ("Dist: %.1f cm" % distance)
time.sleep(0.75)
