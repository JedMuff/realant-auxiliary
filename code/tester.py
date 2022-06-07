import zmq #library for communication with the robot
import time #for timing

#Set max and min values for Dynamixel AX-12A here
MIN_POS = 210
MAX_POS = 795

def send_cmd(ID, value):
    command = "s" + str(ID) + " " + str(value) + "\n"
    b_command = command.encode('UTF-8')
    print(b_command) #test without robot attached

    sock.send_multipart([b"cmd", b_command])
    time.sleep(2) #Sleep is carried out within this function > not needed to call separately in Main

def reset(ID):
    if (int(ID) % 2) == 0: #even ID = outer joint
        send_cmd(ID, 205)
    else: #odd ID = inner joint
        send_cmd(ID, 512)

def reset_all():
    #send in two parts to prevent overload of too many commands at once
    sock.send_multipart([b"cmd", b"s1 512 s3 512 s5 512 s7 512 \n"])
    time.sleep(0.5)
    sock.send_multipart([b"cmd", b"s2 205 s4 205 s6 205 s8 205\n"])
    
    #Note: This command could also be used here to achieve the same thing, with the default positions set in the Arduni code (224 instead of 205).
    #sock.send_multipart([b"cmd", b"reset\n"])


def test_servo(ID):
    send_cmd(ID, MAX_POS)
    send_cmd(ID, MIN_POS)
    reset(ID)
 
if __name__ == '__main__':
    #zmq for communication with the RealAnt, setting up a socket 
    ctx = zmq.Context() 
    sock = ctx.socket(zmq.PUB) 
    sock.connect("tcp://127.0.0.1:3002") 
 
    #Attaching servos. This command is executed in the Arduino code running in the RealAnt.
    time.sleep(0.1) 
    sock.send_multipart([b"cmd", b"attach_servos\n"]) 
    time.sleep(0.1) 

    selected_func = input("Press F for testing servo motion in full range, I for giving input, R for resetting postion, A for resetting position of all servos, or any other key to quit:\n")
    selected_func = selected_func.upper()
    allowed_commands = ["F", "I", "R", "A"]
    while(selected_func in allowed_commands):
        if selected_func == "F":
            print("Testing servo motion in full range.\n")
            ID = input("Give ID in range 1 to 8 to test:\n")
            test_servo(ID)
        elif selected_func == "I":
            print("Testing servo motion with given goal position.\n")
            ID = input("Give ID in range 1 to 8 to test:\n")
            value = input("Give servo position in range "+str(MIN_POS)+" to "+str(MAX_POS)+":\n")
            send_cmd(ID, value)
        elif selected_func == "R":
            print("Resetting servo to default position.\n")
            ID = input("Give ID in range 1 to 8 to reset position:\n")
            reset(ID)
        elif selected_func == "A":
            print("Resettings all servos to default position.\n")
            reset_all()

        selected_func = input("Press F for testing servo motion in full range, I for giving input, R for resetting postion, A for resetting position of all servos, or any other key to quit:\n")
        selected_func = selected_func.upper()
    
    #Resetting all the servo positions via a command executed in the Arduino code running in the RealAnt. 
    sock.send_multipart([b"cmd", b"reset\n"])
    time.sleep(1)
    #Detaching servos. This command is executed in the Arduino code running in the RealAnt.
    sock.send_multipart([b"cmd", b"detach_servos\n"])

    sock.close()
    ctx.term()