from machine import Pin, PWM
from machine import Pin, ADC
from time import sleep
# from Sensor_class import Sensor
from Line_Sensor_class import Line_Sensor

button = Pin(0, Pin.IN, Pin.PULL_DOWN)
forward_left = PWM(Pin(20))
forward_right = PWM(Pin(6))
reverse_left = PWM(Pin(19))
reverse_right = PWM(Pin(7))
# sensor = Sensor(Pin(14, Pin.OUT), Pin(15, Pin.IN))
lineSensor = Line_Sensor(ADC(28), ADC(27), ADC(26))
fullspeed = 65535
oSpeedl = .18
oSpeedr = .14
speedl = oSpeedl
speedr = oSpeedr
driving = False

forward_left.freq(100)
forward_right.freq(100)
reverse_left.freq(20)
reverse_right.freq(20)

while True:
    left, center, right = lineSensor.get_Line()
    if button.value() == 1 and driving == False:
        driving = True
        forward_left.duty_u16(int(fullspeed * speedl))
        forward_right.duty_u16(int(fullspeed * speedr))
    
    if center < 30000 and driving:
        if left > 40000:
            forward_right.freq(20)
            print("go left")
            speedr = .08
            speedl = .1
            forward_left.duty_u16(0)
            forward_right.duty_u16(0)
            reverse_left.duty_u16(int(fullspeed * speedl))
            forward_right.duty_u16(int(fullspeed * speedr))
        elif right > 40000:
            forward_left.freq(20)
            print("go right")
            speedr = .08
            speedl = .1
            forward_left.duty_u16(0)
            forward_right.duty_u16(0)
            forward_left.duty_u16(int(fullspeed * speedl))
            reverse_right.duty_u16(int(fullspeed * speedr))
    elif driving:
        if left < 43000 and right < 43000:
            forward_left.freq(100)
            forward_right.freq(100)
            print("straight")
            speedl = oSpeedl
            speedr = oSpeedr
            reverse_left.duty_u16(0)
            reverse_right.duty_u16(0)
            forward_left.duty_u16(int(fullspeed * speedl))
            forward_right.duty_u16(int(fullspeed * speedr))
    sleep(0.01)
            