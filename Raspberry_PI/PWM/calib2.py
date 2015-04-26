import time
import autopilot
from RPIO import PWM

PWM.init_channel(1, 18005)
autopilot.maxAll()
time.sleep(15)
autopilot.minAll()
time.sleep(15)
PWM.cleanup()
