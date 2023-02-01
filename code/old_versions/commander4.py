# Licensed under MIT licence, see LICENSE for details.
# Copyright Jed Muff, Eric Hannus, Antti Sippola, Julius Mikala, Jere Vespä. 2023


#IN THIS VERSION (commander4.py)
# - The keypresses do not require Ctrl+C to be pressed to exit a loop  (keyboard module needed!)
#  >> The keyboard module is needed for this! Install in Windows with "pip install keyboard"

import zmq
import time
import random #for random_test()
import keyboard #for reading keypresses

from move_set import * #import additional moves from a separate file called move_set.py

#Set max and min values for Dynamixel AX-12A here
MIN_POS = 190
MAX_POS = 815

stepTime = 0.2

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

    sock.send_multipart([b"cmd", ("s"+str(front_RL)+" 300 s"+str(back_RL)+" 300 s"+str(back_LL)+" 300 s"+str(front_LL)+" 300\n").encode('UTF-8')])
    time.sleep(stepTime)
    
    sock.send_multipart([b"cmd", ("s"+str(front_RL)+" 375 s"+str(back_RL)+" 300 s"+str(back_LL)+" 375 s"+str(front_LL)+" 300\n").encode('UTF-8')])
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", ("s"+str(front_RU)+" 512 s"+str(back_RU)+" 312 s"+str(back_LU)+" 512 s"+str(front_LU)+" 712\n").encode('UTF-8')]) ### Move Left
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", ("s"+str(front_RL)+" 300 s"+str(back_RL)+" 300 s"+str(back_LL)+" 300 s"+str(front_LL)+" 300\n").encode('UTF-8')])
    time.sleep(stepTime)
    
    sock.send_multipart([b"cmd", ("s"+str(front_RL)+" 300 s"+str(back_RL)+" 375 s"+str(back_LL)+" 300 s"+str(front_LL)+" 375\n").encode('UTF-8')])
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", ("s"+str(front_RU)+" 312 s"+str(back_RU)+" 512 s"+ str(back_LU)+" 712 s"+str(front_LU)+" 512\n").encode('UTF-8')]) ### Move Right
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
    sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s2 375 s4 300 s6 375 s8 300\n"]) ### Down
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s1 512 s3 312 s5 512 s7 312\n"]) ### rotate
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s2 300 s4 375 s6 300 s8 375\n"]) ### Down
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s1 312 s3 512 s5 312 s7 512\n"]) ### rotate
    time.sleep(stepTime)

def rotateCW():
    sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down 1
    time.sleep(stepTime)
    
    sock.send_multipart([b"cmd", b"s2 375 s4 300 s6 375 s8 300\n"]) ### Down 1
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s1 512 s3 712 s5 512 s7 712\n"]) ### rotate
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down 1
    time.sleep(stepTime)
    
    sock.send_multipart([b"cmd", b"s2 300 s4 375 s6 300 s8 375\n"]) ### Down 2
    time.sleep(stepTime)

    sock.send_multipart([b"cmd", b"s1 712 s3 512 s5 712 s7 512\n"]) ### rotate
    time.sleep(stepTime)

def reset():
    #send in two parts to prevent overload of too many commands at once
    sock.send_multipart([b"cmd", b"s1 512 s3 512 s5 512 s7 512 \n"])
    time.sleep(0.5)
    sock.send_multipart([b"cmd", b"s2 205 s4 205 s6 205 s8 205\n"])

