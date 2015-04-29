import time
import serial
import autopilot
import RPi.GPIO as GPIO
from RPIO import PWM
import socket
from threading import Thread

MAX_LENGTH = 4096

isKill = 0

GPIO.setmode(GPIO.BCM)

#GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(9, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#def hasBeenKilled(channel):
#	isKill = 1

ser = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=3.0)
ser.open()
ser.flush()

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
			movDirection = 2
			search = 0
			serInput = ''
			sensor1 = 0
			sensor2 = 0
			sensor3 = 0
			sensor4 = 0
			if(buf == 'takeoff'):
				autopilot.initialize()
				autopilot.arm()
				#autopilot.takeOff()
				navigating = 1
	
			if buf == '': return
	
			while(navigating == 1):
				#print("In navigation\n")
				if(ser.inWaiting()):
					serInput = ser.readline()
					#if 'f' in serInput: sensor1 = 1
					#else: sensor1 = 0
					#if 'r' in serInput: sensor2 = 1
					#else: sensor2 = 0
					#if 'b' in serInput: sensor3 = 1
					#else: sensor3 = 0
					#if 'l' in serInput: sensor4 = 1
					#else: sensor4 = 0
					#if 'k' in serInput: isKill = 1
					#else: isKill = 0
				#print("After Serial Read")
				print(serInput)
				#time.sleep(1)
				#sensor1 = GPIO.input(9)
				#print("Sensor1 = " + str(sensor1))
				#sensor2 = GPIO.input(7)
				#print("Sensor2 = " + str(sensor2))
				#sensor3 = GPIO.input(8)
				#print("Sensor3 = " + str(sensor3))
				#sensor4 = GPIO.input(11)
				#print("Sensor4 = " + str(sensor4))
				buf = clientsocket.recv(MAX_LENGTH)
				#if buf == '': return
				#isKill = GPIO.input(15)
				print(isKill)
	
				# Initial move right
				if(sensor3 == 1 and sensor1 == 0 and sensor4 == 0 and sensor2 == 0 and movDirection == 2):
					#print("Initial move right")
					autopilot.strafeR()
					autopilot.forward()
					movDirection = 2
					print('Moving right')
	
				if(sensor3 == 0 and sensor1 == 0 and sensor4 == 0 and sensor2 == 0 and movDirection == 2):
					autopilot.strafeR()
					autopilot.backward()
					movDirection = 2
					print('Moving right-ADJ')
	
				# Found right wall, start moving forward
				if(sensor1 == 0 and sensor2 == 1 and (sensor3 == 0 or sensor3 == 1) and sensor4 == 0 and movDirection == 2):
					#print("Found right wall, start moving forward")
					autopilot.stop()
					time.sleep(1)
					autopilot.forward()
					movDirection = 1
					print('Start Moving forward')
	
				# Following right wall
				if(sensor1 == 0 and sensor2 == 1 and sensor3 == 0 and sensor4 == 0 and movDirection == 1):
					#print("Following right wall")
					#autopilot.stop()
					autopilot.forward()
					autopilot.strafeL()
					#movDirection = 1
					print('Moving forward')
	
				if(sensor1 == 0 and sensor2 == 0 and sensor3 == 0 and sensor4 == 0 and movDirection == 1):
					#autopilot.stop()
					autopilot.forward()
					autopilot.strafeR()
					#movDirection = 1
					print('Moving forward-ADJ')
	
				# Hit a right back corner
				if(sensor1 == 1 and sensor4 == 0 and sensor2 == 1 and sensor3 == 0 and movDirection == 1):
					#print("Hit a right back corner")
					autopilot.stop()
					#time.sleep(.3)
					autopilot.strafeL()
					movDirection = 4
					print('Start Moving left')
	
				# Moving left following front wall
				if(sensor1 == 1 and sensor4 == 0 and sensor2 == 0 and sensor3 == 0 and movDirection == 4):
					#print("Moving left following front wall")
					autopilot.stop()
					#time.sleep(.3)
					autopilot.strafeL()
					autopilot.backward()
					#movDirection = 4
					print('Moving left')
	
				if(sensor1 == 0 and sensor4 == 0 and sensor2 == 0 and sensor3 == 0 and movDirection == 4):
					autopilot.stop()
					#time.sleep(.3)
					autopilot.strafeL()
					autopilot.forward()
					#movDirection = 4
					print('Moving left-ADJ')
	
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
					print('Wall vanished')
					ser.flush()
	
				# Found back left corner
				if(sensor1 == 1 and sensor2 == 0 and sensor3 == 0 and sensor4 == 1 and movDirection == 4):
					print("Found back left corner")
					autopilot.stop()
					time.sleep(1)
					autopilot.turnR()
					time.sleep(1.5)
					autopilot.stop()
					time.sleep(1)
					search = 1
					navigating = 0
					ser.flush()
	
				# No direction to fly
				if(sensor1 == 1 and sensor2 == 1 and sensor3 == 1 and sensor4 == 1):
					#print("No direction to fly")
					autopilot.land()
					time.sleep(5)
					flying = 0
					print('Can\'t fly')
	
				# Emergency kill command
				if(buf == "kill"):
					autopilot.throttleCut()
					#time.sleep(10)
					#autopilot.landed()
					flying = 0
					#print('Killing operation')
	
				if(isKill):
					#autopilot.throttleCut()
					autopilot.stop()
					autopilot.land()
					time.sleep(10)
					flying = 0
					return
					#print('Killed manually')
	
			seen = 0
	
			#while(search == 1 and buf != 'stop'):
				# Capture image and look for ball
	except KeyboardInterrupt:
	#	clientsocket.shutdown()
		clientsocket.close()
	
	except:
		print('Error occured, closing socket')
	#	clientsocket.shutdown()
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

