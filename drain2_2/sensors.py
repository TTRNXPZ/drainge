import RPi.GPIO as GPIO
import serial
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    ser = serial.Serial("/dev/serial0", baudrate=115200, timeout=1)
except serial.SerialException:
    print("ERROR: UART device not found (/dev/serial0)")
    ser = None

COM = 0x55

def measure_hcsr04():
    GPIO.output(TRIG, False)
    time.sleep(0.002)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start, pulse_end = 0, 0
    timeout = time.time() + 1
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if pulse_start > timeout:
            return None

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if pulse_end > timeout:
            return None

    pulse_duration = pulse_end - pulse_start
    distance_cm = (pulse_duration * 34300) / 2
    return round(distance_cm, 2)

def read_uart_sensor():
    if not ser:
        return None

    ser.write(bytes([COM]))
    time.sleep(0.1)

    if ser.in_waiting >= 4:
        first_byte = ser.read()
        if first_byte == b'\xFF':
            data = ser.read(3)
            buffer = [0xFF] + list(data)
            CS = buffer[0] + buffer[1] + buffer[2]
            if buffer[3] == (CS & 0xFF):
                distance_mm = (buffer[1] << 8) + buffer[2]
                return distance_mm
    return None

def cleanup():
    GPIO.cleanup()
    if ser:
        ser.close()
