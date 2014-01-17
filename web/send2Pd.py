import os

# (Your own Python script that does whatever you need)

def checkPdStarted(processname):
    tmp = os.popen("ps -Af").read()
    proccount = tmp.count(processname)
    if proccount > 0:
        return True
    # process doesn't exist
    return False

def startStopPd(puredata):
    # start / stop Pd process
    os.system(puredata)

def send2Pd(message=''):
    # Send a message to Pd
    os.system("echo '" + message + ";" + "' | pdsend 3000")

def processText(text):
    # Get text from flask and send it to pd
    words = text.split()
    for i in range(len(words)):
        send2Pd("read wav/" + words[i] + ".wav array1")
        send2Pd("0, 260000 5892")
    # print(words)
    print("Done")

def dspOn():
    message = 'dspOn'    # DSP turns On
    send2Pd(message)

def dspOff():
    message = 'dspOff'   # DSP turns Off
    send2Pd(message)

if __name__ == "__main__":
    dspOn()
    send2Pd("play;")
    # dspOff()
    text = "I hear motorr while we are walking. "
    processText(text)
    print(checkPdStarted('pdextended'))
