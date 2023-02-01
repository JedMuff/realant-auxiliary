// Licensed under MIT licence, see LICENSE for details.
// Copyright Jed Muff, Eric Hannus, Antti Sippola, Julius Mikala, Jere Vespä. 2023

#include <Dynamixel2Arduino.h>

//Board settings
#define DXL_SERIAL   Serial1 //OpenCM9.04 EXP Board's DXL port Serial. (Serial1 for the DXL port on the OpenCM 9.04 board)
#define DEBUG_SERIAL Serial
const uint8_t DXL_DIR_PIN = 28; //OpenCM9.04 EXP Board's DIR PIN. (28 for the DXL port on the OpenCM 9.04 board)


const float DXL_PROTOCOL_VERSION = 1.0;

// !!! NOTE !!! You will need to remember the new ID to be able to contact the servo in the future!
const uint8_t DXL_ID = 6; //Old ID
const uint8_t New_ID = 6; // New ID

Dynamixel2Arduino dxl(DXL_SERIAL, DXL_DIR_PIN);

//This namespace is required to use Control table item names
using namespace ControlTableItem;

void setup() {
  // put your setup code here, to run once:

  // Set Port baudrate to 57600bps. This has to match with DYNAMIXEL baudrate.
  dxl.begin(1000000);
  // Set Port Protocol Version. This has to match with DYNAMIXEL protocol version.
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  // Get DYNAMIXEL information
  dxl.ping(DXL_ID);

  
  //Settings for position control
  // Turn off torque when configuring items in EEPROM area
  dxl.torqueOff(DXL_ID);
  dxl.setOperatingMode(DXL_ID, OP_POSITION);
  dxl.torqueOn(DXL_ID);

  // Limit the maximum velocity in Position Control Mode. Use 0 for Max speed
  dxl.writeControlTableItem(PROFILE_VELOCITY, DXL_ID, 30);

 //Setting new ID
 dxl.setID(DXL_ID, New_ID);
 
}

void loop() {
  // LED test
  dxl.ledOn(New_ID);
  delay(500);
  dxl.ledOff(New_ID);
  delay(500);

  //Memory read test
  //ID, CW & CCW limits
  DEBUG_SERIAL.print("Current (new) ID:");
  DEBUG_SERIAL.print(dxl.readControlTableItem(ID, New_ID));
  DEBUG_SERIAL.print(" CW:");
  DEBUG_SERIAL.print(dxl.readControlTableItem(CW_ANGLE_LIMIT, New_ID));
  DEBUG_SERIAL.print(" CCW:");
  DEBUG_SERIAL.print(dxl.readControlTableItem(CCW_ANGLE_LIMIT, New_ID));
  DEBUG_SERIAL.print("\n");
  
}
