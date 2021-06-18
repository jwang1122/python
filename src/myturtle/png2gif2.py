"""
https://pythonprogramming.altervista.org/png-to-gif/
"""

import subprocess
import os
 
i = "images/*.png"
f=open("output.gif","w")
f.close()
o = "output.gif"
subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
os.system("start output.gif")