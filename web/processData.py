# process messages from PD

def processData(data):
    #
    if data is not None:
        print(data)
        if 'play' in data:
            return "load2 read sounds/motorr.wav array2"
        else:
            print('error')

