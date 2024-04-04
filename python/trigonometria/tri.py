# lados do triângulo
print("Olá, bem_vindo a trigonomeria!", "\n", "aqui daremos algumas propriedas a seu triângulo, tais como: se ele é retângulo, seno, cosseno, tangente e valores dos ângulos!", "\n")
rr = 0
while(rr == 0):
    r = 0
    while(r == 0):
        print("Portanto, coloque os valores dos lados de seu triângulo", "\n", "Nota: os valores devem ser postivos")
        x = float(input(""))
        y = float(input(""))
        z = float(input(""))
        if(x<0) or (y<0) or (z<0):
            print("Por favor, não insira valores negativos", "\n")
            r = 1
        else:
            print("Primeiro olhamos se ele é retângulo, vamos conferir...")
            #Calculo da hipotenusa
            def h1(h, h2, h3):
                m = int(0)
                #x>
                if(x>y) and (x>z):
                    m = 1
                #y>
                elif(y>x) and (y>z):
                    m = 2
                #z>
                elif(z>x) and (z>y):
                    m = 3
                #Conferência
                if(x == h) and (m == 1)  or (y == h2) and (m == 2) or (z == h3) and (m == 3):
                    print("O triângulo é retângulo!")
                    if(m == 1):
                        print("O valor da hipotenusa é:", h, "e a dos catetos é", y, "e", z)
                    elif(m == 2):
                        print("O valor da hipotenusa é:", h2, "e a dos catetos é", x, "e", z)
                    elif(m == 3):
                        print("O valor da hipotenusa é:", h3, "e a dos catetos é", y, "e", x)
                elif(h == h2) and (h2 == h3) and (h == h3):
                    print("Equilátero")
                elif(h == h2) or (h2 == h3) or (h == h3):
                    print("Isógenes")
                else:
                    print("Um triângulo qualquer")
            h1( 
                (y**2 + z**2)**0.5, (x**2 + z**2)**0.5, (x**2 + y**2)**0.5
            )
            print("Agora veremos o valor dos ângulos de seu triângulo")
            def sct(vc1, vc2, vc3, vs1, vs2, vs3,):
                print("Os nomes dos ângulos serão:", "\n", 
                      "Alpha, entre os lados", x, "e", y, "\n", 
                      "Beta, entre os lados", y, "e ", z, "\n",
                        "Ômega, entre os lados:", x,"e", z)
                # print("O valor do ângulo e do cosseno de Alpha é", "\n", a,"º", "Sendo seu cosseno:", vc1)
                print("Cosseno Alpha", vc1)
                print("Cosseno Beta", vc2)
                print("Cosseno Ômega", vc3)
                print("Seno de Alpha")
            sct(
                #Seno
                x/z,
                y
                #valor do cosseno
                (x**2 + y**2 - z**2 )/(2*x*y),
                (z**2 + y**2 - x**2)/(2*z*y),
                (x**2 + z**2 - y**2)/(2*x*z),
                #ângulos
                #Alpha
            )
#180 = pi
#Valor de um ângulo através do radiano:
#(x*pi)/180 Xradianos