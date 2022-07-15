import RPi.GPIO as GPIO
import time
import random

R = 17
G = 27
B = 22

def wait(s):
    time.sleep(s)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

def off():
    GPIO.output(R, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)

while True:
    num = random.randrange(0,7)
    print(num)
    if num == 0:
        print("R")
        GPIO.output(R, GPIO.HIGH)
        wait(0.5)
        off()
    if num == 1:
        print("G")
        GPIO.output(G, GPIO.HIGH)
        wait(0.5)
        off()
    if num == 2:
        print("B")
        GPIO.output(B, GPIO.HIGH)
        wait(0.5)
        off()
    if num == 3:
        print("RG")
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(G, GPIO.HIGH)
        wait(0.5)
        off()
    if num == 4:
        print("RB")
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(B, GPIO.HIGH)
        wait(0.5)
        off()
    if num == 5:
        print("BG")
        GPIO.output(B, GPIO.HIGH)
        GPIO.output(G, GPIO.HIGH)
        wait(0.5)
        off()
    if num == 6:
        print("RGB")
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(G, GPIO.HIGH)
        GPIO.output(B, GPIO.HIGH)
        wait(0.5)
        off()