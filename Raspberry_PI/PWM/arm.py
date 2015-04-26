import time
import autopilot
from RPIO import PWM

autopilot.balance()
time.sleep(5)
autopilot.arm()
