import Adafruit_BBIO.UART as UART
import serial
  
UART.setup("UART1")

ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
 
while 1:
	print ser.readline()
	print ser.readline()
	print ser.readline()
	ser.write(b'Got it')
