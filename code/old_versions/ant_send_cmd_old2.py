# Licensed under MIT licence, see LICENSE for details.
# Copyright Jed Muff, Eric Hannus, Antti Sippola, Julius Mikala, Jere Vespä. 2023

import zmq
import time


#Set max and min values for Dynamixel AX-12A here
MIN_POS = 0 
MAX_POS = 1023


#NOTE: might need changes to ant11_cmd_dxl.ino if giving strings for only 1 servo not for all 8 does not work directly
def send_cmd(index, value):
	command = str(index) + " " + str(value) + "\n"
	#print(command) #test without robot attached
	b_command = command.encode('UTF-8')
	print(b_command) #test without robot attached

	sock.send_multipart([b"cmd", b_command])
	time.sleep(1) #Sleep is carried out within this function > not needed to call separately in Main

def test_servo(index):
	send_cmd(index, MAX_POS)
	send_cmd(index, MIN_POS)

if __name__ == '__main__':
    ctx = zmq.Context()
    sock = ctx.socket(zmq.PUB)
    sock.connect("tcp://127.0.0.1:3002")

    time.sleep(0.1)
    sock.send_multipart([b"cmd", b"attach_servos\n"])
    time.sleep(0.1)

    selected_func = input("Press R for testing servo motion in full range, I for giving input, or any other key to quit:\n")
    selected_func = selected_func.upper()
    while(selected_func == "R" or selected_func == "I"):
    	if selected_func == "R":
    		print("Testing servo motion in full range.\n")
    		index = input("Give index in range 1 to 8 to test:\n")
    		test_servo(index)
    	elif selected_func == "I":
            print("Testing servo motion with given goal position.")
            index = input("Give index in range 1 to 8 to test:\n")
            value = input("Give servo position in range "+str(MIN_POS)+" to "+str(MAX_POS)+":\n")
            send_cmd(index, value)
            
    	selected_func = input("Press R for testing servo motion in full range, I for giving input, or any other key to quit:\n")
    	selected_func = selected_func.upper()
    

    sock.send_multipart([b"cmd", b"reset\n"])
    time.sleep(1)
    sock.send_multipart([b"cmd", b"detach_servos\n"])

    sock.close()
    ctx.term()