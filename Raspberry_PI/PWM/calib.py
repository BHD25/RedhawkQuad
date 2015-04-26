import time
import autopilot
from RPIO import PWM

PWM.init_channel(1, 18005)
autopilot.minAll()
time.sleep(5)
autopilot.maxAll()
time.sleep(30)
PWM.cleanup()
