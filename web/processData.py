# process messages from PD


def processData(data):
    #
    if data is not None:
        print(data)
        if 'play-1' in data:
            return "load2 read sounds/motorr.wav array2"
        elif 'play-2' in data:
            return "load1 read sounds/moga.wav array1"
        else:
            return "exit"
