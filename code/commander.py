# Licensed under MIT licence, see LICENSE for details.
# Copyright Jed Muff, Eric Hannus, Antti Sippola, Julius Mikala, Jere Vespä. 2023

# - The keypresses do not require Ctrl+C to be pressed to exit a loop  (keyboard module needed!)
#  >> The keyboard module is needed for this! Install in Windows with "pip install keyboard"
# - A separate move_set.py file is used to store moves that are called by pressing keys 1-9

import zmq #library for communication with the robot
import time #for timing
import keyboard #for reading keypresses
from move_set import * #import additional moves from a separate file called move_set.py

stepTime = 0.2 #for delays in walking function

#Movement functions
def walk(front_LU, front_LL, front_RU, front_RL, back_LU, back_LL, back_RU, back_RL):
    # The walk() function takes the indexes of the upper (close to the body) and lower (further from the body)
    # servos for the left and right leg (left and right when looking in the desired movement direction), for both 
    #the front and back legs in relation to the direction of movement.

    #_LU = left upper joint
    #_LL = left lower joint
    #_RU = right upper joint
    #_RL = right lower joint

    #The second part of the send_multipart list must be a byte string containing servo indexes (s is included before the numerical index!)
    # and corresponding setpoint values. Spaces are sepearating servo values, and the string must end with a linebreak. To convert a
    # concentrated string to a byte string, the .encode() function is used.

    #TODO: remove old lines if new ones work correctly. They are now ordered in front left > front right > back left > back right order for all commands. Also the descriptions of each movement (also in CW and CCE rotations can be exxtended/improved).
    #sock.send_multipart([b"cmd", ("s"+str(front_RL)+" 300 s"+str(back_RL)+" 300 s"+str(back_LL)+" 300 s"+str(front_LL)+" 300\n").encode('UTF-8')])
    sock.send_multipart([b"cmd", ("s"+str(front_LL)+" 300 s"+str(front_RL)+" 300 s"+str(back_LL)+" 300 s"+str(back_RL)+" 300\n").encode('UTF-8')]) #set all lower joints to 300 = wider than default
    time.sleep(stepTime)
    
    #sock.send_multipart([b"cmd", ("s"+str(front_RL)+" 375 s"+str(back_RL)+" 300 s"+str(back_LL)+" 375 s"+str(front_LL)+" 300\n").encode('UTF-8')])
    sock.send_multipart([b"cmd", ("s"+str(front_LL)+" 300 s"+str(front_RL)+" 375 s"+str(back_LL)+" 375 s"+str(back_RL)+" 300\n").encode('UTF-8')]) #lift front right and back left legs 
    #^^ here we can send to only 2 joints?
    time.sleep(stepTime)

    #sock.send_multipart([b"cmd", ("s"+str(front_RU)+" 512 s"+str(back_RU)+" 312 s"+str(back_LU)+" 512 s"+str(front_LU)+" 712\n").encode('UTF-8')]) ### Move Left
    sock.send_multipart([b"cmd", ("s"+str(front_LU)+" 712 s"+str(front_RU)+" 512 s"+str(back_LU)+" 512 s"+str(back_RU)+" 312\n").encode('UTF-8')]) #move front left and back right legs
    time.sleep(stepTime)

    #sock.send_multipart([b"cmd", ("s"+str(front_RL)+" 300 s"+str(back_RL)+" 300 s"+str(back_LL)+" 300 s"+str(front_LL)+" 300\n").encode('UTF-8')])
    sock.send_multipart([b"cmd", ("s"+str(front_LL)+" 300 s"+str(front_RL)+" 300 s"+str(back_LL)+" 300 s"+str(back_RL)+" 300\n").encode('UTF-8')]) #reset front right and back left legs that were offset previously, now all legs wide again
    #^^here we can send to only 2 joints again?
    time.sleep(stepTime)
    
    #sock.send_multipart([b"cmd", ("s"+str(front_RL)+" 300 s"+str(back_RL)+" 375 s"+str(back_LL)+" 300 s"+str(front_LL)+" 375\n").encode('UTF-8')])
    sock.send_multipart([b"cmd", ("s"+str(front_LL)+" 375 s"+str(front_RL)+" 300 s"+str(back_LL)+" 300 s"+str(back_RL)+" 375\n").encode('UTF-8')]) #lift front left and back right legs
    time.sleep(stepTime)

    #sock.send_multipart([b"cmd", ("s"+str(front_RU)+" 312 s"+str(back_RU)+" 512 s"+ str(back_LU)+" 712 s"+str(front_LU)+" 512\n").encode('UTF-8')]) ### Move Right
    sock.send_multipart([b"cmd", ("s"+str(front_LU)+" 512 s"+str(front_RU)+" 312 s"+ str(back_LU)+" 712 s"+str(back_RU)+" 512\n").encode('UTF-8')]) #move front right and back left legs that were offset previously
    time.sleep(stepTime)


