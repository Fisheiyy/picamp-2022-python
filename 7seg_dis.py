import RPi.GPIO as GPIO
import time
import random

A = 12
B = 16
C = 6
D = 13
E = 19
F = 20
G = 21
PERIOD = 26

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
GPIO.setup(PERIOD, GPIO.OUT)

def off():
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.LOW)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(PERIOD, GPIO.LOW)
    
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
    
def period():
    GPIO.output(PERIOD, GPIO.HIGH)

while True:
    num = random.randrange(0 ,11)
    print(num)
    if num == 1:
        one()
        wait(1)
        off()
    if num == 2:
        two()
        wait(1)
        off()
    if num == 3:
        three()
        wait(1)
        off()
    if num == 4:
        four()
        wait(1)
        off()
    if num == 5:
        five()
        wait(1)
        off()
    if num == 6:
        six()
        wait(1)
        off()
    if num == 7:
        seven()
        wait(1)
        off()
    if num == 8:
        eight()
        wait(1)
        off()
    if num == 9:
        nine()
        wait(1)
        off()
    if num == 0:
        zero()
        wait(1)
        off()
    if num == 10:
        period()
        wait(1)
        off()