import json
import os.path
from subprocess import call

def getAllSounds(fileName):
    #
    # get keyTags
    call(["wget http://home.rdrlab.com:5984/sounding/_design/sounding/_view/keyTags -O " + fileName], shell=True )
    processKeyTags(fileName)

def processKeyTags(fileName):
    #
    jj = json.load(open(fileName))
    print(jj.keys())
    # print(jj["rows"])
    for i in range(len(jj["rows"])):
    # for i in range(5):
        #print(jj["rows"][i]["key"] + " - " + jj["rows"][i]["value"])
        downloadWav(jj["rows"][i]["value"], jj["rows"][i]["key"].lower() + ".wav")

def downloadWav(url, name):
    #
    if os.path.isfile(name):
	pass
    else:
	call(["wget " + url + " -O " + name], shell=True)
	call(["normalize-audio " + name], shell=True)
	print("\n")


if __name__ == "__main__":
    sounds = getAllSounds("keyTags.json")
    # print(sounds)