def forward():
    walk(7, 8, 1, 2, 5, 6, 3, 4)

def backward():
    walk(3, 4, 5, 6, 1, 2, 7, 8)

def left():
    walk(5, 6, 7, 8, 3, 4, 1, 2)

def right():
    walk(1, 2, 3, 4, 7, 8, 5, 6)


def rotateCCW():
    sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) #initially set all outer joints to a wider stance than the default angle of 205
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s2 375 s4 300 s6 375 s8 300\n"]) #lift the lower joints of two diagonal legs
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s1 512 s3 312 s5 512 s7 312\n"]) #shift two legs by rotating the upper joints
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) #reset all lower joints
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s2 300 s4 375 s6 300 s8 375\n"]) #lift the lower joints of the other two legs that were not lifted in the previous step
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s1 312 s3 512 s5 312 s7 512\n"]) #shift two legs by rotating the upper joints
    time.sleep(stepTime)

def rotateCW():
    sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) #initially set all outer joints to a wider stance than the default angle of 205
    time.sleep(stepTime)
    
    sock.send_multipart([b"cmd", b"s2 375 s4 300 s6 375 s8 300\n"]) #lift the lower joints of two diagonal legs
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s1 512 s3 712 s5 512 s7 712\n"]) #shift two legs by rotating the upper joints
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) #reset all lower joints
    time.sleep(stepTime)
    
    sock.send_multipart([b"cmd", b"s2 300 s4 375 s6 300 s8 375\n"]) #lift the lower joints of the other two legs that were not lifted in the previous step
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s1 712 s3 512 s5 712 s7 512\n"]) #shift two legs by rotating the upper joints
    time.sleep(stepTime)

def reset():
    #send in two parts to prevent overload of too many commands at once
    sock.send_multipart([b"cmd", b"s1 512 s3 512 s5 512 s7 512 \n"])
    time.sleep(0.5)
    sock.send_multipart([b"cmd", b"s2 205 s4 205 s6 205 s8 205\n"])


if __name__ == '__main__':
    #zmq for communication with the RealAnt, setting up a socket 
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.connect("tcp://127.0.0.1:3002")

    #Attaching servos. This command is executed in the Arduino code running in the RealAnt.
    time.sleep(0.1)
    sock.send_multipart([b"cmd", b"attach_servos\n"])
    time.sleep(0.1)

    print("Move with WASD, roatate with QE, perform moves with 1-9, exit with Ctrl+C: \n")

    try:
        while(True):
            if keyboard.is_pressed("w"):
                forward()
            elif keyboard.is_pressed("s"):
                backward()
            elif keyboard.is_pressed("a"):
                left()
            elif keyboard.is_pressed("d"):
                right()
            elif keyboard.is_pressed("q"):
                rotateCCW()
            elif keyboard.is_pressed("e"):
                rotateCW()
            elif keyboard.is_pressed("1"):
                call_move(1, sock)
            elif keyboard.is_pressed("2"):
                call_move(2, sock)
            elif keyboard.is_pressed("3"):
                call_move(3, sock)
            elif keyboard.is_pressed("4"):
                call_move(4, sock)
            elif keyboard.is_pressed("5"):
                call_move(5, sock)
            elif keyboard.is_pressed("6"):
                call_move(6, sock)
            elif keyboard.is_pressed("7"):
                call_move(7, sock)
            elif keyboard.is_pressed("8"):
                call_move(8, sock)
            elif keyboard.is_pressed("9"):
                call_move(9, sock)
            else:
                reset()

    except KeyboardInterrupt:
        #Resetting all the servo positions via a command executed in the Arduino code running in the RealAnt.
        sock.send_multipart([b"cmd", b"reset\n"])
        time.sleep(0.7)
        #Detaching servos. This command is executed in the Arduino code running in the RealAnt.
        sock.send_multipart([b"cmd", b"detach_servos\n"])

        sock.close()
        ctx.term()