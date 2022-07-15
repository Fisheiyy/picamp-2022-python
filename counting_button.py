import RPi.GPIO as GPIO
import time

A = 12
B = 16
C = 6
D = 13
E = 19
F = 20
G = 21
Btn = 25

def wait(s):
    time.sleep(s)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(Btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def off():
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.LOW)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    
def one():
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    
def two():
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    
def three():
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    
def four():
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    
def five():
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    
def six():
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    
def seven():
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    
def eight():
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    
def nine():
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    
def zero():
    GPIO.output(A, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)
    GPIO.output(C, GPIO.HIGH)
    GPIO.output(D, GPIO.HIGH)
    GPIO.output(E, GPIO.HIGH)
    GPIO.output(F, GPIO.HIGH)
    
amt = 0

while True:
    if amt == 10:
        amt = 0
    if GPIO.input(Btn) == GPIO.HIGH:
        print(amt)
        if amt == 0:
            off()
            zero()
            wait(0.2)
        if amt == 1:
            off()
            one()
            wait(0.2)
        if amt == 2:
            off()
            two()
            wait(0.2)
        if amt == 3:
            off()
            three()
            wait(0.2)
        if amt == 4:
            off()
            four()
            wait(0.2)
        if amt == 5:
            off()
            five()
            wait(0.2)
        if amt == 6:
            off()
            six()
            wait(0.2)
        if amt == 7:
            off()
            seven()
            wait(0.2)
        if amt == 8:
            off()
            eight()
            wait(0.2)
        if amt == 9:
            off()
            nine()
            wait(0.2)
        amt += 1