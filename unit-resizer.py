# Transforms all sizes in .css from *px to *vw.
# Uses Decimal library
# Saves original .css in .css.bak file
import sys
import re
from decimal import *

input_file = "style.css"
getcontext().prec = 3
vw = Decimal(3.2)

content = ""

stream_in = open(input_file, "r")
for line in stream_in:
    content += line
stream_in.close()

streamOut = open(input_file + ".bak", "w+")
for l in content:
    streamOut.write(l)
streamOut.close()

def rebuild_sizes(regx, content):
    rebuilt_stylesheet = ""
    parts = regx.findall(content)
    for u in parts:
        num = Decimal(int(u[:len(u)-2]))
        res = num/vw
        index = content.find(u)
        rebuilt_stylesheet += content[:index] + (" " + str(res) + "vw")
        content = content[index + len(u):]
    return(rebuilt_stylesheet + content)

content = rebuild_sizes(re.compile(r"\s\d*px"), content)
content = rebuild_sizes(re.compile(r"\s-\d*px"), content)

streamOut = open(input_file, "w+")
for l in content:
    streamOut.write(l)
streamOut.close()
