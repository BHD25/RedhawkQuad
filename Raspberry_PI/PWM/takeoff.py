import time
import serial
import autopilot
import RPi.GPIO as GPIO
from RPIO import PWM
import socket
from threading import Thread

MAX_LENGTH = 4096

GPIO.setmode(GPIO.BCM)

GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#ser = serial.Serial('/dev/ttyACM0', 115200)

# 1 roll
# 2 pitch
# 3 throttle
# 4 yaw
# 5 mode

# 6 dummy1
# 7 dummy2
# 8 dummy3

def handle(clientsocket):
	print('Made connection')
	while(1):
		buf = clientsocket.recv(MAX_LENGTH)
		navigating = 0
		movDirection = 2
		search = 0
		serInput = ''
		if(buf == 'takeoff'):
			autopilot.initialize()
			autopilot.takeOff()
			navigating = 1

		if buf == '': return

		while(navigating == 1):
			#serInput = ser.readline()
			sensor1 = GPIO.input(9)
			sensor2 = GPIO.input(7)
			sensor3 = GPIO.input(8)
			sensor4 = GPIO.input(11)
			buf = clientsocket.recv(MAX_LENGTH)
			if buf == '': return
	
			if(sensor1 == 0 and sensor2 == 1 and movDirection == 2):
				autopilot.stop()
				autopilot.forward()
				movDirection = 1
				print('Moving forward\n')

			#else if(sensor1 == 0 && sensor2 == 1 && movDirection == 1):


			if(sensor1 == 0 and sensor2 == 0 and movDirection == 4):
				autopilot.stop()
				time.sleep(.3)
				autopilot.forward()
				time.sleep(.5)
				autopilot.stop()
				movDirection = 2
				autopilot.strafeR()
				time.sleep(1)
				autopilot.stop()
				print('Wall vanished\n')

			if(sensor1 == 1 and sensor4 == 0 and sensor2 == 1 and movDirection == 1):
				autopilot.stop()
				time.sleep(.3)
				autopilot.strafeL()
				movDirection = 4
				print('Moving left\n')

			if(sensor3 == 1 and sensor2 == 0 and movDirection == 2):
				autopilot.strafeR()
				movDirection = 2
				print('Moving right\n')		

			if(sensor1 == 1 and sensor2 == 1 and sensor3 == 1 and sensor4 == 1):
				autopilot.land()
				time.sleep(5)
				flying = 0
				print('Can\'t fly\n')

			if(sensor1 == 1 and sensor4 == 1):
				navigating = 0
				autopilot.stop()
				autopilot.turnR()
				time.sleep(.5)
				autopilot.stop()
				search = 1
				print('Reached back corner\n')

			if(buf == "kill"):
				autopilot.land()
				time.sleep(10)
				autopilot.landed()
				flying = 0
				print('Killing operation\n')

		seen = 0

		#while(search == 1 and buf != 'stop'):
			# Capture image and look for ball
		


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 1000
HOST = '192.168.0.101'

serversocket.bind((HOST, PORT))
serversocket.listen(10)

while 1:
	print('Waiting for connection!')
	#accept connections from outside
	(clientsocket, address) = serversocket.accept()

	ct = Thread(target=handle, args=(clientsocket,))
	ct.run()
		

#time.sleep(5)
#autopilot.land()
#time.sleep(10)
PWM.cleanup()

