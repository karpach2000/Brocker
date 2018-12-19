import numpy as np
import MySpaceFactory as SF
from MySpaceFactory import MySpaceFactory

L = np.array(range(20))
F = np.arctan(L)
#print(F)
msf = MySpaceFactory()
space = msf.generateSpace(L)
prognose = msf.getAbsolutePrognoze(space)
print("space:\n",space)
print("prognose:\n",prognose)