# Licensed under MIT licence, see LICENSE for details.
# Copyright Jed Muff, Eric Hannus, Antti Sippola, Julius Mikala, Jere Vespä. 2023

import zmq
import time

import random #for random_test()

#Set max and min values for Dynamixel AX-12A here
MIN_POS = 190
MAX_POS = 815


#Movement functions

def forward():
    #all legs to moving position
    sock.send_multipart([b"cmd", b"s7 358 s5 666 s3 358 s1 666 \n"])
    time.sleep(2)

    #front legs forward
    sock.send_multipart([b"cmd", b"s2 512\n"])
    time.sleep(1)
    sock.send_multipart([b"cmd", b"s8 512\n"])
    time.sleep(1)

    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s2 205 s4 512 s6 512 s8 205 \n"])
            time.sleep(1)
            #reset legs one by one
            sock.send_multipart([b"cmd", b"s2 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s6 205\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s8 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s4 205\n"])
            time.sleep(1)

            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s2 205 s4 512 s6 512 s8 205 \n"])
            time.sleep(1)
            #reset legs one by one v2
            sock.send_multipart([b"cmd", b"s8 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s4 205\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s2 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s6 205\n"])
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    #reset to base position
    reset()
    time.sleep(2)


def backward():
    #all legs to moving position
    sock.send_multipart([b"cmd", b"s7 358 s5 666 s3 358 s1 666 \n"])
    time.sleep(2)

    #back legs forward
    sock.send_multipart([b"cmd", b"s4 512\n"])
    time.sleep(1)
    sock.send_multipart([b"cmd", b"s6 512\n"])
    time.sleep(1)

    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            #simultaneous command to all legs = large backward movememnt
            sock.send_multipart([b"cmd", b"s4 205 s2 512 s8 512 s6 205 \n"])
            time.sleep(1)
            #reset legs one by one
            sock.send_multipart([b"cmd", b"s6 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s2 205\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s4 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s8 205\n"])
            time.sleep(1)

            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s4 205 s2 512 s8 512 s6 205 \n"])
            time.sleep(1)
            #reset legs one by one v2
            sock.send_multipart([b"cmd", b"s4 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s8 205\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s6 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s2 205\n"])
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    #reset to base position
    reset()
    time.sleep(2)

def left():
    #all legs to moving position
    sock.send_multipart([b"cmd", b"s5 358 s7 666 s1 358 s3 666 \n"])
    time.sleep(2)

    #left legs forward
    sock.send_multipart([b"cmd", b"s8 512\n"])
    time.sleep(1)
    sock.send_multipart([b"cmd", b"s6 512\n"])
    time.sleep(1)

    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s6 205 s4 512 s2 512 s8 205 \n"])
            time.sleep(1)
            #reset legs one by one
            sock.send_multipart([b"cmd", b"s6 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s2 205\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s8 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s4 205\n"])
            time.sleep(1)

            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s6 205 s4 512 s2 512 s8 205 \n"])
            time.sleep(1)
            #reset legs one by one v2
            sock.send_multipart([b"cmd", b"s8 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s4 205\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s6 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s2 205\n"])
            time.sleep(1)
    
    except KeyboardInterrupt:
        pass    

    #reset to base position
    reset()
    time.sleep(2)

def right():
    #all legs to moving position
    sock.send_multipart([b"cmd", b"s5 358 s7 666 s1 358 s3 666 \n"])
    time.sleep(2)

    #right legs forward
    sock.send_multipart([b"cmd", b"s2 512\n"])
    time.sleep(1)
    sock.send_multipart([b"cmd", b"s4 512\n"])
    time.sleep(1)

    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s2 205 s6 512 s8 512 s4 205 \n"])
            time.sleep(1)
            #reset legs one by one
            sock.send_multipart([b"cmd", b"s2 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s6 205\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s4 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s8 205\n"])
            time.sleep(1)

            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s2 205 s6 512 s8 512 s4 205 \n"])
            time.sleep(1)
            #reset legs one by one v2
            sock.send_multipart([b"cmd", b"s4 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s8 205\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s2 512\n"])
            time.sleep(1)
            sock.send_multipart([b"cmd", b"s6 205\n"])
            time.sleep(1)
    
    except KeyboardInterrupt:
        pass
    
    #reset to base position
    reset()
    time.sleep(2)


def rotateCCW():
    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            #initialize position
            sock.send_multipart([b"cmd", b"s1 512 s3 552 s5 512 s7 472 \n"])
            time.sleep(1)

            #lift first & third leg
            sock.send_multipart([b"cmd", b"s2 300 s6 300 \n"])
            time.sleep(1)
            #move first & third leg
            sock.send_multipart([b"cmd", b"s1 700 s5 700 \n"])
            time.sleep(1)
            #drop first & third leg
            sock.send_multipart([b"cmd", b"s2 205 s6 205 \n"])
            time.sleep(1)

            #lift second & foutrh leg
            sock.send_multipart([b"cmd", b"s8 300 s4 300 \n"])
            time.sleep(1)
            #move second & fourth leg
            sock.send_multipart([b"cmd", b"s7 700 s3 700 \n"])
            time.sleep(1)
            #drop second & fourth leg
            sock.send_multipart([b"cmd", b"s8 205 s4 205 \n"])
            time.sleep(1)

            #now it snaps back to inital position at the start of the loop

    
    except KeyboardInterrupt:
        pass

    #reset to base position
    reset()
    time.sleep(2)

def rotateCW():
    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            #initialize position
            sock.send_multipart([b"cmd", b"s7 512 s3 552 s5 512 s1 472 \n"])
            time.sleep(1)

            #lift first & third leg
            sock.send_multipart([b"cmd", b"s2 300 s6 300 \n"])
            time.sleep(1)
            #move first & third leg
            sock.send_multipart([b"cmd", b"s1 324 s5 324 \n"])
            time.sleep(1)
            #drop first & third leg
            sock.send_multipart([b"cmd", b"s2 205 s6 205 \n"])
            time.sleep(1)

            #lift second & foutrh leg
            sock.send_multipart([b"cmd", b"s8 300 s4 300 \n"])
            time.sleep(1)
            #move second & fourth leg
            sock.send_multipart([b"cmd", b"s7 324 s3 324 \n"])
            time.sleep(1)
            #drop second & fourth leg
            sock.send_multipart([b"cmd", b"s8 205 s4 205 \n"])
            time.sleep(1)

            #now it snaps back to inital position at the start of the loop

    
    except KeyboardInterrupt:
        pass

    #reset to base position
    reset()
    time.sleep(2)

def reset():
    sock.send_multipart([b"cmd", b"s1 512 s2 205 s3 512 s4 205 s5 512 s6 205 s7 512 s8 205\n"])


#Action functions
def wave():
        # initial position
        sock.send_multipart([b"cmd", b"s1 512 s2 256 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(2)
        # wave middle
        sock.send_multipart([b"cmd", b"s1 512 s2 512 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(1)

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
        time.sleep(1)
        # reset initial position
        sock.send_multipart([b"cmd", b"s1 512 s2 256 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])

def sideWave():
        # initial position
        sock.send_multipart([b"cmd", b"s1 512 s2 256 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(2)
        # wave high
        sock.send_multipart([b"cmd", b"s1 512 s2 612 s3 552 s4 256 s5 512 s6 256 s7 472 s8 256\n"])
        time.sleep(1)

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
        time.sleep(1)
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
        time.sleep(1)
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
    

    sock.send_multipart([b"cmd", b"reset\n"])
    time.sleep(1)
    sock.send_multipart([b"cmd", b"detach_servos\n"])

    sock.close()
    ctx.term()