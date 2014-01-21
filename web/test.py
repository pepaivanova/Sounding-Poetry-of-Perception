from time import time
from pd import Pd

start = time()
# start pd
pd = Pd(port=3010, nogui=True, open="sounding.pd", cmd=None,
        path=["patches"], extra=None, stderr=False)
pd.Send(["Hello world"])
pd.Send(["Hello Rado"])
pd.Send(["dspOn"])
#pd.Send(["dspOff"])
#pd.Send(["dspOn"])
pd.Send(["load read sounds/moga.wav array1"])
pd.Send(["play1"])
pd.Send(["load read sounds/motorr.wav array2"])
pd.Send(["play2"])


while pd.Alive():
    data = pd.Update()

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
