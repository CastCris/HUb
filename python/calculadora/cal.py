r = [0,1]
c = 1
for i  in r:
    def cal():
        t = 1
        t_t = 0
        t_m = 0
        n = []
        os = []
        x = [1,2]
        e = 1
        o_dis = ["+", "-", "*", "/", "p", "="]
        est = 1
        m_contador = -1
        m_e = 1
        m_s = 0
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
            #Z
            if(e<1):
                z = n[e]
            else:
                z = n[e+1]
            #Estado
            if((e+1)<=len(os)-1):
                if(os[e] == "+" or os[e] == "-") and (os[e+1] != "*" and os[e+1] != "/"):
                    est = 1
                    m = 2
                elif(os[e+1] == "*" or os[e+1] == "/"):
                    est = 2 
                    m = 1
                elif(e == 0):
                    est = 2
                    t = n[e+1]
                    m = 1
            else:
                if(os[e] == "+" or os[e]== "-"):
                    est = 1
                    m = 2
                else:
                    est = 2
                    m = 1
            #Adição
            if(os[e] == "+"):
                if(est == 1):
                    if(e<1):
                        t = z+n[e+1]
                    else:
                        t = z
            #Subtração
            elif(os[e] == "-"):
                if(est == 1):
                    if(e<1):
                        t = z-n[e+1]
                    else:
                        t = -z
                else:
                    t = n[e+1]*(-1)
            #Multiplicação
            elif(os[e] == "*"):
                if(e+1<=len(os)-1):
                    if(os[e+1] != "*" and "/"):
                        if(m_e<=1):
                            t = t*z
                        else:
                            if(m_s == 0):
                                t = n[m_contador]+(t*z)
                            else:
                                t = t*z
                        m_contador = -1
                    else:
                        if(e>0):
                            t = t*z
                        else:
                            t = z*n[e+1]
                else:
                    if(e>0):
                        t = n[m_contador]+(t*z)
                    else:
                        t = n[e+1]*z
                        est = 1
                    t_m = 0
            #Divisão
            elif(os[e] == "/"):
                if(e>0):
                    if(os[e-1] == "+"):
                        t = (t-n[e-1])+(n[e]/z)
                    elif(os[e-1] == "-"):
                        t = (t+n[e-1])-(n[e]/z)
                    elif(os[e-1] == "*"):
                        if(os[e-2] != "*") and (os[e-2] != "/"):
                            if(t<0):
                                if(os[e-2] == "+"):
                                    t = ((t+(n[e]*n[e-1]))+(n[e-1]*(n[e]/z)))
                                else:
                                    t = ((t+(n[e]*n[e-1]))-(n[e-1]*(n[e]/z)))
                            else:
                                if(os[e-2] == "+"):
                                    t = ((t-(n*(n[e-1]))))+(n[e-1]*(n[e]/z))
                                else:
                                    t = ((t-(n*(n[e-1]))))-(n[e-1]*(n[e]/z))
                        else:
                            t = (t+(n[e]*n[e-1]*n[e-2]))+(n[e-2]*(n[e-1]*(n[e]/z)))
                    else:
                        t = t/z
                else:
                    t = z/n[e+1]
            e += 1
            #Regulador
            #ESt1
            if(est == 1):
                t_t = t+t_t+t_m
                if(t == 1 and e==0):
                    t = 0
                else:
                    t = 0
                t_m = 0
                if(e<=len(os)-1):
                    if(os[e] != "+" or "-") and (m == 1):
                        if(os[e-1] == "-") and (os[e+2] == "*" or "/"):
                            t = -n[e+1]
                        elif(os[e+2] == "*" or "/"):
                            t = n[e+1]
                        else:
                            m_s = 2
                        m_e = 0
            #EST2
            elif(est == 2):
                t_m = t
                m_e += 1
                if(m_contador == -1):
                    if(e+2<=len(os)-2):
                        if(os[e+2] == "*" or "/") and (os[e-1] != "*" and os[e-1] != "/"):
                            m_contador = e-1
                            t = n[e]
                        else:
                            m_s = 1
                            t = n[e+1]
                    else:
                        m_contador = e-1
                    m_e == 0
                if(e+1<=len(os)-1):
                    if(os[e+1] != "*" or "/") and (m == 2):
                        t = 0
                        m = 0
                        m_contador = -1
                if(e == len(os)):
                    t_t = t_m
                elif(os[e] == "+" or os[e] == "-"):
                    t_t = t_t+t_m
        print(t_t)
        return t
    try:
        cal()
    except ValueError:  
        print("Por favor, coloque números, e não uma língua alienídena aos computadores!")
    except:
        print("O que você fez!!??")
    c += 1
    r.append(c)