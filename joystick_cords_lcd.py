import PCF8591 as ADC
import time
import RPi.GPIO as GPIO

A = 12
B = 16
C = 6
D = 13
E = 19
F = 20
G = 21
H = 26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(H, GPIO.OUT)

def off():
    GPIO.output(A, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    GPIO.output(E, GPIO.LOW)
    GPIO.output(F, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(H, GPIO.LOW)
    
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
    GPIO.output(H, GPIO.HIGH)

def wait(s):
    time.sleep(s)

def setup():
    ADC.setup(0x48)					# Setup PCF8591
    global state

def direction():	#get joystick result
    state = ['home', 'up', 'down', 'left', 'right']
    i = 0
    if ADC.read(0) <= 30:
        i = 1		#up
    if ADC.read(0) >= 225:
        i = 2		#down

    if ADC.read(1) <= 30:
        i = 3		#left
    if ADC.read(1) >= 225:
        i = 4		#right

    if ADC.read(0) - 125 < 15 and ADC.read(0) - 125 > -15	and ADC.read(1) - 125 < 15 and ADC.read(1) - 125 > -15:
        i = 0
    
    return state[i]

def loop():
    loops = 0
    while True:
        if direction() != None:
            j = 0
            if ADC.read(0) <= 30:
                j = 1		#up
            if ADC.read(0) >= 225:
                j = 2		#down
            if ADC.read(1) <= 30:
                j = 3		#left
            if ADC.read(1) >= 225:
                j = 4		#right
            if ADC.read(0) - 125 < 15 and ADC.read(0) - 125 > -15	and ADC.read(1) - 125 < 15 and ADC.read(1) - 125 > -15:
                j = 0
            print("X:", ADC.read(0))
            print("Y:", ADC.read(1))
            wait(0.05)
            off()
            if j != 0:
                loops = 0
            if j == 0:
                zero()
            if j == 1:
                one()
            if j == 2:
                two()
            if j == 3:
                three()
            if j == 4:
                four()
            if loops > 50:
                print("Idle timeout")
            while loops > 50:
                off()
                if direction() != 'home':
                    print("Resume")
                    break
            loops += 1
            
def destroy():
    off()
    pass

if __name__ == '__main__':		# Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()