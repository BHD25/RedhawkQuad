import time
import autopilot
import RPi.GPIO as GPIO
from RPIO import PWM

GPIO.setmode(GPIO.BCM)

# 1 roll
# 2 pitch
# 3 throttle
# 4 yaw
# 5 mode

# 6 dummy1
# 7 dummy2
# 8 dummy3

autopilot.initialize()
autopilot.takeOff()

navigating = 1
movDirection = 2
search = 0

while(navigating == 1):
	if(sensor1 == 0 && sensor2 == 1 && movDirection == 2):
		autopilot.stop()
		autopilot.forward()
		movDirection = 1

	#else if(sensor1 == 0 && sensor2 == 1 && movDirection == 1):


	if(sensor1 == 0 && sensor2 == 0 && movDirection == 4):
		autopilot.stop()
		time.sleep(.3)
		autopilot.forward()
		time.sleep(.5)
		autopilot.stop()
		movDirection = 2
		autopilot.strafeR()
		time.sleep(1)
		autopilot.stop()

	if(sensor1 == 1 && sensor4 == 0 && sensor2 == 1 && movDirection == 1):
		autopilot.stop()
		time.sleep(.3)
		autopilot.strafeL()
		movDirection = 4

	if(sensor3 == 1 && sensor2 == 0 && movDirection == 2):
		autopilot.strafeR()
		movDirection = 2

	if(sensor1 == 1 && sensor2 == 1):
		autopilot.strafeL()

	if(sensor1 == 1 && sensor2 == 1 && sensor3 == 1 && sensor4 == 1):
		autopilot.land()
		time.sleep(5)
		flying = 0

	if(sensor1 == 1 && sensor4 == 1):
		navigating = 0
		autopilot.stop()
		autopilot.turnR()
		time.sleep(.5)
		autopilot.stop()
		search = 1

	if(pipe == "kill"):
		autopilot.land()
		time.sleep(5)
		flying = 0

seen = 0

while(search == 1):
	# Capture image and look for ball
	if(seen = 1):
		

#time.sleep(5)
#autopilot.land()
#time.sleep(10)
PWM.cleanup()

