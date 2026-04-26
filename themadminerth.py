import subprocess
import time
import random
from PIL import Image
import cv2
import numpy as np
import pytesseract
import os
import json
from datetime import datetime
from io import BytesIO

#nosleep
import ctypes
import sys
import atexit

if sys.platform.startswith("win"):
    print("🔌 Preventing Windows from sleeping (screen may still turn off)...")

    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001

    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED
    )

    def restore_sleep():
        print("🛑 Restoring Windows sleep settings.")
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

    atexit.register(restore_sleep)
    
# adb devices
# adb tcpip 5555
# adb connect 192.168.0.141:5555


#CONSTANTS
WAIT_AFTER_ATTACK_CLICK = 0.2
WAIT_AFTER_FIND_MATCH = 6
WAIT_BATTLE_DURATION = 50  # in seconds
WAIT_AFTER_END_BATTLE = 3
WAIT_BETWEEN_CYCLES = 5  # time between attack cycles
SEARCHING = 6
IMG_DIR = "mob/mobsea"
LAST_HERO_COORDS = None



def main_loop():
    attack_count = 0
    """
    Implementation omitted.
    In production, this handles whole attacking cycle.
    """
    raise NotImplementedError("Removed for demo")



if __name__ == "__main__":
    main_loop()
