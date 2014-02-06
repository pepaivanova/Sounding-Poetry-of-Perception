import os


def processPoetry(text):
    # process text from the input
    fileslist = getFiles('patches/sounds')
    temp = []
    poetry = text.split()
    for i in range(len(poetry)):
        if '.' in poetry[i]:
            # find the position of dot symbol
            pos = poetry[i].index('.')
            print(pos)
            # replace '.' symbol with 'dot'
            poetry[i] = poetry[i].strip('.') + ' dot'
            print(type(poetry))
    for i in range(len(poetry)):
        temp[i] = poetry[i] + ' '
        text = ''.join(temp)
    print(text)
    #os.system(('java -cp patches/bin AudioMix "%s" 0.1 "%s"', poetry[2], poetry))
    print(poetry)
    #pass

def checkSymbol(symbol, word):
    #
    pass

def getFiles(folder):
    '''
    Search for all .mp3 and .wav files in folder.
    Returns tuple with all files
    '''
    musicFiles = []
    for root, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(('.mp3', '.wav')):
                musicFiles.append(filename)
    # return tuple
    return tuple(musicFiles)

def checkWord(word, filelist):
    '''
    Check if word exists in filelist.
    Return: bool (True/False)
    '''
    match = False
    for i in range(len(filelist)):
        if word in filelist[i]:
            match = True
    # returns True if word exists in list
    return match


def main():
    processPoetry('fairytale with 3dprinter.')

if __name__ == "__main__":
    main()


