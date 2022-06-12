import serial
import time

# arduino_blink.py

for i in range(10):
    with serial.Serial('COM4', 9800, timeout=1) as ser:
        time.sleep(1)
        ser.write(b'H')   # send the pyte string 'H'
        time.sleep(1)   # wait 0.5 seconds
        ser.write(b'L')   # send the byte string 'L'
