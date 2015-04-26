import time
import serial
import autopilot
import RPi.GPIO as GPIO
from RPIO import PWM
import socket
from threading import Thread

MAX_LENGTH = 4096

#isKill = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#def hasBeenKilled(channel):
#	isKill = 1

ser = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=3.0)
ser.open()

# 1 roll
# 2 pitch
# 3 throttle
# 4 yaw
# 5 mode

# 6 dummy1
# 7 dummy2
# 8 dummy3

#GPIO.add_event_detect(10, GPIO.RISING, callback=hasBeenKilled, bouncetime=300)

def handle(clientsocket):
	print('Made connection\n')
	try:
		flying = 1
		while(flying):
			#print('YO MAN')
			buf = clientsocket.recv(MAX_LENGTH)
			navigating = 0
			#autopilot.initialize()
			movDirection = 22
			search = 0
			serInput = ''
			if(buf == 'takeoff'):
				autopilot.initialize()
				autopilot.takeOff()
				navigating = 1

			if buf == '': return

			while(navigating == 1):
				print("In navigation\n")
				serInput = ser.readline()
				print(repr(serInput))
				sensor1 = GPIO.input(9)
				#print("Sensor1 = " + str(sensor1))
				sensor2 = GPIO.input(7)
				#print("Sensor2 = " + str(sensor2))
				sensor3 = GPIO.input(8)
				#print("Sensor3 = " + str(sensor3))
				sensor4 = GPIO.input(11)
				#print("Sensor4 = " + str(sensor4))
				#buf = clientsocket.recv(MAX_LENGTH)
				#if buf == '': return
				isKill = GPIO.input(15)
				print(isKill)
	
				# Initial move right
				if(sensor3 == 1 and sensor1 == 0 and sensor4 == 0 and sensor2 == 0 and movDirection == 2):
					#print("Initial move right")
					autopilot.strafeR()
					autopilot.forward()
					movDirection = 2
					#print('Moving right\n')
	
				if(sensor3 == 0 and sensor1 == 0 and sensor4 == 0 and sensor2 == 0 and movDirection == 2):
					autopilot.strafeR()
					autopilot.backward()
					movDirection = 2
					#print('Moving right-ADJ\n')
	
				# Found right wall, start moving forward
				if(sensor1 == 0 and sensor2 == 1 and (sensor3 == 0 or sensor3 == 1) and sensor4 == 0 and movDirection == 2):
					#print("Found right wall, start moving forward")
					autopilot.stop()
					time.sleep(1)
					autopilot.forward()
					movDirection = 1
					#print('Moving forward\n')
	
				# Following right wall
				if(sensor1 == 0 and sensor2 == 1 and sensor3 == 0 and sensor4 == 0 and movDirection == 1):
					#print("Following right wall")
					#autopilot.stop()
					autopilot.forward()
					autopilot.strafeL()
					#movDirection = 1
					#print('Moving forward\n')
	
				if(sensor1 == 0 and sensor2 == 0 and sensor3 == 0 and sensor4 == 0 and movDirection == 1):
					#autopilot.stop()
					autopilot.forward()
					autopilot.strafeR()
					#movDirection = 1
					#print('Moving forward\n')
	
				# Hit a right back corner
				if(sensor1 == 1 and sensor4 == 0 and sensor2 == 1 and sensor3 == 0 and movDirection == 1):
					#print("Hit a right back corner")
					autopilot.stop()
					#time.sleep(.3)
					autopilot.strafeL()
					movDirection = 4
					#print('Moving left\n')
	
				# Moving left following front wall
				if(sensor1 == 1 and sensor4 == 0 and sensor2 == 0 and sensor3 == 0 and movDirection == 4):
					#print("Moving left following front wall")
					autopilot.stop()
					#time.sleep(.3)
					autopilot.strafeL()
					autopilot.backward()
					#movDirection = 4
					#print('Moving left\n')
	
				if(sensor1 == 0 and sensor4 == 0 and sensor2 == 0 and sensor3 == 0 and movDirection == 4):
					autopilot.stop()
					#time.sleep(.3)
					autopilot.strafeL()
					autopilot.forward()
					#movDirection = 4
					#print('Moving left\n')
	
				# Lost front wall
				if(sensor1 == 0 and sensor2 == 0 and sensor3 == 0 and sensor4 == 0 and movDirection == 4):
					#print("Lost front wall")
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
					#print('Wall vanished\n')
	
				# Found back left corner
				if(sensor1 == 1 and sensor2 == 0 and sensor3 == 0 and sensor4 == 1 and movDirection == 4):
					#print("Found back left corner")
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
					#print("No direction to fly")
					autopilot.land()
					time.sleep(5)
					flying = 0
					#print('Can\'t fly\n')
	
				# Emergency kill command
				if(buf == "kill"):
					autopilot.land()
					time.sleep(10)
					autopilot.landed()
					flying = 0
					#print('Killing operation\n')
	
				if(isKill):
					autopilot.throttleCut()
					flying = 0
					return
					#print('Killed manually')
	
			seen = 0
	
			#while(search == 1 and buf != 'stop'):
				# Capture image and look for ball
	except:
		print('Error occured, closing socket')
		clientsocket.shutdown()
		clientsocket.close()


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

