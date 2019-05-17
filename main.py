# import the necessary packages

import numpy as np
import mss
import cv2
import time
import subprocess
from utils import template_matching


def a(z):
    #cv2.destroyAllWindows()
    # take a screenshot of the screen and store it in memory, then
    # convert the PIL/Pillow image to an OpenCV compatible NumPy array
    # and finally write the image to disk
    try:
        name = "gaming [Running] - Oracle VM VirtualBox" #"Diablo II"
        output = subprocess.check_output(["xwininfo", "-name", name], universal_newlines=True)
        properties = {}
        for line in output.split("\n"):
            if ":" in line:
                parts = line.split(":",1)
                properties[parts[0].strip()] = parts[1].strip()

        x = int(properties['Absolute upper-left X'])
        y = int(properties['Absolute upper-left Y'])
        w = int(properties['Width'])
        h = int(properties['Height'])
        print("Found", name, "at", x, y, w, h)
    except:
        print("Can't find", name)
    with mss.mss() as sct:  
        if (x != None):
            region = {'top': y, 'left': x, 'width': w, 'height': h}
        else:
            region = {'top': 0, 'left': 0, 'width': 0, 'height': 0}

        # Grab the data
        sct_img = sct.grab(region)
        # Inference HERE

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output="screenshot.png")
        template_matching("screenshot.png", "template.png")
        #image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        #cv2.imshow("lol", image)
        #cv2.imwrite("img.png", image)
        #print()

if __name__ == '__main__':  
    import keyboard
    keyboard.on_press_key("a", a, 'a')

    
    # Blocks until you press esc.
    keyboard.wait('esc')
    print("Exit")