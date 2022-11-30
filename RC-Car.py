import RPi.GPIO as GPIO
import time
import keyboard
from pyPS4Controller.controller import Controller
 
 
in1 = 5
in2 = 6
in3 = 13
in4 = 19
en1 = 23
en2 = 24
servo1 = 4
 
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.setup(servo1,GPIO.OUT)
 
p1 = GPIO.PWM(en1, 50)
p2 = GPIO.PWM(en2, 50)
serv = GPIO.PWM(servo1, 50)
serv.start(2.5)
maxpower = 90
zerosteer = (2+(90/18)) # 90 Grad Ausgangsposition
 
class MyController(Controller):
 
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
 
    def on_L3_down(self,value):
        speed = (value/32767) * maxpower  
	  backwards(speed)
  
     def on_L3_up(self,value):
        speed = (abs(value)/32767) * maxpower  
	  forward(speed)
     
def on_L3_at_rest(self):
		p1.start(0)
		p1.start(0)
		serv.ChangeDutyCycle(zerosteer)
 
	def on_L3_right(self,value):
	    Angle = ((1-(value/32767))*90)
          steer(2+(Angle/18))
	    
 #32767
 
def on_L3_left: #-32767
 	    Angle = (((abs(x)/32767)*90)+90)
		steer(2+(Angle/18))
 
#-32767, mitte 0
 
def forward(speed):
    print("Vorwartsmodus aktiviert")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    p1.start(speed)
    p2.start(speed)
 
    
#32767
 
def backwards(speed):
    print("Ruckwertsmodus aktiviert")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.HIGH)
    p1.start(speed)
    p2.start(speed)
 
def steer(Cycle):
    serv.ChangeDutyCycle(Cycle)
