import RPi.GPIO as GPIO
import time
from AlphaBot2 import AlphaBot2

A = 8
SPEED = 50

#RUN = DISTANCE/SPEED
RUN = .8
TURN = 0.27
TURNSPD = 28
SLOW = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(A,GPIO.IN,GPIO.PUD_UP)

Ab = AlphaBot2()

# find speed of robot, set each movement to a certain time to be 0.5 meters
# start when A is pressed, find hardware
Ab.setPWMA(SPEED)
Ab.setPWMB(SPEED)

go = True

try:
    while go == True:
        if GPIO.input(A) == 0:
            
            time.sleep(0.8) # just so it doesnt take off while still pressing button
            ### LINE ONE FORWARD ###
 
            #start, go forward
            Ab.setMotor(SPEED,SPEED)
            time.sleep(RUN)
            
            # before stopping, cut the speed to stop better
            Ab.setMotor(SPEED/2, SPEED/2)
            time.sleep(SLOW) # maybe keep???
 
            Ab.stop()
            time.sleep(TURN) # just used TURN speed bc convenient/ arbitary
                 
            #TURN LEFT
            Ab.setMotor(0, TURNSPD)
            time.sleep(TURN)
            Ab.stop()
            time.sleep(TURN)
 
            
            ### LINE TWO START ###
 
            #start, go forward
            Ab.setMotor(SPEED,SPEED)
            time.sleep(RUN)
            
            # before stopping, cut the speed to stop better
            Ab.setMotor(SPEED/2, SPEED/2)
            time.sleep(SLOW) # maybe keep???
 
            Ab.stop()
            time.sleep(TURN) # just used TURN speed bc convenient/ arbitary
                 
            #TURN LEFT
            Ab.setMotor(0, TURNSPD)
            time.sleep(TURN)
            Ab.stop()
            time.sleep(TURN)
 
            
            ### LINE THREE START ###
 
            #start, go forward
            Ab.setMotor(SPEED,SPEED)
            time.sleep(RUN)
            
            # before stopping, cut the speed to stop better
            Ab.setMotor(SPEED/2, SPEED/2)
            time.sleep(SLOW) # maybe keep???
 
            Ab.stop()
            time.sleep(TURN) # just used TURN speed bc convenient/ arbitary
                 
            #TURN LEFT
            Ab.setMotor(0, TURNSPD)
            time.sleep(TURN)
            Ab.stop()
            time.sleep(TURN)
 
            ### LINE FOUR START ###
 
            #start, go forward
            Ab.setMotor(SPEED,SPEED)
            time.sleep(RUN)
            
            # before stopping, cut the speed to stop better
            Ab.setMotor(SPEED/2, SPEED/2)
            time.sleep(SLOW) # maybe keep???
 
            Ab.stop()
            time.sleep(TURN) # just used TURN speed bc convenient/ arbitary
                 
            #TURN LEFT
            Ab.setMotor(0, TURNSPD)
            time.sleep(TURN)
            Ab.stop()
            time.sleep(TURN)
            
            go = False

except KeyboardInterrupt:
    GPIO.cleanup()
    
