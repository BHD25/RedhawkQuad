import time
from RPIO import PWM

THRMIN=980/2
THRMAX=2020/2
THRMID=(THRMAX+THRMIN)/2

YAWMIN=980/2
YAWMAX=2020/2
YAWMID=(YAWMAX+YAWMIN)/2

PITMIN=980/2
PITMAX=2020/2
PITMID=(PITMAX+PITMIN)/2

ROLMIN=980/2
ROLMAX=2020/2
ROLMID=(ROLMAX+ROLMIN)/2

FREQ=55.54
SUBCYCL=18005

MODEALT = 1420/2
MODESTAB = 1280/2
MODELAND = 1560/2

ROLL = 22
PITCH = 27
THROTTLE = 4
YAW = 17
MODE = 18
DUMMY1 = 23
DUMMY2 = 24
DUMMY3 = 25

SERVO = PWM.Servo()

throttle=THRMIN
#yaw=(YAWMAX+YAWMIN)/2
#pitch=(PITMAX+PITMIN)/2
#roll=(ROLMAX+ROLMIN)/2

def arm():
#	global throttle
#	global yaw
#	global pitch
#	global roll
#	PWM.init_channel(1, SUBCYCL)
	SERVO.set_servo(THROTTLE, THRMIN);
	SERVO.set_servo(YAW, YAWMAX);
	SERVO.set_servo(PITCH, PITMID);
	SERVO.set_servo(ROLL, ROLMID);
	SERVO.set_servo(MODE, MODESTAB);
#	SERVO.set_servo(DUMMY1, 1420/2);
	SERVO.set_servo(DUMMY1, MODESTAB);
	SERVO.set_servo(DUMMY2, MODESTAB);
	SERVO.set_servo(DUMMY3, MODESTAB);
	time.sleep(10);
	SERVO.set_servo(YAW,YAWMID);

def minAll():
#	global throttle
#	global yaw
#	global pitch
#	global roll
	SERVO.set_servo(THROTTLE, THRMIN)
	SERVO.set_servo(YAW, YAWMIN)
	SERVO.set_servo(PITCH, PITMIN)
	SERVO.set_servo(ROLL, ROLMIN)
	SERVO.set_servo(MODE, MODESTAB)
	SERVO.set_servo(DUMMY1, MODESTAB)
	SERVO.set_servo(DUMMY2, MODESTAB)
	SERVO.set_servo(DUMMY3, MODESTAB)

def maxAll():
#	global throttle
#	global yaw
#	global pitch
#	global roll
	SERVO.set_servo(THROTTLE, THRMAX)
	SERVO.set_servo(YAW, YAWMAX)
	SERVO.set_servo(PITCH, PITMAX)
	SERVO.set_servo(ROLL, ROLMAX)
	SERVO.set_servo(MODE, MODELAND)
	SERVO.set_servo(DUMMY1, MODELAND)
	SERVO.set_servo(DUMMY2, MODELAND)
	SERVO.set_servo(DUMMY3, MODELAND)

def thrMax():
#	global throttle
#	PWM.start(THROTTLE, THRMAX, FREQ, 0)
	SERVO.set_servo(THROTTLE, THRMAX)

def thrMin():
#	global throttle
	PWM.start(THROTTLE, THRMIN, FREQ, 0)

def stopAll():
#	global throttle
#	global yaw
#	global pitch
#	global roll
	PWM.stop(THROTTLE)
	PWM.stop(YAW)
	PWM.stop(PITCH)
	PWM.stop(ROLL)

def takeOff():
	balance()
	time.sleep(10)
	arm()
	#time.sleep(6)
	#autopilot.arm()
	time.sleep(3)
	thrMax()
	time.sleep(.3)
	balance()
	setAltitude()
#	global throttle
#	global yaw
#	global pitch
#	global roll
#	while throttle<9:
#		throttle+=.1
#		PWM.set_duty_cycle(THROTTLE, throttle)
#		time.sleep(1)

def stop():
	PWM.set_servo(THROTTLE, THRMID)
	PWM.set_servo(YAW, YAWMID)
	PWM.set_servo(PITCH, PITMID)
	PWM.set_servo(ROLL, ROLMID)

def forward():
	PWM.set_servo(PITCH, (PITMAX*.75))

def backward():
	PWM.set_servo(PITCH, (PITMAX*.25))

def strafeL():
	PWM.set_servo(ROLL, (ROLMAX*.25))

#	pitch=(PITMIN+PITMAX)/2-1
#	PWM.set_duty_cycle(PITCH, pitch) 
#	while pitch!=(PITMIN+PITMAX)/2:
#		pitch+=.1
#		PWM.set_duty_cycle(PITCH, pitch) 
		
def strafeR():
	PWM.set_servo(ROLL, (ROLMAX*.75))

#	pitch=(PITMIN+PITMAX)/2+1
#	PWM.set_duty_cycle(PITCH, pitch) 
#	while pitch!=(PITMIN+PITMAX)/2:
#		pitch-=.1
#		PWM.set_duty_cycle(PITCH, pitch) 

def turnL():
	PWM.set_servo(YAW, (YAWMAX*.25))

def turnR():
	PWM.set_servo(YAW, (YAWMAX*.75))

def balance():
#	PWM.init_channel(1, SUBCYCL)
	SERVO.set_servo(THROTTLE, THRMID)
	SERVO.set_servo(YAW, YAWMID)
	SERVO.set_servo(ROLL, ROLMID)
	SERVO.set_servo(PITCH, PITMID)
	SERVO.set_servo(MODE, (MODESTAB+MODELAND)/2)
	SERVO.set_servo(DUMMY1, (MODESTAB+MODELAND)/2)
	SERVO.set_servo(DUMMY2, (MODESTAB+MODELAND)/2)
	SERVO.set_servo(DUMMY3, (MODESTAB+MODELAND)/2)

def initialize():
	PWM.init_channel(1,SUBCYCL)
	
def land():
	SERVO.set_servo(MODE, MODELAND)
#	global throttle
#	global yaw
#	global pitch
#	global roll
#	while throttle<THRMIN:
#		throttle-=.05
#		PWM.set_duty_cycle(THROTTLE, throttle)
#		time.sleep(1)

def setAltitude():
	SERVO.set_servo(MODE, MODEALT)
