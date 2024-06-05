import time
import winsound
t = [time.time()]; at = 0
if __name__ == '__main__':
    while True:
        try:
            if at == 0:
                print("\n"," "*40,time.strftime("%H:%M do dia %d de %m de %Y", time.localtime()), "\nO que procura?\n1- Cronômetro\n2- Temporizador\n3- Há quanto tempo..."); txt = None
                txt = str(input())
                se = 0; s = []; mex = 31; at = 0; dila = 0
            if txt == "1" or at == 1:
                if at == 0:
                    t.append(time.time()); prin = [0,0,0,0,0,0]; va = 0; tt = time.time()-t[len(t)-1]
                    print("Caso queira para-ló, aperte ctrl+C:")
                while True:
                    if (time.time()-int(t[len(t)-1])-dila)>tt+va:
                        if prin[0]>59:
                            for i in range(6):
                                if i>0 and i<5 and prin[1]>59 or prin[2]>59 or prin[3]>mex or prin[4]>11 or prin[0]>59:
                                    if i == 1 and prin[i]<60: prin[i] += 1; prin[i-1] -= 60
                                    elif i ==2 and prin[i]<24: prin[i] += 1; prin[i-1] -= 60
                                    elif i == 3 and prin[i]<mex: prin[i] += 1; prin[i-1] -= mex
                                    elif i == 4 and prin[i]>12: prin[4] -= 12; prin[5] += 1
                        prin.reverse()
                        for i in range(6):
                            if i<5: print(prin[i], end="/")
                            else: print(prin[i])
                        prin.reverse()
                        prin[0] += 1;va += 1
            elif txt == "2" or at == 2:
                if at == 0:
                    print("Defina um tempo(Y/M/D/h/m/s). Nota: Para pausa-ló aperte ctrl+C:", end=" ")
                    try: t = input().split(); tt= []
                    except: print("Como assim deu erro?")
                    for i in range(len(t)):
                        try: tt.append(int(t[i]))
                        except: i = i
                        if len(tt)>5: break
                    print(tt)
                    for i in range(6):
                        for j in range(tt[i]):
                            if i == 0:#Ano
                                if j%4 == 0: se+= 60*24*366
                                else: se+= 60*24*366
                            elif i == 1:#Mês
                                if j == 2:
                                    if tt[0] % 4 == 0: mex = 29
                                    else: mex = 28
                                elif j == 5 or j == 7 or j == 8 or j == 10 or j == 12: mex = 31
                                elif j == 3 or j == 4 or j == 9 or j == 11 or j == 6: mex = 30
                                else: mex = 31
                                se += 60*24*mex
                            elif i == 2: se += 60*24#Dia
                            elif i ==3: se += 60#Hora
                            elif i == 4: se += 1#Minutos
                            elif i == 5: break
                        if tt[i]>0:
                            if i<5 : se *= 60
                    se += tt[5]
                    t.append(se+time.time()); tt.reverse(); prin = []
                    for i in range(len(tt)):
                        if i<2 and tt[i]>59: tt[i+1] += 1*(tt[i]//60);tt[i] -= 60*(tt[i]//60)
                        elif i == 2 and tt[i]>23:tt[i+1] += 1*(tt[i]//24); tt[i] -= 24*(tt[i]//24)
                        elif i == 3 and tt[i]>mex:
                            j = tt[i+1]
                            while tt[i]>mex:
                                if j == 2:
                                    if tt[5] % 4 == 0: mex = 29
                                    else: mex = 28
                                elif j == 5 or j == 7 or j == 8 or j == 10 or j == 12 or j == 1: mex = 31
                                elif j == 3 or j == 4 or j == 9 or j == 11 or j == 6: mex = 30
                                else: mex = 31
                                j += 1
                                tt[i] -= mex; tt[i+1] += 1
                        elif i == 4 and tt[i]>11: tt[i+1] += 1*(tt[i]//11);tt[i] -= 12*(tt[i]//11)
                    va = (t[len(t)-1]-time.time()); tt.reverse();prin = tt
                #
                while t[len(t)-1]>=time.time()-dila-1:
                    if (time.time()-dila)>t[len(t)-1]-va:
                        if prin[5]<0:
                            for i in range(len(prin)):
                                if i<5:
                                    if prin[i+1]<=0 and prin[i]>0:
                                        if i == 0: prin[i+1] += 12
                                        elif i == 1:
                                            j = tt[i]
                                            if j == 2:
                                                if tt[0] % 4 == 0: mex = 29
                                                else: mex = 28
                                            elif j == 5 or j == 7 or j == 8 or j == 10 or j == 12 or j == 1: mex = 31
                                            elif j == 3 or j == 4 or j == 9 or j == 11 or j == 6: mex = 30
                                            else: mex = 31
                                            prin[i+1] += mex
                                        elif i == 2: prin[i+1] += 24
                                        elif i>2: prin[i+1] += 60
                                        prin[i] -= 1
                        for i in range(len(prin)):
                            if i<5: print(prin[i], end="/")
                            else: print(prin[i])
                        va -= 1; prin[5] -= 1
                winsound.PlaySound('plin.wav',winsound.SND_FILENAME)
            elif txt == "3":
                print("Coloque alguma data seguindo o modelo:\nHoras:Minutos Dia Mês e Ano\nNota: deve-se colocar a enumeração do mês ao invés de seu nome e não coloque um 1000>ano>9000\r")
                try:x = time.strptime(input(), "%H:%M %d %m %Y")
                except: print("Uai, não sabe mais colocar data ou ler?")
                print("\n","Então há...")
                data = time.localtime(); prin = []
                #
                prin.append(x[0]-data[0]);prin.append(x[1]-data[1]); prin.append(x[2]-data[2]); prin.append(x[3]-data[3]); prin.append(x[4]-data[4]); prin.reverse()
                e = 0; va = 2
                if prin[4]<0: prin[4] *= -1
                for i in range(5):
                    if x[i] != data[i]:
                        if x[i]>data[i]: ati = 1
                        else: ati = 0
                        break
                for i in prin:
                    m = x[1]
                    if m<0: m *= -1
                    if m == 2:
                        if x[0] % 4 == 0: mex = 29
                        else: mex = 28
                    elif m == 5 or m == 7 or m == 8 or m == 10 or m == 12 or m == 1: mex = 31
                    elif m == 3 or m == 4 or m == 9 or m == 11 or m == 6: mex = 30
                    else: mex = 31
                    #
                    if i<0 and ati == 1:
                        if e == 0: prin[e] += 60; prin[e+1] -= 1
                        elif e == 1: prin[e] += 24; prin[e+1] -= 1
                        elif e == 2:
                            prin[e] += mex; prin[e+1] -= 1
                        elif e == 3:
                            prin[e] += 12; prin[e+1] -= 1
                    #
                    elif ati == 0 and i>0:
                        if e == 0: prin[e] -= 60#Minutos
                        elif e == 1:prin[e] -= 24#Hora
                        elif e == 2: prin[e] -= mex#DIas
                        elif e == 3: prin[e] -= 12#Meses,[4]?
                        #
                        de = []
                        if prin[1] == 0: dia = 23
                        else: dia = 24
                        for j in range(len(prin)): 
                            if prin[j]<0: prin[j] *= -1; de.append(j)
                        if prin[1] != 0 and prin[1] != 1 and e<1: prin[1] -= 1
                        elif prin[2] != 0 and prin[2] != 1 and e<2: prin[1] -= dia;prin[2] -= 1
                        elif prin[3] != 0 and prin[3] != 1 and e<3: 
                            if e<1: prin[1] -= dia; 
                            if e<2: prin[2] -= mex-1
                            if e<3:prin[3] -= 1
                        elif prin[4] != 0:
                            if e<1:prin[1] -= dia
                            if e<2: prin[2] -= mex-1
                            if e<3: prin[3] -= 11
                            if e<4: prin[4] -= 1
                            break
                        for j in de: prin[j] *= -1
                    if e>0 and va>0: va -= 1
                    e += 1
                for i in range(len(prin)): 
                    if prin[i]<0: prin[i] *= -1
                prin.reverse()
                for i in range(len(prin)):
                    res = str(prin[i])+" ";v = prin[i]
                    if i == 0:
                        if v<2: res += "Ano"
                        else: res += "Anos"
                    elif i == 1:
                        if v<2: res += "Mês"
                        else: res += "Meses"
                    elif i == 2:
                        if v<2: res += "Dia"
                        else: res += "Dias"
                    elif i == 3:
                        if v<2: res += "Hora"
                        else: res += "Horas"
                    elif i == 4:
                        if v<2: res += "Minuto"
                        else: res += "Minutos"
                    print(res)
                try:
                    if at== 0: print("Atrás foi", end=" ")
                    else: print("A partir de agora será", end=" ")
                    print("a data", time.strftime("%H:%M/%d/%m/%Y", x))
                except:
                    print("É agorita mesmo!")
            else: print("Inválido")
            at = 0
        except KeyboardInterrupt: 
            if txt == "1" or txt == "2":
                t1 = time.time()
                if input("Continuar a contagem?[S/N] ") == "s": 
                    if txt == "1": at = 1
                    elif txt =="2": at = 2
                    dila += time.time()-t1
                else: at = 0
            else: input("Por quê quer sair? "); break
def time_init():global temp ; temp = time.time()
def time_end(): print(str(round(time.time()-temp, 2))+'s'); return 0
# import sys
# from os.path import dirname, abspath
# d = dirname(dirname(abspath(__file__)))
# sys.path.append(d+'\\tp\\')
# from tempo import *
# """"
# time_end()