#Action functions
def wave():
        # initial position
        sock.send_multipart([b"cmd", b"s1 512 s2 256 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(2)
        # wave middle
        sock.send_multipart([b"cmd", b"s1 512 s2 512 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.7)

        # -- cycle 1 -- #
        # wave up
        sock.send_multipart([b"cmd", b"s1 512 s2 612 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.5)
        # wave down
        sock.send_multipart([b"cmd", b"s1 512 s2 412 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.5)

        # -- cycle 2 -- #
        # wave up
        sock.send_multipart([b"cmd", b"s1 512 s2 612 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.5)
        # wave down
        sock.send_multipart([b"cmd", b"s1 512 s2 412 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.5)
        # -- end cycle -- #
        
        # wave middle
        sock.send_multipart([b"cmd", b"s1 512 s2 512 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.7)
        # reset initial position
        sock.send_multipart([b"cmd", b"s1 512 s2 256 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])

def sideWave():
        # initial position
        sock.send_multipart([b"cmd", b"s1 512 s2 256 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(2)
        # wave high
        sock.send_multipart([b"cmd", b"s1 512 s2 612 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.7)

        # -- cycle 1 -- #
        # wave high left
        sock.send_multipart([b"cmd", b"s1 412 s2 612 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.5)
        # wave high right
        sock.send_multipart([b"cmd", b"s1 612 s2 612 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.5)

        # -- cycle 2 -- #
        # wave high left
        sock.send_multipart([b"cmd", b"s1 412 s2 612 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.5)
        # wave high right
        sock.send_multipart([b"cmd", b"s1 612 s2 612 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.5)
        # -- end cycle -- #
        
        # wave high
        sock.send_multipart([b"cmd", b"s1 512 s2 612 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(0.7)
        # reset initial position
        sock.send_multipart([b"cmd", b"s1 512 s2 256 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])

def scratch():
        # initial position
        sock.send_multipart([b"cmd", b"s1 512 s2 256 s3 512 s4 256 s5 512 s6 256 s7 512 s8 256\n"])
        time.sleep(2)

        # -- cycle 1 -- #
        # Scratch low
        sock.send_multipart([b"cmd", b"s1 512 s2 412 s3 512 s4 412 s5 512 s6 412 s7 512 s8 412\n"])
        time.sleep(0.5)
        
        # Scratch high
        sock.send_multipart([b"cmd", b"s1 512 s2 205 s3 512 s4 205 s5 512 s6 205 s7 512 s8 205\n"])
        time.sleep(0.5)
        
        # -- cycle 2 -- #
        # Scratch low
        sock.send_multipart([b"cmd", b"s1 512 s2 412 s3 512 s4 412 s5 512 s6 412 s7 512 s8 412\n"])
        time.sleep(0.5)
        
        # Scratch high
        sock.send_multipart([b"cmd", b"s1 512 s2 205 s3 512 s4 205 s5 512 s6 205 s7 512 s8 205\n"])
        time.sleep(0.7)
        # -- end cycle -- #

        # reset initial position
        sock.send_multipart([b"cmd", b"s1 512 s2 256 s3 512 s4 256 s5 512 s6 256 s7 512 s8 256\n"])


if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.connect("tcp://127.0.0.1:3002")

    time.sleep(0.1)
    sock.send_multipart([b"cmd", b"attach_servos\n"])
    time.sleep(0.1)

    print("Move with WASD, QE to rotate, actions with 1-3, quit with any other key: \n")

    '''
    selected_func = input("Move with WASD, QE to rotate, actions with 1-3, quit with any other key: \n")
    selected_func = selected_func.upper()
    allowed = ["W", "A", "S", "D", "Q", "E", "1", "2", "3"]
    while(selected_func in allowed):
        if selected_func == "W":
            print("Forward \n")
            forward()
        elif selected_func == "A":
            print("Left \n")
            left()
        elif selected_func == "S":
            print("Backward \n")
            backward()
        elif selected_func == "D":
            print("Right \n")
            right()
        elif selected_func == "Q":
            print("Rotate counter-clockwise \n")
            rotateCCW()
        elif selected_func == "E":
            print("Rotate clockwise \n")
            rotateCW()
        elif selected_func == "1":
            print("Wave \n")
            wave()
        elif selected_func == "2":
            print("sideWave \n")
            sideWave()
        elif selected_func == "3":
            print("scratch \n")
            scratch()

        selected_func = input("Move with WASD, R to rotate, actions with 1-3, quit with any other key: \n")
        selected_func = selected_func.upper()
        '''
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
            wave()
        elif keyboard.is_pressed("2"):
            sideWave()
        elif keyboard.is_pressed("3"):
            scratch()
        else:
            reset()

    sock.send_multipart([b"cmd", b"reset\n"])
    time.sleep(0.7)
    sock.send_multipart([b"cmd", b"detach_servos\n"])

    sock.close()
    ctx.term()