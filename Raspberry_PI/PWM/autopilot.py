import time
from RPIO import PWM

THRMIN=980/2
THRMAX=2020/2
THRMID=(THRMAX+THRMIN)/2

YAWMIN=980/2
YAWMAX=2020/2
YAWMID=(YAWMAX+YAWMIN)/2
YAW75=(YAWMAX+YAWMID)/2
YAW60=610
YAW40=400
YAW25=(YAWMID+YAWMIN)/2

PITMIN=980/2
PITMAX=2020/2
PITMID=(PITMAX+PITMIN)/2
PIT75=(PITMAX+PITMID)/2
PIT60=610
PIT40=400
PIT25=(PITMID+PITMIN)/2

ROLMIN=980/2
ROLMAX=2020/2
ROLMID=(ROLMAX+ROLMIN)/2
ROL75=(ROLMAX+ROLMID)/2
ROL60=610
ROL40=400
ROL25=(ROLMID+ROLMIN)/2

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

def throttleCut():
	balance()
	SERVO.set_servo(THROTTLE, THRMIN)
	SERVO.set_servo(YAW, YAWMIN)
	

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

#def thrMin():
#	global throttle
#	PWM.start(THROTTLE, THRMIN, FREQ, 0)

#def stopAll():
#	global throttle
#	global yaw
#	global pitch
#	global roll
#	PWM.stop(THROTTLE)
#	PWM.stop(YAW)
#	PWM.stop(PITCH)
#	PWM.stop(ROLL)

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
	SERVO.set_servo(THROTTLE, THRMID)
	SERVO.set_servo(YAW, YAWMID)
	SERVO.set_servo(PITCH, PITMID)
	SERVO.set_servo(ROLL, ROLMID)

def forward():
	SERVO.set_servo(PITCH, PIT60)

def backward():
	SERVO.set_servo(PITCH, PIT40)

def strafeL():
	SERVO.set_servo(ROLL, ROL40)

#	pitch=(PITMIN+PITMAX)/2-1
#	PWM.set_duty_cycle(PITCH, pitch) 
#	while pitch!=(PITMIN+PITMAX)/2:
#		pitch+=.1
#		PWM.set_duty_cycle(PITCH, pitch) 
		
def strafeR():
	SERVO.set_servo(ROLL, ROL60)

#	pitch=(PITMIN+PITMAX)/2+1
#	PWM.set_duty_cycle(PITCH, pitch) 
#	while pitch!=(PITMIN+PITMAX)/2:
#		pitch-=.1
#		PWM.set_duty_cycle(PITCH, pitch) 

def turnL():
	SERVO.set_servo(YAW, YAW40)

def turnR():
	SERVO.set_servo(YAW, YAW60)

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

def landed():
	SERVO.set_servo(MODE, MODESTAB)
	SERVO.set_servo(THROTTLE, THRMIN)

def setAltitude():
	SERVO.set_servo(MODE, MODEALT)
