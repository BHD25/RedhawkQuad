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

			# Initial move right
			if(sensor3 == 1 and sensor1 == 0 and sensor4 == 0 and sensor2 == 0 and movDirection == 2):
				autopilot.strafeR()
				autopilot.forward()
				movDirection = 2
				print('Moving right\n')

			if(sensor3 == 0 and sensor1 == 0 and sensor4 == 0 and sensor2 == 0 and movDirection == 2):
				autopilot.strafeR()
				autopilot.backward()
				movDirection = 2
				print('Moving right\n')

			# Found right wall, start moving forward
			if(sensor1 == 0 and sensor2 == 1 and sensor3 == 0 and sensor4 == 0 and movDirection == 2):
				autopilot.stop()
				autopilot.forward()
				movDirection = 1
				print('Moving forward\n')

			# Following right wall
			if(sensor1 == 0 and sensor2 == 1 and sensor3 == 0 and sensor4 == 0 and movDirection == 1):
				#autopilot.stop()
				autopilot.forward()
				autopilot.strafeL()
				#movDirection = 1
				print('Moving forward\n')

			if(sensor1 == 0 and sensor2 == 0 and sensor3 == 0 and sensor4 == 0 and movDirection == 2):
				#autopilot.stop()
				autopilot.forward()
				autopilot.strafeR()
				#movDirection = 1
				print('Moving forward\n')

			# Hit a right back corner
			if(sensor1 == 1 and sensor4 == 0 and sensor2 == 1 and sensor3 == 0 and movDirection == 1):
				autopilot.stop()
				#time.sleep(.3)
				autopilot.strafeL()
				movDirection = 4
				print('Moving left\n')

			# Moving left following front wall
			if(sensor1 == 1 and sensor4 == 0 and sensor2 == 0 and sensor3 == 0 and movDirection == 4):
				autopilot.stop()
				#time.sleep(.3)
				autopilot.strafeL()
				autopilot.backward()
				#movDirection = 4
				print('Moving left\n')

			if(sensor1 == 0 and sensor4 == 0 and sensor2 == 0 and sensor3 == 0 and movDirection == 4):
				autopilot.stop()
				#time.sleep(.3)
				autopilot.strafeL()
				autopilot.forward()
				#movDirection = 4
				print('Moving left\n')

			# Lost front wall
			if(sensor1 == 0 and sensor2 == 0 and sensor3 == 0 and sensor4 == 0 and movDirection == 4):
				autopilot.stop()
				time.sleep(.3)
				audopilot.strafeL()
				time.sleep(.3)
				autopilot.stop()
				time.sleep(.5)
				autopilot.forward()
				time.sleep(.5)
				autopilot.stop()
				time.sleep(.5)
				movDirection = 2
				while (sensor3 == 0):
					autopilot.strafeR()
					time.sleep(1)
					autopilot.stop()
				print('Wall vanished\n')

			# Found back left corner
			if(sensor1 == 1 and sensor2 == 0 and sensor3 == 0 and sensor4 == 1 and movDirection == 4):
				autopilot.stop()
				time.sleep(1)
				autopilot.turnR()
				time.sleep(1.5)
				autopilot.stop()
				time.sleep(1)
				search = 1
				navigating = 0

			# No direction to fly
			if(sensor1 == 1 and sensor2 == 1 and sensor3 == 1 and sensor4 == 1):
				autopilot.land()
				time.sleep(5)
				flying = 0
				print('Can\'t fly\n')

			# Emergency kill command
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

