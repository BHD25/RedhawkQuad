import time
from RPIO import PWM

# These set the PWM signal
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

# Sets the pins on the Pi that each is associated with
ROLL = 22
PITCH = 27
THROTTLE = 4
YAW = 17
MODE = 18
DUMMY1 = 23
DUMMY2 = 24
DUMMY3 = 25

# Initialize PWM
SERVO = PWM.Servo()

throttle=THRMIN

# Arm method
def arm():
	SERVO.set_servo(THROTTLE, THRMIN);
	SERVO.set_servo(YAW, YAWMAX);
	SERVO.set_servo(PITCH, PITMID);
	SERVO.set_servo(ROLL, ROLMID);
	SERVO.set_servo(MODE, MODESTAB);
	SERVO.set_servo(DUMMY1, MODESTAB);
	SERVO.set_servo(DUMMY2, MODESTAB);
	SERVO.set_servo(DUMMY3, MODESTAB);
	time.sleep(10);
	SERVO.set_servo(YAW,YAWMID);

# Set all signals to minimum values
def minAll():
	SERVO.set_servo(THROTTLE, THRMIN)
	SERVO.set_servo(YAW, YAWMIN)
	SERVO.set_servo(PITCH, PITMIN)
	SERVO.set_servo(ROLL, ROLMIN)
	SERVO.set_servo(MODE, MODESTAB)
	SERVO.set_servo(DUMMY1, MODESTAB)
	SERVO.set_servo(DUMMY2, MODESTAB)
	SERVO.set_servo(DUMMY3, MODESTAB)

# Cut the throttle
def throttleCut():
	balance()
	SERVO.set_servo(THROTTLE, THRMIN)
	SERVO.set_servo(YAW, YAWMIN)
	
# Set all signals to max values
def maxAll():
	SERVO.set_servo(THROTTLE, THRMAX)
	SERVO.set_servo(YAW, YAWMAX)
	SERVO.set_servo(PITCH, PITMAX)
	SERVO.set_servo(ROLL, ROLMAX)
	SERVO.set_servo(MODE, MODELAND)
	SERVO.set_servo(DUMMY1, MODELAND)
	SERVO.set_servo(DUMMY2, MODELAND)
	SERVO.set_servo(DUMMY3, MODELAND)

# Set throttle signal to max value
def thrMax():
	SERVO.set_servo(THROTTLE, THRMAX)

# Takeoff method
def takeOff():
	balance()
	time.sleep(10)
	arm()
	time.sleep(3)
	thrMax()
	time.sleep(.3)
	balance()
	setAltitude()

# Stop all movement in any direction
def stop():
	SERVO.set_servo(THROTTLE, THRMID)
	SERVO.set_servo(YAW, YAWMID)
	SERVO.set_servo(PITCH, PITMID)
	SERVO.set_servo(ROLL, ROLMID)

# Fly forward
def forward():
	SERVO.set_servo(PITCH, PIT60)

# Fly backward
def backward():
	SERVO.set_servo(PITCH, PIT40)

# Fly left
def strafeL():
	SERVO.set_servo(ROLL, ROL40)

# Fly right		
def strafeR():
	SERVO.set_servo(ROLL, ROL60)

# Turn left
def turnL():
	SERVO.set_servo(YAW, YAW40)

# Turn right
def turnR():
	SERVO.set_servo(YAW, YAW60)

# Set all signals to mid values
def balance():
	SERVO.set_servo(THROTTLE, THRMID)
	SERVO.set_servo(YAW, YAWMID)
	SERVO.set_servo(ROLL, ROLMID)
	SERVO.set_servo(PITCH, PITMID)
	SERVO.set_servo(MODE, (MODESTAB+MODELAND)/2)
	SERVO.set_servo(DUMMY1, (MODESTAB+MODELAND)/2)
	SERVO.set_servo(DUMMY2, (MODESTAB+MODELAND)/2)
	SERVO.set_servo(DUMMY3, (MODESTAB+MODELAND)/2)

# Initialize the PWM channel
def initialize():
	PWM.init_channel(1,SUBCYCL)

# Set mode signal to the land
def land():
	SERVO.set_servo(MODE, MODELAND)

# Set mode signal to stabilize and throttle to its minimum value
def landed():
	SERVO.set_servo(MODE, MODESTAB)
	SERVO.set_servo(THROTTLE, THRMIN)

# Set mode signal to static altitude
def setAltitude():
	SERVO.set_servo(MODE, MODEALT)
