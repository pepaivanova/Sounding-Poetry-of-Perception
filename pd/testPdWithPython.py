import os

# (Your own Python script that does whatever you need)


def send2Pd(message=''):
    # Send a message to Pd
    os.system("echo '" + message + ";" + "' | pdsend 3000")


def dspOn():
    message = 'dspOn'    # DSP turns On
    send2Pd(message)


def dspOff():
    message = 'dspOff'   # DSP turns Off
    send2Pd(message)


def setVolume():
    vol = 80    # Set volume value (0-100)
    message = '1 ' + str(vol) + ';'     # make a string for use with pdsend
    send2Pd(message)

if __name__ == "__main__":
    dspOn()
    send2Pd("read wav/motorr.wav array1")
    send2Pd("0, 260000 5892")
    # dspOff()
