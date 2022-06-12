# arduino_LED_user.py

import time
from tkinter import Label, PhotoImage
from inputs import get_gamepad
import math
import threading

import serial
ser = serial.Serial('COM4', 115200)
# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager


class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0
        self.DPadX = 0

        self._monitor_thread = threading.Thread(
            target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def read(self):  # return the buttons/triggers that you care about in this methode
        LX = self.LeftJoystickX
        LY = self.LeftJoystickY
        a = self.A
        x = self.X  # b=1, x=2
        y = self.Y
        b = self.B

        rb = self.RightBumper
        lb = self.LeftBumper
        rt = self.RightTrigger
        lt = self.LeftTrigger
        return [LX, LY, a, b, x, y, lb, rb, lt, rt]

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / \
                        XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / \
                        XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / \
                        XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / \
                        XboxController.MAX_JOY_VAL  # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / \
                        XboxController.MAX_TRIG_VAL  # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / \
                        XboxController.MAX_TRIG_VAL  # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state
                elif event.code == 'BTN_WEST':
                    self.X = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state
                elif event.code == "ABS_HAT0X":
                    self.DPadX = event.state


global IsLEDOn
IsLEDOn = False

global i
i = 0
global x
x = 0
global a
a = 0
global b
b = 0
global c
c = 0
ser.write("LED Off\r".encode())


def BaseUp():
    ser.write("Up\r".encode())


def BaseDown():
    ser.write("Down\r".encode())


def StopBase():
    ser.write("Stop Base\r".encode())


def Extend():
    ser.write("Extend\r".encode())


def Retract():
    ser.write("Retract\r".encode())


def StopExtend():
    ser.write("Stop Extend\r".encode())


def TiltUp():
    ser.write("Tilt Up\r".encode())


def TiltDown():
    ser.write("Tilt Down\r".encode())


def StopTilt():
    ser.write("Stop Tilt\r".encode())


def Pinch():
    ser.write("Pinch\r".encode())


def Release():
    ser.write("Release\r".encode())


def StopGripper():
    ser.write("Stop Gripper\r".encode())


def Right():
    ser.write("Right\r".encode())


def Left():
    ser.write("Left\r".encode())


def StopRotation():
    ser.write("Stop Rotation\r".encode())


def LEDOn():
    ser.write("LED On\r".encode())
    print("LED On")


def LEDOff():
    ser.write("LED Off\r".encode())
    print("LED Off")


def ToggleLED():
    global IsLEDOn
    if IsLEDOn:
        LEDOff()
        IsLEDOn = False
    else:
        LEDOn()
        IsLEDOn = True


while True:
    try:
        xbox = XboxController()
        while True:
            xbox.read()
            time.sleep(0.1)
            if xbox.X == 1:
                
                ToggleLED()
                """ changeLEDToggleColor() """
            if xbox.Start == 1:
                ser.reset_output_buffer()
                ser.reset_input_buffer()
            if xbox.B == 1:
                ser.close()
                exit()
            if xbox.LeftJoystickY > 0.9:
                BaseUp()
                c += 1
            if xbox.LeftJoystickY < -0.9:
                BaseDown()
                c += 1
            if (xbox.LeftJoystickY < 0.9 and xbox.LeftJoystickY > -0.9) and c >= 1:
                StopBase()
                c = 0
            if xbox.RightBumper == 1:
                Extend()
                b += 1
            if xbox.LeftBumper == 1:
                Retract()
                b += 1
            if (xbox.LeftBumper == 0 and xbox.RightBumper == 0) and b >= 1:
                StopExtend()
                b = 0
            if xbox.RightJoystickY > 0.9:
                TiltUp()
                a += 1
                print("a = " + str(a))
            if xbox.RightJoystickY < -0.9:
                TiltDown()
                a += 1
                print("a = " + str(a))
            if (xbox.RightJoystickY < 0.9 and xbox.RightJoystickY > -0.9) and a >= 1:
                StopTilt()
                a = 0
                print("a = " + str(a))
            if xbox.RightTrigger > 0.9:
                Pinch()
                i += 1
            if xbox.LeftTrigger > 0.9:
                Release()
                i += 1
                print("i = " + str(i))
            if (xbox.RightTrigger == 0 and xbox.LeftTrigger == 0) and i >= 1:
                StopGripper()
                i = 0
                print("i = " + str(i))
            if xbox.LeftJoystickX > 0.9:
                Right()
                x += 1
                print("x = " + str(x))
            if xbox.LeftJoystickX < -0.9:
                Left()
                x += 1
                print("x = " + str(x))
            if (xbox.LeftJoystickX < 0.9 and xbox.LeftJoystickX > -0.9) and x >= 1:
                StopRotation()
                x = 0
                print("x = " + str(x))
    except:
        print("Error")
        ser.close()
        break
