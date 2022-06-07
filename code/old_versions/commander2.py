# Licensed under MIT licence, see LICENSE for details.
# Copyright Ote Robotics Ltd. 2020

import zmq
import time

import random #for random_test()

#Set max and min values for Dynamixel AX-12A here
MIN_POS = 190
MAX_POS = 815

stepTime = 0.2

#Movement functions

def forward():
    print("Press Ctrl+C to exit movement")
    try:
        while(True):
                # Step D
                sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down 1
                time.sleep(stepTime)
                
                # Step D
                sock.send_multipart([b"cmd", b"s2 375 s4 300 s6 375 s8 300\n"]) ### Down 1
                time.sleep(stepTime)

                # Step E
                sock.send_multipart([b"cmd", b"s1 512 s3 312 s5 512 s7 712\n"]) ### Move Left
                time.sleep(stepTime)

                # Step D
                sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down 1
                time.sleep(stepTime)
                
                # Step G
                sock.send_multipart([b"cmd", b"s2 300 s4 375 s6 300 s8 375\n"]) ### Down 2
                time.sleep(stepTime)

                # Step H
                sock.send_multipart([b"cmd", b"s1 312 s3 512 s5 712 s7 512\n"]) ### Move Right
                time.sleep(stepTime)

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
    time.sleep(0.7)
    sock.send_multipart([b"cmd", b"s6 512\n"])
    time.sleep(0.7)

    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            #simultaneous command to all legs = large backward movememnt
            sock.send_multipart([b"cmd", b"s4 205 s2 512 s8 512 s6 205 \n"])
            time.sleep(0.7)
            #reset legs one by one
            sock.send_multipart([b"cmd", b"s6 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s2 205\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s4 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s8 205\n"])
            time.sleep(0.7)

            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s4 205 s2 512 s8 512 s6 205 \n"])
            time.sleep(0.7)
            #reset legs one by one v2
            sock.send_multipart([b"cmd", b"s4 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s8 205\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s6 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s2 205\n"])
            time.sleep(0.7)

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
    time.sleep(0.7)
    sock.send_multipart([b"cmd", b"s6 512\n"])
    time.sleep(0.7)

    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s6 205 s4 512 s2 512 s8 205 \n"])
            time.sleep(0.7)
            #reset legs one by one
            sock.send_multipart([b"cmd", b"s6 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s2 205\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s8 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s4 205\n"])
            time.sleep(0.7)

            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s6 205 s4 512 s2 512 s8 205 \n"])
            time.sleep(0.7)
            #reset legs one by one v2
            sock.send_multipart([b"cmd", b"s8 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s4 205\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s6 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s2 205\n"])
            time.sleep(0.7)
    
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
    time.sleep(0.7)
    sock.send_multipart([b"cmd", b"s4 512\n"])
    time.sleep(0.7)

    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s2 205 s6 512 s8 512 s4 205 \n"])
            time.sleep(0.7)
            #reset legs one by one
            sock.send_multipart([b"cmd", b"s2 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s6 205\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s4 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s8 205\n"])
            time.sleep(0.7)

            #simultaneous command to all legs = large forward movememnt
            sock.send_multipart([b"cmd", b"s2 205 s6 512 s8 512 s4 205 \n"])
            time.sleep(0.7)
            #reset legs one by one v2
            sock.send_multipart([b"cmd", b"s4 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s8 205\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s2 512\n"])
            time.sleep(0.7)
            sock.send_multipart([b"cmd", b"s6 205\n"])
            time.sleep(0.7)
    
    except KeyboardInterrupt:
        pass
    
    #reset to base position
    reset()
    time.sleep(2)


def rotateCCW():
    print("Press Ctrl+C to exit movement")
    try:
        while(True):
            # Step D
            sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down 1
            time.sleep(stepTime)
            
            # Step D
            sock.send_multipart([b"cmd", b"s2 375 s4 300 s6 375 s8 300\n"]) ### Down 1
            time.sleep(stepTime)

            # Step E
            sock.send_multipart([b"cmd", b"s1 512 s3 312 s5 512 s7 312\n"]) ### rotate
            time.sleep(stepTime)

            # Step D
            sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down 1
            time.sleep(stepTime)
            
            # Step G
            sock.send_multipart([b"cmd", b"s2 300 s4 375 s6 300 s8 375\n"]) ### Down 2
            time.sleep(stepTime)

            # Step H
            sock.send_multipart([b"cmd", b"s1 312 s3 512 s5 312 s7 512\n"]) ### rotate
            time.sleep(stepTime)
    
    except KeyboardInterrupt:
        pass

    #reset to base position
    reset()
    time.sleep(2)

def rotateCW():
    print("Press Ctrl+C to exit movement")
    try:
        while(True):
                # Step D
                sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down 1
                time.sleep(stepTime)
                
                # Step D
                sock.send_multipart([b"cmd", b"s2 375 s4 300 s6 375 s8 300\n"]) ### Down 1
                time.sleep(stepTime)

                # Step E
                sock.send_multipart([b"cmd", b"s1 512 s3 712 s5 512 s7 712\n"]) ### rotate
                time.sleep(stepTime)

                # Step D
                sock.send_multipart([b"cmd", b"s2 300 s4 300 s6 300 s8 300\n"]) ### Down 1
                time.sleep(stepTime)
                
                # Step G
                sock.send_multipart([b"cmd", b"s2 300 s4 375 s6 300 s8 375\n"]) ### Down 2
                time.sleep(stepTime)

                # Step H
                sock.send_multipart([b"cmd", b"s1 712 s3 512 s5 712 s7 512\n"]) ### rotate
                time.sleep(stepTime)

            #now it snaps back to inital position at the start of the loop

    
    except KeyboardInterrupt:
        pass

    #reset to base position
    reset()
    time.sleep(2)

def reset():
    #sock.send_multipart([b"cmd", b"s1 512 s2 205 s3 512 s4 205 s5 512 s6 205 s7 512 s8 205\n"])
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
    time.sleep(0.7)
    sock.send_multipart([b"cmd", b"detach_servos\n"])

    sock.close()
    ctx.term()