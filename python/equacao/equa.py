print("Olá, bem-vindo a equação.py!","\n", "aqui, como você deve ter presumido, você poderá resolver as suas equações malucas! Além disso, você pode fazer outras coisas, tais como:", "\n", "Se o valor das expressões é verdadeiro ou utilzar como uma humilde calculadora", "\n")
r = 1
ola_nov = 0
while(r == 1):
    print("Digite a expressão", "\n", "Nota: esta calculadora é diferente das demais, não pela eficiencia e pela forma que ela calcula, e sim pela forma como ela organiza os calcúlos. Veja a seguir como ela funciona", "\n", "[operações|comandos] <proxima lnha> [número]", "\n", "\n","operações:", "\n", "+","\n" ,"Número", "\n","[Soma valores]", "\n", "\n", "-", "\n", "Número", "\n", "[Subtrai valores]", "\n", "\n", "[opção(+|-)]*", "\n","Número", "\n", "[Multiplica valores]","\n","*|+* --> (n1 . n2)", "\n", "-* --> -(n1.n2)", "\n", "\n", "[opção(+|-)]/", "\n", "Número","\n", "[Divide valores]","\n", "/|+/ --> (n1/n2)", "\n", "-/ --> -(n1/n2)", "\n")
    #valores de reinicialização
    re_conta = int(1)
    #valores para a conta
    ze = float(0)
    e = 1
    contador = e
    #número
    n1 = 0
    #totais
    totz = float(0)
    tot1 = float(0)
    #Ciclo
    final_ciclo = 0
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
            print("Valor total:", ze)
            #operação
            def operar(z):
                #Ignição
                while(e<2):
                    o = str(input(""))
                    n = float(input(""))
                #Operações
                    if(o == "+") or (o == "-") or (o =="*") or (o == "/"):
                        #Soma
                        if(o == "+"):
                            return n_ant1 + n
                        #Subtração
                        elif(o == "-"):
                            return n_ant1 - n
                        #multiplicação
                        #positiva
                        elif(o == "*"):
                            return n * n_ant1
                    else:
                        return
                while(e>=2):
                    ciclo = 1
                    o = str(input(""))
                    if(o != "*"):
                        n = float(input(""))                    
                        if(n != None):
                            n_ant = n
                            o_ant = o
                    else:
                        o_ant = "*"
                    print("Op. ant:", o_ant)
                    if(o == "+") or (o == "-") or (o == "*") or (o == "/"):
                        #Soma
                        if(o == "+"):
                            n_ant = n
                            return n_ant + z
                        #Subtração
                        elif(o == "-"):
                            n_ant = n
                            return z - n_ant
                        elif(o == "*"):
                            if(o_ant == "*"):
                                n = float(input(""))
                                return ze*n
                            else:
                                print("FOI!!")
                    else:
                        return 
            ze = operar(float())
            e = e+1
        totz = ze+totz
    if(final == 1):
        print("Obrigado por utilizar a calculadora maluca!", "\n", "O resultado de sua expressão foi:", z,"\n", "Caso queira fazer outra continha digite 'r'")
        o = str(input(""))
        if(o == "r"):
            re_conta = 1