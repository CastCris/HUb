r = [0,1]
c = 1
for i  in r:
    def cal():
        t = 0
        n = []
        os = []
        x = [1,2]
        e = 1
        o_dis = ["+", "-", "*", "/", "p", "="]
        for i in x:
            try:
                n.append(float(input("N: ")))
            except:
                print("Por favor, não confunda letras com números. É como confundir um facistinha com um comunista")
                erro = 2
                while(erro == 2):
                    try:
                        n.append(float(input("N: ")))
                    except:
                        print("Tente denovo")
                    else:
                        break
            os.append(str(input("O: ")))
            l = e-1
            if(os[l] != o_dis[0]) and (os[l]!=o_dis[1]) and (os[l]!=o_dis[2]) and (os[l]!=o_dis[3]) and (os[l]!=o_dis[5]):
                if(os[l] == "p") or (os[l] == "P"):
                    g = []
                    d = 0
                    for i in n:
                        g.append(n[d])
                        g.append(os[d])
                        d += 1
                    d = 0
                    g.pop()
                    for i in g:
                        print(g[d], end=" ")
                        d += 1
                    print("\n")
                else:
                    print("Por favor, não insira qualquer besteira. Tete denovo")
                erro = 1
                while(erro == 1):
                    os[l] = str(input("O: "))
                    if(os[l]==o_dis[0]) or (os[l]==o_dis[1]) or (os[l]==o_dis[2]) or (os[l]==o_dis[3]) or (os[l]==o_dis[5]):
                        break
                    else:
                        print("Tente novamente")
            #FInalização|O outro lado
            if(os[l] == "="):
                print("Final")
                os.pop()
                e = 0
                break
            else:
                x.append(len(x)+1)
            # print(n)
            e += 1
        for i in os:
            if(e<1):
                z = n[e]
            else:
                z = n[e+1]
            #Adição
            if(os[e] == "+"):
                if(e<1):
                    t = z+n[e+1]
                else:
                    t = t+z
            #Subtração
            elif(os[e] == "-"):
                if(e<1):
                    t = z-n[e+1]
                else:
                    t = t-z
            elif(os[e] == "*"):
                if(e>0):
                    if(os[e-1] == "+"):
                        t = (t-n[e])+(z*n[e])
                    elif(os[e-1] == "-"):
                        t = (t+n[e])-(z*n[e])
                    else:
                        t = t*z
                else:
                    t = z*n[e+1]
            else:
                if(e>0):
                    if(os[e-1] == "+"):
                        t = (t-n[e])+(n[e]/z)
                    elif(os[e-1] == "-"):
                        t = (t+n[e])-(n[e]/z)
                    elif(os[e-1] == "*"):
                        t = (t-(n[e]*n[e-1]))+(n[e-1]*(n[e]/z))
                    else:
                        t = t/z
                else:
                    t = z/n[e+1]
            e += 1
        print(t)
        return t
    try:
        cal()
    except ValueError:
        print("Por favor, coloque números, e não uma língua alienídena aos computadores!")
    except:
        print("O que você fez!!??")
    c += 1
    r.append(c)