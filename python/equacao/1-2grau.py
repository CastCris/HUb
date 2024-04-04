print("Olá, bem-vindo a equação.com!","\n", "aqui, como você deve ter presumido, você poderá resolver as suas equações malucas!", "\n", "Qual tipo de equação você quer?")
def repetidor(r):
    while(r == 1):
        print("Nota: Digite 1 para 1º e 2 para 2º" ,"\n" ,"1º", "\n", "2º")
        ti = int(input(""))
        if(ti == 1):
            print("Digite a equação", "\n", "Nota: A equação deve ter o símbolo de igual e um valor após ele para dar certinho e, caso queira finalizar a conta, digite 'f' após colocar o simbolo e o valor de algum número no final")
            def numeros():
                rr = str("+")
                rr1 = str("+")
                re = "-"
                while(re == "-"):
                    while(rr == "+"):
                        n = float(input(""))
                        o = str(input(""))
                        n2 = float(input(""))
                        o2 = str(input(""))
                        if(o2 == "+") or (o2 == "-") or (o2 == "*") or (o2 == "/"):
                            rr == "-"
                            rr == "+"
                        elif(o2 == "=") or (o == "="):
                            rr= "-"
                            while(rr1 == "+"):
                                n1 = float(input(""))
                                o1 = str(input(""))
                                n12 = float(input(""))
                                o12 = str(input(""))
                                if(o12 == "+") or (o12 == "-") or (o12 == "*") or (o12 == "/"):
                                    rr1 == "-"
                                    rr1 == "+"
                                elif(o1 == "f") or (o12 == "f"):
                                    rr1 = "-"
                                    rr = "-"
                                    re = "+"
                                    print(o1, o12, re)
                                    if(rr1 == "-"):
                                        print("Uhhhh!!")
                def resoulcao():
                    x = int(0)
                    print(x)
                resoulcao()
            numeros()
repetidor(
    int(1)
)