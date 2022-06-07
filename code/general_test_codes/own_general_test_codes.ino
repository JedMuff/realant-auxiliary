#include <Dynamixel2Arduino.h>

//Board settings
#define DXL_SERIAL   Serial1 //OpenCM9.04 EXP Board's DXL port Serial. (Serial1 for the DXL port on the OpenCM 9.04 board)
#define DEBUG_SERIAL Serial
const uint8_t DXL_DIR_PIN = 28; //OpenCM9.04 EXP Board's DIR PIN. (28 for the DXL port on the OpenCM 9.04 board)

const uint8_t DXL_ID = 6;
const float DXL_PROTOCOL_VERSION = 1.0;

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
  
}

void loop() {
  // LED test
  dxl.ledOn(DXL_ID);
  delay(500);
  dxl.ledOff(DXL_ID);
  delay(500);

  //Memory read test
  //CW & CCW limits
  /*
  DEBUG_SERIAL.print("CW:");
  DEBUG_SERIAL.print(dxl.readControlTableItem(CW_ANGLE_LIMIT, DXL_ID));
  DEBUG_SERIAL.print(" CCW:");
  DEBUG_SERIAL.print(dxl.readControlTableItem(CCW_ANGLE_LIMIT, DXL_ID));
  DEBUG_SERIAL.print("\n");
  */

  //Read position
  DEBUG_SERIAL.print("Current position:");
  DEBUG_SERIAL.print(dxl.readControlTableItem(PRESENT_POSITION, DXL_ID));
  DEBUG_SERIAL.print("\n");
  
  
  //Position control test
  dxl.setGoalPosition(DXL_ID, 200);
  delay(2000);
  dxl.setGoalPosition(DXL_ID, 512);
  delay(2000);
  dxl.setGoalPosition(DXL_ID, 800);
  delay(2000);
  
}
