
import math
from cellulare import Cellulare


telnuovo=Cellulare()
telnuovo.chiamata(10)
telnuovo.ricarica(20)
for i in range(5):
    telnuovo.chiamata(30)
    telnuovo.stato()