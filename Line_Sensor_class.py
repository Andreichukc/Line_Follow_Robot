from machine import Pin, ADC
from time import sleep

class Line_Sensor:
    def __init__(self, left, center, right):
        self.left = left
        self.center = center
        self.right = right
    
    def get_Line(self):
        left_value = self.left.read_u16()
        center_value = self.center.read_u16()
        right_value = self.right.read_u16()
        print(f'left = {left_value:.2f}, center = {center_value:.2f}, right = {right_value:.2f}')
        return left_value, center_value, right_value
        
        
# sensorTest = Line_Sensor(ADC(28), ADC(27), ADC(26))
# 
# while True:
#     sensorTest.get_Line()
#     sleep(1)