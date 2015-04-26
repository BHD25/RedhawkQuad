import serial

port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
port.open()

port.write("testing")
count = 0

try:
	while count < 30:
		#port.write('1')
		rcv = port.readline()
		print(repr(rcv))
		#port.write("\r\nYou sent:" + repr(rcv))
		count = count + 1
		if count == 15:
			port.write('0')
			port.flush()

except KeyboardInterrupt:
	port.close()
