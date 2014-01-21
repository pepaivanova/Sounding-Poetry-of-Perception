from time import time
from pd import Pd

start = time()
# start pd
pd = Pd(port=3010, nogui=False, open="sounding.pd", cmd=None,
        path=["patches"], extra=None, stderr=False)
pd.Send(["Hello world"])
pd.Send(["Hello Rado"])

while pd.Alive():
    pd.Update()

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
