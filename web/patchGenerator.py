import os


def getFilesList(folder):
    '''
    Search for all .wav and .mp3 files in folder.
    Return list with names.
    '''
    musicFiles = []
    for root, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(('.wav', '.mp3')):
                musicFiles.append(filename)
    # return list of wav and mp3 files in the folder
    return musicFiles


def checkWord(word, filelist):
    '''
    Checks if given word exists in filelist.
    Return True or False
    '''
    match = False
    for i in range(len(filelist)):
        if word in filelist[i]:
            match = True
    # returns True or False
    return match


if __name__ == "__main__":
    f = getFilesList('../pd/wav')
    print(type(f))
    print("----------")
    # print all found files in folder
    print(f)
    # check if some word exists
    c = checkWord('gridge', f)
    # print True or False
    print(c)
