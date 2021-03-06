from Adafruit_Thermal import *

maxCol = 32
printer = Adafruit_Thermal("/dev/ttyO2", 19200, timeout=5)
printer.begin()
printer.upsideDownOn()

def parse(text):
    r = text.split(' ')
    curLine = ''
    fin = []
    tally = 0
    for w in r:
        if len(w)+len(curLine) > (maxCol-1):
            fin.append(curLine)
            curLine = ''
            curLine+=w
        else:
            curLine+=' '+w
    # print curLine
    fin.append(curLine)
    fin[0] = fin[0].lstrip()
    fin.reverse()
    rt = '\n'.join(fin)
    return rt+'\n'
