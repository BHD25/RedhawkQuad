import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

while 1:
	GPIO.setup("P8_13", GPIO.OUT)
	GPIO.output("P8_13", GPIO.HIGH)
	GPIO.cleanup()
	PWM.start("P8_13", 50)
	PWM.stop("P8_13")
	PWM.cleanup()
