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
    time_init()
    def __init__(self, number:'numero', index:'base1',index_2:'base2') -> 'Conversão':
        self.number = number; self.index = index; self.index_2 = index_2
        #
        self.bi()
    def bi(self):
        alfa = {10:'A', 11:'B',12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M',23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
        alfa_ar = []; alfa_i = 1
        n = self.number; ind = [self.index, self.index_2]
        alfa_ar = [alfa]; lis_n = [[],[]]
        if ind[0]>26:
            alfa_ar.append({});letra = alfa.values(); e = 1; c = 36
            while True:
                for i in letra:
                    if c-26<ind[0]-26: alfa_ar[e][c] = i +'-'+str(alfa_i)
                    c += 1
                if c+10>ind[0]-26: break
                e += 1; alfa_ar.append({})
                alfa_i += 1
        # print(alfa_ar)
        #Conversão 1
        lis_str = list(str(self.number)); e = [0,0]; cont = [0,0]; va = [0,1]; m = 0
        for i in alfa_ar[len(alfa_ar)-1].values(): va[0]= i
        va[0] = alfa_i; ponte = ''
        while va[0]>10: va[0]/= 10; va[1] += 1
        for i in lis_str:
            if cont[0]>0: cont[0]-= 1
            else: ponte = ''
            if i == '-' or cont[0]>0:
                if i == '-': ponte += lis_str[e[0]-1] + lis_str[e[0]]; lis_n[m].pop(e[1]);cont[0] = va[1]+1
                elif i != '0':ponte += lis_str[e[0]]
            elif i == '.':m = 1; 
            else: lis_n[m].append(i)
            if cont[0] == 1: lis_n[m].append(ponte)
            e[0] += 1; e[1] = len(lis_n[m])-1
        # print(lis_n, '1')
        lis_n[0].reverse()
        n = 0
        for i in range(len(lis_n)):
            if i == 0: v = 1
            else: v = 0.1
            for j in lis_n[i]:
                try: j = int(j)
                except:
                    for k in alfa_ar:
                        for l,m in k.items():
                            if m == j: j = l; break
                        if j == l: break
                if j>ind[0]-1: print('Por favor, não coloque um número maior que a base'); break
                elif j != 0: n += j*v
                #
                if i == 0: v *= ind[0]
                else: v /= ind[0]
        e = 0
        # print(n, '2')
        #Conversão 2
        lis_n = [[int(n)], [n - int(n)]]
        if lis_n[0] != 0:
            n = lis_n[0][0]
            while True:
                n/=ind[1]
                if n - int(n) == 0: lis_n[0].append(0)
                else: 
                    if int(n*ind[1] - int(n)*ind[1])<10: lis_n[0].append(int(n*ind[1] - int(n)*ind[1]))
                    else:
                        for i in alfa_ar:
                            for j in i.keys():
                                if j == int(n*ind[1] - int(n)*ind[1]): lis_n[0].append(i[j])
                            if j == int(n*ind[1] - int(n)*ind[1]): break
                if n<1: break
        #2
        if lis_n[1] != 0:
            n = lis_n[1][0]
            while True:
                n *= ind[1]
                if int(n)<10:
                    lis_n[1].append(int(n))
                else:
                    for i in alfa_ar:
                        for j in i.keys():
                            if j == int(n): lis_n[1].append(i[j]); break
                        if j == int(n): break
                if (n - int(n))*ind[1] == 0: break
                n = n - int(n)
        # print(lis_n)
        lis_n[1].pop(0); lis_n[0].pop(0);lis_n[0].reverse()
        for i in range(len(lis_n)): 
            if i>0: print('.', end='')
            for j in lis_n[i]: print(j, end='')
        print('\r')
        time_end()
bibi('1.5',10,2)