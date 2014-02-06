import os


def processPoetry(text):
    # process text from the input
    fileslist = getFiles('patches/sounds')
    temp = []
    poetry = text.strip('.!-')
    background = poetry.split()
    #print(poetry)
    #print(type(poetry))
    # background set to the second word in text
    msg = 'java -cp bin AudioMix "' + background[1] + '" 0.1 "' + poetry + '"'
    os.system(msg)

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
    return musicFiles

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
    processPoetry('Motorr thegridge moga motorr moga nemoga.')

if __name__ == "__main__":
    main()

