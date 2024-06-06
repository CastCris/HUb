import random
import os, os.path
import winsound
from os.path import dirname, abspath
class sound:
    def __init__(self, tipo, local) -> None:
        self.tipo = tipo
        self.local = local
        if self.tipo == '%a':
            som = {}; e = 0
            for i in os.listdir(self.local):
                if i.endswith('.wav'): som[e] = i; e += 1
            ran = random.randrange(0, e)
            d = dirname(dirname(abspath(__file__)))
            winsound.PlaySound(d+'\\'+self.local+'\\'+som[ran], winsound.SND_ALIAS)