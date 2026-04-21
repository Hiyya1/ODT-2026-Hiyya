#This code operates 12 flowers, provided that all the servos and sensors are working correctly. For my final project, only the first 6 were used.

# import libraries
from machine import I2C, Pin, time_pulse_us
from hcsr04 import HCSR04
from servo import Servo
import time

# initialise PCA9685 and servo pins
# PCA9685 class to control servo motor via I2C
class PCA9685:
    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.reset()
        self.set_pwm_freq(50)  # 50Hz for servos

    def reset(self):
        self.i2c.writeto_mem(self.address, 0x00, bytes([0x00]))

    def set_pwm_freq(self, freq_hz):
        prescale_val = int(25000000.0 / (4096 * freq_hz) - 1)
        old_mode = self.i2c.readfrom_mem(self.address, 0x00, 1)[0]
        new_mode = (old_mode & 0x7F) | 0x10
        self.i2c.writeto_mem(self.address, 0x00, bytes([new_mode]))
        self.i2c.writeto_mem(self.address, 0xFE, bytes([prescale_val]))
        self.i2c.writeto_mem(self.address, 0x00, bytes([old_mode]))
        time.sleep_ms(5)
        self.i2c.writeto_mem(self.address, 0x00, bytes([old_mode | 0xa1]))

    def set_pwm(self, channel, on, off):
        reg = 0x06 + 4 * channel
        data = bytearray([
            on & 0xFF,
            on >> 8,
            off & 0xFF,
            off >> 8
        ])
        self.i2c.writeto_mem(self.address, reg, data)

    def set_servo_angle(self, channel, angle):
        angle = max(0, min(180, angle))  # Clamp angle
        pulse_min = 102  # 0 degrees
        pulse_max = 512  # 180 degrees
        pulse = int(pulse_min + (pulse_max - pulse_min) * angle / 180)
        self.set_pwm(channel, 0, pulse)

# Setup I2C and PCA9685
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
pca = PCA9685(i2c)

# assign ESP32 pins to ultrasonic sensors
sensor1 = HCSR04(trigger_pin=15, echo_pin=2)
sensor2 = HCSR04(trigger_pin=15, echo_pin=4)
sensor3 = HCSR04(trigger_pin=15, echo_pin=18)
sensor4 = HCSR04(trigger_pin=15, echo_pin=19)
sensor5 = HCSR04(trigger_pin=15, echo_pin=25)
sensor6 = HCSR04(trigger_pin=15, echo_pin=33)
sensor7 = HCSR04(trigger_pin=15, echo_pin=23)
sensor8 = HCSR04(trigger_pin=15, echo_pin=13)
sensor9 = HCSR04(trigger_pin=15, echo_pin=12)
sensor10 = HCSR04(trigger_pin=15, echo_pin=14)
sensor11 = HCSR04(trigger_pin=15, echo_pin=27)
sensor12 = HCSR04(trigger_pin=15, echo_pin=26)


# start loop
while (1):
# trigger all sensors
# get distance of object above sensors
    distance1 = sensor1.distance_cm()
    distance2 = sensor2.distance_cm()
    distance3 = sensor3.distance_cm()
    distance4 = sensor4.distance_cm()
    distance5 = sensor5.distance_cm()
    distance6 = sensor6.distance_cm()
    distance7 = sensor7.distance_cm()
    distance8 = sensor8.distance_cm()
    distance9 = sensor9.distance_cm()
    distance10 = sensor10.distance_cm()
    distance11 = sensor11.distance_cm()
    distance12 = sensor12.distance_cm()

# if object detected by a sensor X at a distance of 10-50cm,
# rotate corresponding servo X slowly by 90 degrees
# wait for 1 second
# rotate in reverse by 90 degrees
# go back to sensor loop

    if distance1 > 2 and distance1 < 30:
        print ("Sensor 1 detects object")
        for i in range (0,90):
            pca.set_servo_angle(0, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(0, (90-i))
            time.sleep(0.01)

    if distance2 > 2 and distance2 < 30:
        print ("Sensor 2 detects object")
        for i in range (0,90):
            pca.set_servo_angle(1, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(1, (90-i))
            time.sleep(0.01)
            
    if distance3 > 2 and distance3 < 30:
        print ("Sensor 3 detects object")
        for i in range (0,90):
            pca.set_servo_angle(2, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(2, (90-i))
            time.sleep(0.01)
            
    if distance4 > 2 and distance4 < 30:
        print ("Sensor 4 detects object")
        for i in range (0,90):
            pca.set_servo_angle(3, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(3, (90-i))
            time.sleep(0.01)
            
    if distance5 > 2 and distance5 < 30:
        print ("Sensor 5 detects object")
        for i in range (0,90):
            pca.set_servo_angle(4, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(4, (90-i))
            time.sleep(0.01)
            
    if distance6 > 2 and distance6 < 30:
        print ("Sensor 6 detects object")
        for i in range (0,90):
            pca.set_servo_angle(5, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(5, (90-i))
            time.sleep(0.01)
            
    if distance7 > 2 and distance7 < 30:
        print ("Sensor 7 detects object")
        for i in range (0,90):
            pca.set_servo_angle(6, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(6, (90-i))
            time.sleep(0.01)
            
    if distance8 > 2 and distance8 < 30:
        print ("Sensor 8 detects object")
        for i in range (0,90):
            pca.set_servo_angle(7, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(7, (90-i))
            time.sleep(0.01)
            
    if distance9 > 2 and distance9 < 30:
        print ("Sensor 9 detects object")
        for i in range (0,90):
            pca.set_servo_angle(8, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(8, (90-i))
            time.sleep(0.01)
            
    if distance10 > 2 and distance10 < 30:
        print ("Sensor 10 detects object")
        for i in range (0,90):
            pca.set_servo_angle(9, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(9, (90-i))
            time.sleep(0.01)
            
    if distance11 > 2 and distance11 < 30:
        print ("Sensor 11 detects object")
        for i in range (0,90):
            pca.set_servo_angle(10, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(10, (90-i))
            time.sleep(0.01)
            
    if distance12 > 2 and distance12 < 30:
        print ("Sensor 12 detects object")
        for i in range (0,90):
            pca.set_servo_angle(12, i)
            time.sleep(0.01)
        time.sleep(1)
        for i in range (0,90):
            pca.set_servo_angle(12, (90-i))
            time.sleep(0.01)