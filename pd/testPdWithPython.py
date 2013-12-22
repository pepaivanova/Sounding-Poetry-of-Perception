import os

# (Your own Python script that does whatever you need)

def send2Pd(message=''):
    # Send a message to Pd
    os.system("echo '" + message + "' | pdsend 3000")

def audioOn():
    message = '0 1;'    # Id=0 (DSP), message=1 (turn it on)
    send2Pd(message)

def setVolume():
    vol = 80    # Set volume value (0-100)
    message = '1 ' + str(vol) + ';'     # make a string for use with pdsend
    send2Pd(message)

if __name__ == "__main__":
    audioOn()
    setVolume()
    send2Pd("test")
