import time
t = [time.time()]
if __name__ == '__main__':
    while True:
        print("\n"," "*40,time.strftime("%H:%M do dia %d de %m de %Y", time.localtime()), "\n","O que procura?", "\n", "1- Cronômetro", "\n", "2- Temporizador","\n","3- Há quanto tempo...")
        txt = str(input())
        se = 0; s = []
        if txt == "1":
            t.append(time.time())
            print("Aparte enter para finalizar o cronometro ou digite 'p' para pausa-ló:")
            while True:
                if input("Contando ovelhas...") != "p":
                    for i in s:
                        se += i
                    print("\n",str(round(-t[len(t)-1]+time.time()-se, 2))+"s", "\n"); t.pop(); s.clear();break
                else: p = time.time();input("**Despausar**");s.append(time.time()-p); p = 0
            se = 0
        elif txt == "2":
            print("Defina um tempo(Y/M/D/h/m/s):", end=" ")
            t = input().split(); tt= []
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
                            if data[0] % 4 == 0: mex = 29
                            else: mex = 28
                        elif j == 5 or j == 7 or j == 8 or j == 10 or j == 12: mex = 31
                        elif j == 3 or j == 4 or j == 9 or j == 11: mex = 30
                        else: mex = 29
                        se += 60*24*mex
                    elif i == 2: se += 60*24#Dia
                    elif i ==3: se += 60#Hora
                    elif i == 4: se += 1#Minutos
                    elif i == 5: se += 1
                if tt[i]>0:
                    if i<5 : se *= 60
            t.append(se+time.time())
            while t[len(t)-1]>=time.time():
                # print(round(t[len(t)-1]-time.time(), 0), "\r")
        elif txt == "3":
            print("Coloque alguma data seguindo o modelo:", "\n", "Horas:Minutos Dia Mês e Ano", "\n", "Nota: deve-se colocar a enumeração do mês ao invés de seu nome", "\r")
            x = time.strptime(input(), "%H:%M %d %m %Y")
            print("\n","Então há...")
            data = time.localtime(); prin = []
            #
            prin.append(x[0]-data[0]);prin.append(x[1]-data[1]); prin.append(x[2]-data[2]); prin.append(x[3]-data[3]); prin.append(x[4]-data[4]); prin.reverse()
            print(prin)
            e = 0; va = 2
            if prin[4]<0: prin[4] *= -1
            for i in range(5):
                if x[i] != data[i]:
                    if x[i]>data[i]: at = 1
                    else: at = 0
                    break
            for i in prin:
                m = x[1]
                if m<0: m *= -1
                if m == 2:
                    if x[0] % 4 == 0: mex = 29
                    else: mex = 28
                elif m == 5 or m == 7 or m == 8 or m == 10 or m == 12: mex = 31
                elif m == 3 or m == 4 or m == 9 or m == 11: mex = 30
                else: mex = 29
                #
                if i<0 and at == 1:
                    if e == 0: prin[e] += 60; prin[e+1] -= 1
                    elif e == 1: prin[e] += 24; prin[e+1] -= 1
                    elif e == 2:
                        prin[e] += mex; prin[e+1] -= 1
                    elif e == 3:
                        prin[e] += 12; prin[e+1] -= 1
                #
                elif at == 0 and i>0:
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