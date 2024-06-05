import random
import os, os.path
import winsound
class sound:
    def __init__(self, tipo) -> None:
        self.tipo = tipo
        if self.tipo == '%a':
            som = {}; e = 0
            for i in os.listdir():
                if i.endswith('.wav'): som[e] = i; e += 1
            ran = random.randrange(0, e)
            winsound.PlaySound(som[ran], winsound.SND_FILENAME)
sound('%a')