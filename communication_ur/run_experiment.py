from numpy.core.defchararray import array
from urinterface.robot_connection import RobotConnection
import numpy as np
from math import pi
from pathlib import Path
import time
import msvcrt
from points import *


def deg_to_rad(deg):
    rad = deg * pi / 180
    return rad


def loosen_screw(robot, previous_waypoint):
    loosen_program_name = "/programs/loosen_screw.urp"
    robot.load_program(loosen_program_name)
    robot.play_program()
    time.sleep(1)
    robot.movej(previous_waypoint, v=1.0, a=0.5)

def tighten_screw(robot, previous_waypoint):
    tighten_program_name = "/programs/tighten_screw.urp"
    robot.load_program(tighten_program_name)
    robot.play_program()
    time.sleep(1)
    robot.movej(previous_waypoint, v=1.0, a=0.5)

v0 = 1.0
a0 = 5.0
vm_ip = "192.168.1.2"
# vm_ip = "192.168.142.128"
ur5e = RobotConnection(vm_ip) # Establish dashboard connection (port 29999) and controller connection (port 30002)

f_name = "test_motion1.csv"
filename = Path("test_results") / Path(f_name)
config_file =  Path("resources") / Path("record_configuration.xml")
ur5e.start_recording(filename=filename, overwrite=True, frequency=50, config_file=config_file, publish_topic=["actual_q"]) # start recording and place the recorded data in test_motion.csv

time.sleep(1)


# while True:
#     ur5e.load_program("/programs/test_movement.urp")
#     ur5e.play_program()
#     time.sleep(10)


while True:
    k = msvcrt.getwche()
    if k == "c":
        break
    elif k in {"1","2","3","4","5","6","7","8","9"}:
        if k == "1":
            ur5e.load_program("/programs/test_movement.urp")
            ur5e.play_program()
            time.sleep(10)
        elif k == "2":
            ur5e.load_program("/programs/short_program.urp")
            ur5e.play_program()
        elif k == "3":
            ur5e.load_program("/programs/screw_points.urp")
            ur5e.play_program()
    
    # reset k
    k = "a"

ur5e.stop_recording()
