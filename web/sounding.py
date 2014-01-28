from time import time
from pd import Pd

def startPd():
    #start = time()
    # start pd
    pd = Pd(port=3010, nogui=True, open="sounding.pd", cmd=None,
            path=["patches"], extra=None, stderr=False)
    pd.Send(["Hello world"])
    pd.Send(["Hello Rado"])
    pd.Send(["dspOn"])
    #pd.Send(["dspOff"])
    #pd.Send(["dspOn"])
    pd.Send(["load1 read sounds/moga.wav array1"])

    while pd.Alive():
        pd.Update()

    if pd.Alive():
        pd.Exit()
    '''
    sentexit = False
    while time() - start < 20 and pd.Alive():
        if time() - start > 5 and not sentexit:
            pd.Send(["exit"])
            sentexit = True
        print(pd.Alive())
        #pd.Send([1, 2, 3])
        pd.Update()

    if pd.Alive():
        pd.Exit()
    '''


if __name__ == "__main__":
    startPd()
