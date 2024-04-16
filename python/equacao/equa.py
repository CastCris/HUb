print("Olá, bem-vindo a equação.py!","\n", "aqui, como você deve ter presumido, você poderá resolver as suas equações malucas! Além disso, você pode fazer outras coisas, tais como:", "\n", "Se o valor das expressões é verdadeiro ou utilzar como uma humilde calculadora", "\n")
r = 1
ola_nov = 0
while(r == 1):
    print("Digite a expressão", "\n", "Nota: esta calculadora é diferente das demais, não pela eficiencia e pela forma que ela calcula, e sim pela forma como ela organiza os calcúlos. Veja a seguir como ela funciona", "\n", "[operações|comandos] <proxima lnha> [número]", "\n", "\n","operações:", "\n", "+","\n" ,"Número", "\n","[Soma valores]", "\n", "\n", "-", "\n", "Número", "\n", "[Subtrai valores]", "\n", "\n", "[opção(+|-)]*", "\n","Número", "\n", "[Multiplica valores]","\n","*|+* --> (n1 . n2)", "\n", "-* --> -(n1.n2)", "\n", "\n", "[opção(+|-)]/", "\n", "Número","\n", "[Divide valores]","\n", "/|+/ --> (n1/n2)", "\n", "-/ --> -(n1/n2)", "\n")
    #valores de reinicialização
    re_conta = int(1)
    #valores para a conta
    z = float(0)
    e = 1
    contador = e
    #número
    n1 = 0
    #totais
    #Ativador
    ativador = int(0)
    tot1 = z
    while(re_conta == 1):
        conta = 1
        n_ant1 = float(0)
        while(conta == 1):
            #número
            #número de entrada
            if(e == 1):
                n1 = float(input(""))
            elif(e>1):
                n1 = n1
            #número de armazenamento
            n_ant1 = n1
            print("Valor total:" ,z)
            #operação
            def operar(o, n):
                #Valores
                #N antigo
                n_ant = float(0)
                #Marcador de ida
                def marcar():
                    if(o == "+"):
                        return 1
                    elif(o == "-"):
                        return 2
                    elif(o == "*"):
                        return 3
                    elif(o == "/"):
                        return 4
                if(e>1):
                    print(m)
                #Opções para desenvolvedor
                if(o == "z"):
                    print(z)
                #Operações
                if(o == "+") or (o == "-") or (o =="*") or (o == "/"):
                    if(e<2):
                        #Soma
                        if(o == "+"):
                            m = marcar()
                            return n_ant1 + n
                        #Subtração
                        elif(o == "-"):
                            return n_ant1 - n
                        #multiplicação
                        #positiva
                        elif(o == "*"):
                            return n * n_ant1
                    elif(e>=2):
                        #Soma
                        if(o == "+"):
                            while(n_ant == 0):
                                n_ant = n
                                if(n_ant != 0):
                                    return n_ant + z
                        #Subtração
                        if(o == "-"):
                            while(n_ant == 0):
                                n_ant = n
                                if(n_ant != 0):
                                    return z - n_ant
                        #Multiplicaçãp
                        if(o == "*"):
                            if(o_ant == "+") or (o_ant == "-") and (e == 2):
                                n_ant = 0
                                if(o_ant == "+"):
                                    while(n_ant == 0):
                                        n_ant = n
                                        print("1")
                                        if(n_ant != 0):
                                            o_ant = "*"
                                            return (z-n_ant1) + (n_ant1*n_ant)
                                elif(o_ant == "-"):
                                    while(n_ant == 0):
                                        n_ant = n
                                        if(n_ant != 0):
                                            return (z+n_ant1) - (n_ant1*n_ant)
                                elif(o_ant == "*"):
                                    while(n_ant == 0):
                                        n_ant = n
                                        print(n_ant)
                                        if(n_ant != 0):
                                            return z*n_ant
                else:
                    return armazenador_cons
            z = operar(str(input("")) ,float(input("")))
            #O antigo
            def operar_antigo(o_ant):
                if(m == 1):
                    return "+"
                elif(m == 2):
                    return "-"
                elif(m == 3):
                    return "*"
                elif(m == 4):
                    return "/"
            o_ant = operar_antigo(str())
            print(o_ant)
            if(e>1):
                print(o_ant)
            armazenador_cons = z
            contador = e-1
            e = e+1
        tot1 = z + tot1
    if(final == 1):
        print("Obrigado por utilizar a calculadora maluca!", "\n", "O resultado de sua expressão foi:", z,"\n", "Caso queira fazer outra continha digite 'r'")
        o = str(input(""))
        if(o == "r"):
            re_conta = 1