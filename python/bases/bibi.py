import sys
import winsound
from tkinter import *
from tkinter import ttk
#
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d+'\\tp\\')
from tempo import *
#
class bibi():
    def __init__(self, number, index,ty) -> None:
        self.number = number;self.ty = ty; self.index = index
        #
        self.bi()
    def bi(self):
        x = 0
        alfa = {x:'A', x+1:'B',x+2:'C', x+3:'D', x+4:'E', x+5:'F', x+6:'G', x+7:'H', x+8:'I', x+9:'J', x+10:'K', x+11:'L', x+12:'M', x+13:'N', x+14:'O', x+15:'P', x+16:'Q', x+17:'R', x+18:'S', x+19:'T', x+20:'U', x+21:'V', x+22:'W', x+23:'X', x+24:'Y', x+25:'Z'}
        n = self.number; ind = self.index
        if self.ty == 'c':
            lis_n = [[],[]]; alfa_i = 1
            while True:
                n = n/ind
                if n - int(n) == 0: lis_n[1].append(0)
                else: 
                    if int(n*ind - int(n)*ind)<10:
                        lis_n[1].append(int(n*ind - int(n)*ind)); n = int(n)
                    else:
                        while True:
                            for j in alfa.keys():
                                if j+10 == int(n*ind - int(n)*ind): lis_n[1].append(alfa[j]); break
                            if j+10 == int(n*ind - int(n)*ind): break
                            else: 
                                x += 10
                                alfa = {x:'A', x+1:'B',x+2:'C', x+3:'D', x+4:'E', x+5:'F', x+6:'G', x+7:'H', x+8:'I', x+9:'J', x+10:'K', x+11:'L', x+12:'M', x+13:'N', x+14:'O', x+15:'P', x+16:'Q', x+17:'R', x+18:'S', x+19:'T', x+20:'U', x+21:'V', x+22:'W', x+23:'X', x+24:'Y', x+25:'Z'}
                                for j in alfa.keys():
                                    alfa[j] += str(alfa_i)
                                alfa_i += 1
                if n<1: break
            if self.number - int(self.number) != 0:
                n = self.number - int(self.number)
                while True:
                    n *= ind
                    lis_n[0].append(int(n))
                    if (n - int(n))*ind == 0: break
                    n = n - int(n)
            lis_n[1].reverse();lis_n.reverse()
        elif self.ty == 'd':
            lis_n = [list(str(self.number)), 0]; lis_n[0].reverse()
            v = 1
            for i in lis_n[0]:
                i = int(i)
                if i>ind-1: print('Por favor, não coloque um número maior que a base'); break
                elif i != 0: lis_n[1] += i*v
                v *= ind
        print(lis_n)
bibi(10,16,'c')