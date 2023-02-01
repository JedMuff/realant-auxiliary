# Licensed under MIT licence, see LICENSE for details.
# Copyright Jed Muff, Eric Hannus, Antti Sippola, Julius Mikala, Jere Vespä. 2023

import zmq
import time


#Function for calling any of the action functions manually added to the move_list
def call_move(key, sock):
        index = key-1 #keystroke 1 = index 0 in list
        move_list = [wave, sideWave, scratch, empty_move, empty_move, empty_move, empty_move, empty_move, empty_move] #Update this list of moves as new functions are added!
        if index < len(move_list):
                move_list[index](sock)


#Action functions

def empty_move(sock):
        #This function is a placeholder used in move_list if no other function is used, so that something will happen when each of the keys 1-9 are pressed.
        print("No move has been added to this key yet.")
        time.sleep(1)

def wave(sock):
        print("wave") #for debugging
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

def sideWave(sock):
        print("sidewave") #for debugging
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

def scratch(sock):
        print("scratch") #for debugging
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