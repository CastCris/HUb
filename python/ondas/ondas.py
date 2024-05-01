#Modos
modo_ds = 1#modo desenvolvedor
#Renicialização
reniciar = 0
#Valores para as ondas
proporcao = 1
#Ciclo
section_ciclo = 1
ciclo_1_1 = 1
ciclo_1_2 = 0
ciclo_1_3 = 0
ciclo_1_4 = 0
ciclo_1_5 = 0
ciclo_1_6 = 0
#Repetidores
#Ciclo
repet_ciclo_1_1 = 1
repet_ciclo_1_2 = 0
repet_ciclo_1_3 = 0
repet_ciclo_1_4 = 0
repet_ciclo_1_5 = 0
repet_ciclo_1_6 = 0
#Seções
repet_sectio_1 = 2
#Removedor
remover_1 = 0
repetidor = 0
repetidor_se = 0
depois = 1
ciclo = 0
ciclo_des = repet_ciclo_1_1+repet_ciclo_1_2+repet_ciclo_1_3+repet_ciclo_1_4+repet_ciclo_1_5+repet_ciclo_1_6
#Seção 1
#Quantidade desejada
quant_dej_dir_1_1 = 40
quant_dej_dir_1_2 = 0
quant_dej_dir_1_3 = 0
quant_dej_dir_1_4 = 0
quant_dej_dir_1_5 = 0
quant_dej_dir_1_6 = 0
#Largura
#Prohressiva
rigth_armazenada_1_1 = 40
rigth_armazenada_1_2 = 0
rigth_armazenada_1_3 = 0
rigth_armazenada_1_4 = 0
rigth_armazenada_1_5 = 0
rigth_armazenada_1_6 = 0
#Inicial
r_init_armazenada_1_1 = 1
r_init_armazenada_1_2 = 0
r_init_armazenada_1_3 = 0
r_init_armazenada_1_4 = 0
r_init_armazenada_1_5 = 0
r_init_armazenada_1_6 = 0
#Proporcional|Não porporcional
r_init_pro_ro = 1
#Espaçamento
esp_des_1_1 = 2
esp_des_1_2 = 0
esp_des_1_3 = 0
esp_des_1_4 = 0
esp_des_1_5 = 0
esp_des_1_6 = 0
#Fator 1
fator1_1_1 = 10
fator1_1_2 = 0
fator1_1_3 = 0
fator1_1_4 = 0
fator1_1_5 = 0
fator1_1_6 = 0
#Fator 2
fator2_1_1 = 10
fator2_1_2 = 0
fator2_1_3 = 0
fator2_1_4 = 0
fator2_1_5 = 0
fator2_1_6 = 0
#Suavidade
sua_1_1 = 1
sua_1_2 = 1
sua_1_3 = 0
sua_1_4 = 0
sua_1_5 = 0
sua_1_6 = 0
#Tipos
onda_1_1_t = 1
onda_1_2_t = 1
onda_1_3_t = 1
onda_1_4_t = 1
onda_1_5_t = 1
onda_1_6_t = 1
#Quantidade de tipos
quant_tipo = 5
#4Tipos:
#1- Multiplicar
#2- Dividir
#3- Somar
#4- Subtrair
#Número
fator1 = int(10)# número desejado a ser multiplicado
fator2 = int(10)# número desejado a ser multiplicado pelo fator1_di
n_di = int(10)# número divisor
armazenador_x = int(1)#Armazenador do x
n_flutuante = int(0)
n_flutuante_exibir = n_flutuante
#Quantidade
quant = int(1)
#Quantidade desejada
#Largura
quant_dej_dir = int(1)#direita
#Total
quant_dej = quant_dej_dir
#Direita
rigth = int(1)#direita marcadora
rigth_desj = int(1)#direita desejada
#Espaçamento
esp = int(1)
esp_des = int(1)
contagem_esp = int(0)#contagem esp
contagem_esp_armazenamento = int(0)
#Suava|Robusto
pro_ro = 1#geral
pro_ro_exibir = pro_ro
#lados
pro_ro_es = 0#esquerdo
pro_ro_es_exibir = pro_ro_es
pro_ro_di = 0#direito
pro_ro_di_exibir = pro_ro_di
#Outros
#Incializadores
onda = 1
ativador = 0
#Config
entra = 0
#Texto
text = 1
#Mais não!
vezes = 0
#Configurações
exibir_instrucoes = 1
configuracoes = 0
selecionar_tipo = None
estado_config = 1
while (reniciar != 1):
    #Repetidor
    while(onda == 1):
        #Renicializanodres importantes. Não mexa!!!!
        configuracoes = 0
        repetidor_se = 0
        depois = 1
        t_atual = 1
        #Texto
        while(text == 1):
            #Início
            if(vezes<1):
                print("Olá, bem_vindo ao ondinhas.com!","\n" ,"Aqui você pode, como deve ter presumido,fazer  ondinhas dos mais variáveis jeitos, deste de suaves á ondas ígrimes ou, até, verdadeiras tempestades, além de poder personalisa-lás.", "\n", "Caso queira ver o projeto de uma vez, apenas pressione c no termianal! Porém, caso queria mudar alguma das  configurações das ondas, sinta-se a vontade para fazer isso. Apenas digite config e faça as suas mudanças")
            elif(vezes != 0):
                if(vezes<2):
                    print("Gostou do programinnhas? Não importa, para ser franco contigo, não tem como  enviar feedback XD, por enquanto...", "\n", "Entretanto, como toda via, você pode repetir quantas vezes quiser, apenas digite 'C' logo abixo e, claro, se quiser fazer alguma mudança, digite confing")
            comecar = str(input(""))
            if(comecar == "config"):
                configuracoes = 1
                text = 0
            elif(comecar == "c") or (comecar == "C"):
                text = 0
            else:
                print("Inválido, tente novamente")
        while(configuracoes == 1):
            if(exibir_instrucoes == 1):
                print("")
                exibir_instrucoes = 0
            #Confiurações
            print("Digite a configuração desejada")
            ciclo_1_1 = 2
            entra = 0
            while(configuracoes == 1):
                #Ciclo
                ciclo_des = 0
                #Dados atuais
                #Onda atual
                def onda_atual(atual):
                    if(ciclo_1_1 == 2):
                        return 1
                    elif(ciclo_1_2 == 2):
                        return 2
                    elif(ciclo_1_3 == 2):
                        return 3
                    elif(ciclo_1_4 == 2):
                        return 4
                    elif(ciclo_1_5 == 2):
                        return 5
                    elif(ciclo_1_6 == 2):
                        return 6
                o_atual = onda_atual(int())
                def tipo_atual(t_atual):
                    if(section_ciclo == 1):
                        #1
                        if(ciclo_1_1 == 2):
                            if(onda_1_1_t == 1):
                                return 1
                            elif(onda_1_1_t == 2):
                                return 2
                        #2
                        elif(ciclo_1_2 == 2):
                            if(onda_1_2_t == 1):
                                return 1
                            elif(onda_1_2_t == 2):
                                return 2
                        #3
                        elif(ciclo_1_3 == 2):
                            if(onda_1_3_t == 1):
                                return 1
                            elif(onda_1_3_t == 2):
                                return 2
                        #4
                        elif(ciclo_1_4 == 2):
                            if(onda_1_4_t == 1):
                                return 1
                            elif(onda_1_4_t == 2):
                                return 2
                        #5
                        elif(ciclo_1_5 == 2):
                            if(onda_1_5_t == 1):
                                return 1
                            elif(onda_1_5_t == 2):
                                return 2
                        #6
                        elif(ciclo_1_6 == 2):
                            if(onda_1_6_t == 1):
                                return 1
                            elif(onda_1_6_t == 2):
                                return 2
                t_atual = tipo_atual(int())
                if(t_atual == None):
                    print("Modelo de onda inválido, altere-a para não ocorre erros")
                    if(ciclo_1_1 == 2):
                        onda_1_1_t = 1
                    elif(ciclo_1_2 == 2):
                        onda_1_2_t = 1
                    elif(ciclo_1_3 == 2):
                        onda_1_3_t = 1
                    elif(ciclo_1_4 == 2):
                        onda_1_4_t = 1
                    elif(ciclo_1_5 == 2):
                        onda_1_5_t = 1
                    elif(ciclo_1_6 == 2):
                        onda_1_6_t = 1
                if(entra == 0):
                    print("Seção", section_ciclo, "Onda:", o_atual,)                
                #Comecar
                if(estado_config == 1):
                    comecar = str(input("~ "))
                    #Define onda
                    #Seção
                    if(comecar == "st") or (comecar == "St") or (comecar == "sT"):
                        print("Escolha uma seção padrão para as suas ondas:")
                        estado_config = 2
                    elif(comecar == "str") or (comecar == "Str"):
                        print("Repetidor da Seção", section_ciclo)
                        if(section_ciclo == 1):
                            repet_sectio_1 = int(input())
                    #Onda
                    #Adicionar e configurar
                    #1
                    elif(comecar == "o1"):
                        if(section_ciclo == 1):
                            ciclo_1_1 = 2
                            ciclo_1_2 = 0
                            ciclo_1_3 = 0
                            ciclo_1_4 = 0
                            ciclo_1_5 = 0
                            ciclo_1_6 = 0
                    #2
                    elif(comecar == "o2"):
                        if(section_ciclo == 1):
                            ciclo_1_1 = 0
                            ciclo_1_2 = 2
                            ciclo_1_3 = 0
                            ciclo_1_4 = 0
                            ciclo_1_5 = 0
                            ciclo_1_6 = 0
                    #3
                    elif(comecar == "o3"):
                        if(section_ciclo == 1):
                            ciclo_1_1 = 0
                            ciclo_1_2 = 0
                            ciclo_1_3 = 2
                            ciclo_1_4 = 0
                            ciclo_1_5 = 0
                            ciclo_1_6 = 0
                    #4
                    elif(comecar == "o4"):
                        if(section_ciclo == 1):
                            ciclo_1_1 = 0
                            ciclo_1_2 = 0
                            ciclo_1_3 = 0
                            ciclo_1_4 = 2
                            ciclo_1_5 = 0
                            ciclo_1_6 = 0
                    #5
                    elif(comecar == "o5"):
                        if(section_ciclo == 1):
                            ciclo_1_1 = 0
                            ciclo_1_2 = 0
                            ciclo_1_3 = 0
                            ciclo_1_4 = 0
                            ciclo_1_5 = 2
                            ciclo_1_6 = 0
                    #6
                    elif(comecar == "o6"):
                        if(section_ciclo == 1):
                            ciclo_1_1 = 0
                            ciclo_1_2 = 0
                            ciclo_1_3 = 0
                            ciclo_1_4 = 0
                            ciclo_1_5 = 0
                            ciclo_1_6 = 2
                    #Repetidor
                    elif(comecar == "or") or (comecar == "Or"):
                        print("Repetido da Onda:", o_atual, "Seção", section_ciclo)
                        estado_config = 3
                    #Remover
                    elif(comecar == "o-") or (comecar == "O-"):
                        print("Selecione açuma onda para ser deletada")
                        estado_config = 4
                    #Comprimenoto
                    elif(comecar == "T") or (comecar == "t"):
                        print("Tamanho da Onda", o_atual, "Seção:",section_ciclo)
                        estado_config = 5
                    #Altura
                    elif(comecar == "a") or (comecar == "A"):
                        print("Altura final da Onda:", o_atual, "Seção", section_ciclo)
                        estado_config = 6
                    #Suavidade
                    elif(comecar == "S") or (comecar == "s"):
                        print("Suavidade da Onda[S|N]:", o_atual, "Seção", section_ciclo)
                        estado_config = 7
                    #Espaçamento
                    elif(comecar == "e") or (comecar == "E"):
                        print("Espaçamento da Onda:", o_atual, "Seção", section_ciclo)
                        estado_config = 8
                    #Números
                    #Multiplos mútuos
                    elif(comecar == "N m") or (comecar == "n M") or (comecar == "n m"):
                        print("Número a ser multiplicado por si mesmo, da Onda", o_atual, "Seção",  section_ciclo)
                        estado_config = 9
                    #Fatores
                    #Fator1
                    elif(comecar == "N1") or (comecar == "n1"):
                        if(t_atual == 1):
                            print("Multiplo 1 da Onda", o_atual, "Seção", section_ciclo)
                        elif(t_atual == 2):
                            print("Dividendo da Onda", o_atual, "Seção", section_ciclo)
                        estado_config = 10
                    #Fator 2
                    elif(comecar == "N2") or (comecar == "n2"):
                        if(t_atual == 1):
                            print("Multiplo 2 da Onda", o_atual, "Seção", section_ciclo)
                        elif(t_atual == 2):
                            print("Divisor da Onda", o_atual, "Seção", section_ciclo)
                        estado_config = 11
                    #Listagem
                    #Local
                    elif(comecar == "L") or (comecar == "l"):
                        print("Lista das configurações da onda atual:")
                        if(section_ciclo == 1):
                            print("\n", "==============","\n","Seção 1")
                            #1
                            if(ciclo_1_1 != 0):
                                print("Onda 1", "\n", "Tamanho:", quant_dej_dir_1_1, "\n""Altura:",    rigth_armazenada_1_1,"\n", "Altura inicial:",r_init_armazenada_1_1,   "\n", "Espaçamento:", esp_des_1_1)
                                if(onda_1_1_t == 1):
                                    print("Fatores:", "\n", "1:",  fator1_1_1, "\n","2", fator2_1_1)
                                elif(onda_1_1_t == 2):
                                    print("Dividendo", fator1_1_1, "\n","Divisor", di_1_1)
                                print("Suavidade:", sua_1_1, "\n","Repetição:", repet_ciclo_1_1, "\n")
                            #2
                            elif(ciclo_1_2 != 0):
                                print("Onda 2", "\n", "Tamanho:", quant_dej_dir_1_2, "\n""Altura:",    rigth_armazenada_1_2,"\n", "Altura inicial:",r_init_armazenada_1_2,   "\n", "Espaçamento:", esp_des_1_2)
                                if(onda_1_2_t == 1):
                                    print("Fatores:", "\n", "1:",  fator1_1_2, "\n","2", fator2_1_2)
                                elif(onda_1_2_t == 2):
                                    print("Dividendo", fator1_1_2, "\n","Divisor", di_1_2)
                                print("Suavidade:", sua_1_2, "\n","Repetição:", repet_ciclo_1_2, "\n")
                            #3
                            elif(ciclo_1_3 != 0):
                                print("Onda 3", "\n", "Tamanho:", quant_dej_dir_1_3, "\n""Altura:",    rigth_armazenada_1_3,"\n", "Altura inicial:",r_init_armazenada_1_3,   "\n", "Espaçamento:", esp_des_1_3)
                                if(onda_1_3_t == 1):
                                    print("Fatores:", "\n", "1:",  fator1_1_3, "\n","2", fator2_1_3)
                                elif(onda_1_3_t == 2):
                                    print("Dividendo", fator1_1_3, "\n","Divisor", di_1_3)
                                print("Suavidade:", sua_1_3, "\n","Repetição:", repet_ciclo_1_3, "\n")
                            #4
                            elif(ciclo_1_4 != 0):
                                print("Onda 4", "\n", "Tamanho:", quant_dej_dir_1_4, "\n","Altura:", rigth_armazenada_1_4,"\n", "Altura inicial:",r_init_armazenada_1_4,"\n", "Espaçamento:", esp_des_1_4)
                                if(onda_1_4_t == 1):
                                    print("Fatores:", "\n", "1:",  fator1_1_4, "\n","2", fator2_1_4)
                                elif(onda_1_4_t == 2):
                                    print("Dividendo", fator1_1_4, "\n","Divisor", di_1_4)
                                print("Suavidade:", sua_1_4, "\n","Repetição:", repet_ciclo_1_4, "\n")
                            #5
                            elif(ciclo_1_5 != 0):
                                print("Onda 5", "\n", "Tamanho:", quant_dej_dir_1_5, "\n","Altura:", rigth_armazenada_1_5,"\n", "Altura inicial:",r_init_armazenada_1_5,"\n", "Espaçamento:", esp_des_1_5)
                                if(onda_1_5_t == 1):
                                    print("Fatores:", "\n", "1:",  fator1_1_5, "\n","2", fator2_1_5)
                                elif(onda_1_5_t == 2):
                                    print("Dividendo", fator1_1_5, "\n","Divisor", di_1_5)
                                print("Suavidade:", sua_1_5, "\n","Repetição:", repet_ciclo_1_5, "\n")
                            #6
                            elif(ciclo_1_6 != 0):
                                print("Onda 6", "\n", "Tamanho:", quant_dej_dir_1_6, "\n","Altura:", rigth_armazenada_1_6,"\n", "Altura inicial:",r_init_armazenada_1_6,"\n", "Espaçamento:", esp_des_1_6)
                                if(onda_1_6_t == 1):
                                    print("Fatores:", "\n", "1:",  fator1_1_6, "\n","2", fator2_1_6)
                                elif(onda_1_6_t == 2):
                                    print("Dividendo", fator1_1_6, "\n","Divisor", di_1_6)
                                print("Suavidade:", sua_1_6, "\n","Repetição:", repet_ciclo_1_6, "\n")
                            print("==============", "\n")
                    #Geral
                    elif(comecar == "Lg") or (comecar == "lg"):
                        if(section_ciclo == 1):
                            print("\n", "==============")
                            if(repet_sectio_1>1):
                                print("Seção 1 repete", repet_sectio_1, "vezes")
                            else:
                                print("Seção 1 repete", repet_sectio_1, "vez")
                            #1
                            if(quant_dej_dir_1_1 != 0):
                                if(onda_1_1_t<1) or (onda_1_1_t>quant_tipo):
                                    print("Onda 1 | Modelo inválido")
                                else:
                                    print("Onda 1 | Tipo:", onda_1_1_t)
                                print("Tamanho:", quant_dej_dir_1_1, "\n","Espaçamento:", esp_des_1_1, "\n","Altura:", rigth_armazenada_1_1)
                                if(onda_1_1_t == 1):
                                    print("Altura inicial:",r_init_armazenada_1_1, "\n","Fatores:", "\n", "1:", fator1_1_1, "\n","2", fator2_1_1)
                                elif(onda_1_1_t == 2):
                                    print("Dividendo:", fator1_1_1,"\n","Divisor:", fator2_1_1)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_1, "\n","Repetição:", repet_ciclo_1_1, "\n")
                            #2
                            if(quant_dej_dir_1_2 != 0):
                                if(onda_1_2_t<1) or (onda_1_2_t>quant_tipo):
                                    print("Onda 2 | Modelo inválido")
                                else:
                                    print("Onda 2 | Tipo:", onda_1_2_t)
                                print("Tamanho:", quant_dej_dir_1_1, "\n", "Espaçamento:", esp_des_1_1, "\n","Altura:", rigth_armazenada_1_1)
                                if(onda_1_2_t == 1):
                                    print("Altura inicial:",r_init_armazenada_1_2, "\n","Fatores:", "\n", "1:", fator1_1_2, "\n","2", fator2_1_2)
                                elif(onda_1_2_t == 2):
                                    print("Dividendo:", fator1_1_2, "\n","Divisor:", fator2_1_2)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_2, "\n","Repetição:", repet_ciclo_1_2, "\n")
                            #3
                            if(quant_dej_dir_1_3 != 0):
                                if(onda_1_3_t<1) or (onda_1_3_t>quant_tipo):
                                    print("Onda 3 | Modelo inválido")
                                else:
                                    print("Onda 3 | Tipo:", onda_1_3_t)
                                print("Tamanho:", quant_dej_dir_1_3, "\n", "Espaçamento:", esp_des_1_3, "\n","Altura:", rigth_armazenada_1_3)
                                if(onda_1_3_t == 1):
                                    print("Altura inicial:",r_init_armazenada_1_3, "\n","Fatores:", "\n", "1:", fator1_1_3, "\n","2", fator2_1_3)
                                elif(onda_1_3_t == 2):
                                    print("Dividendo:", fator1_1_3, "\n","Divisor:", fator2_1_3)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_3, "\n","Repetição:", repet_ciclo_1_3, "\n")
                            #4
                            if(quant_dej_dir_1_4 != 0):
                                if(onda_1_4_t<1) or (onda_1_4_t>quant_tipo):
                                    print("Onda 4 | Modelo inválido")
                                else:
                                    print("Onda 4 | Tipo:", onda_1_4_t)
                                print("Tamanho:", quant_dej_dir_1_4, "\n", "Espaçamento:", esp_des_1_4, "\n","Altura:", rigth_armazenada_1_4)
                                if(onda_1_4_t == 1):
                                    print("Altura inicial:",r_init_armazenada_1_4, "\n","Fatores:", "\n", "1:", fator1_1_4, "\n","2", fator2_1_4)
                                elif(onda_1_4_t == 2):
                                    print("Dividendo:", fator1_1_4, "\n","Divisor:", fator2_1_4)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_4, "\n","Repetição:", repet_ciclo_1_4, "\n")
                            #5
                            if(quant_dej_dir_1_5 != 0):
                                if(onda_1_5_t<1) or (onda_1_5_t>quant_tipo):
                                    print("Onda 5 | Modelo inválido")
                                else:
                                    print("Onda 5 | Tipo:", onda_1_5_t)
                                print("Tamanho:", quant_dej_dir_1_5, "\n", "Espaçamento:", esp_des_1_5, "\n","Altura:", rigth_armazenada_1_5)
                                if(onda_1_5_t == 1):
                                    print("Altura inicial:",r_init_armazenada_1_5, "\n","Fatores:", "\n", "1:", fator1_1_5, "\n","2", fator2_1_5)
                                elif(onda_1_5_t == 2):
                                    print("Dividendo:", fator1_1_5, "\n","Divisor:", fator2_1_5)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_5, "\n","Repetição:", repet_ciclo_1_5, "\n")
                            #6
                            if(quant_dej_dir_1_6 != 0):
                                if(onda_1_6_t<1) or (onda_1_6_t>quant_tipo):
                                    print("Onda 6 | Modelo inválido")
                                else:
                                    print("Onda 6 | Tipo:", onda_1_6_t)
                                print("Tamanho:", quant_dej_dir_1_6, "\n", "Espaçamento:", esp_des_1_6, "\n","Altura:", rigth_armazenada_1_6)
                                if(onda_1_6_t == 1):
                                    print("Altura inicial:",r_init_armazenada_1_6, "\n","Fatores:", "\n", "1:", fator1_1_6, "\n","2", fator2_1_6)
                                elif(onda_1_6_t == 2):
                                    print("Dividendo:", fator1_1_6, "\n","Divisor:", fator2_1_6)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_6, "\n","Repetição:", repet_ciclo_1_6, "\n")
                            print("==============", "\n")
                    #Dúvida
                    elif(comecar == "?"):
                        print("Seção:", section_ciclo, "Onda:", o_atual)
                    #Finalização
                    elif(comecar == "f") or (comecar == "F"):
                        estado_config = 14
                    #Modo DS
                    elif(comecar == "ds") or (comecar == "Ds"):
                        print("Como você descobriu aqui !!!???")
                        modo_ds = int(input(""))
                    #Altura Inicial
                    elif(comecar == "ai") or (comecar == "Ai") or (comecar == "AI!"):
                        print("Digite a altura inicicial de sua onda")
                        estado_config = 12
                    #Tipo
                    elif(comecar == "mo") or (comecar == "Mo"):
                        print("Selecione o modelo da onda", o_atual, "Seção", section_ciclo)
                        estado_config = 13
                    #Erro
                    else:
                        print("Inválido, tente novamente")
                else:
                    if(estado_config != 7) and (estado_config != 13) and (estado_config != 14):
                        comecar = int(input(""))
                    else:
                        comecar = 1
                    if type(comecar) is int and (comecar>0):
                        #Proscessadores
                        #Seção padrão
                        def retornador():
                            return comecar
                        #Seletor de seções
                        if(estado_config == 2):
                            def section(esc):
                                    if(comecar == 1):
                                        return 1
                                    elif(comecar == 2):
                                        return 2
                                    elif(comecar == 3):
                                        return 3
                            section_ciclo = section(int())
                        #Rpetidor|Cicilo
                        elif(estado_config == 3):
                            if(ciclo_1_1 == 2):
                                repet_ciclo_1_1 = retornador()
                            elif(ciclo_1_2 == 2):
                                repet_ciclo_1_2 = retornador()
                            elif(ciclo_1_3 == 2):
                                repet_ciclo_1_3 = retornador()
                            elif(ciclo_1_4 == 2):
                                repet_ciclo_1_4 = retornador()
                            elif(ciclo_1_5 == 2):
                                repet_ciclo_1_5 = retornador()
                            elif(ciclo_1_6 == 2):
                                repet_ciclo_1_6 = retornador()
                        #Removedor
                        elif(estado_config == 4):
                            if(section_ciclo == 1):
                                #1
                                if(comecar == 1):
                                    quant_dej_dir_1_1 = 0
                                    repet_ciclo_1_1 = 0
                                    remover_1 = 1
                                #2
                                elif(comecar == 2):
                                    quant_dej_dir_1_2 = 0
                                    repet_ciclo_1_2 = 0
                                    remover_1 = 2
                                #3
                                elif(comecar == 3):
                                    quant_dej_dir_1_3 = 0
                                    repet_ciclo_1_3 = 0
                                    remover_1 = 3
                                #4
                                elif(comecar == 4):
                                    quant_dej_dir_1_4 = 0
                                    repet_ciclo_1_4 = 0
                                    remover_1 = 4
                                #5
                                elif(comecar == 5):
                                    quant_dej_dir_1_5 = 0
                                    repet_ciclo_1_5 = 0
                                    remover_1 = 5
                                #6
                                elif(comecar == 6):
                                    quant_dej_dir_1_6 = 0
                                    repet_ciclo_1_6 = 0
                                    remover_1 = 6
                        #Tamanho
                        elif(estado_config == 5):
                            if(section_ciclo == 1):
                                if(ciclo_1_1 == 2):
                                    quant_dej_dir_1_1 = retornador()
                                elif(ciclo_1_2 == 2):
                                    quant_dej_dir_1_2 = retornador()
                                elif(ciclo_1_3 == 2):
                                    quant_dej_dir_1_3 = retornador()
                                elif(ciclo_1_4 == 2):
                                    quant_dej_dir_1_4 = retornador()
                                elif(ciclo_1_5 == 2):
                                    quant_dej_dir_1_5 = retornador()
                                elif(ciclo_1_6 == 2):
                                    quant_dej_dir_1_6 = retornador()
                            remover_1 = 0
                        #Altura
                        elif(estado_config == 6):
                            if(section_ciclo == 1):#S1
                                if(ciclo_1_1 == 2):#1
                                    rigth_armazenada_1_1 = retornador()
                                elif(ciclo_1_2 == 2):#2
                                    rigth_armazenada_1_2 = retornador()
                                elif(ciclo_1_3 == 2):#3
                                    rigth_armazenada_1_3 = retornador()
                                elif(ciclo_1_4 == 2):#4
                                    rigth_armazenada_1_4 = retornador()
                                elif(ciclo_1_5 == 2):#5
                                    rigth_armazenada_1_5 = retornador()
                                elif(ciclo_1_6 == 2):#6
                                    rigth_armazenada_1_6 = retornador()
                        #Suavidade
                        elif(estado_config == 7):
                            def suave_d(sus):
                                if(sus == "S") or (sus == "s"):
                                    return 1
                                elif(sus == "N") or (sus == "n"):
                                    return 0
                                else:
                                    print("Inválido")
                            sus = suave_d(str(input("")))
                            if(ciclo_1_1 == 2):
                                sua_1_1 = sus
                            elif(ciclo_1_2 == 2):
                                sua_1_2 = sus
                            elif(ciclo_1_3 == 2):
                                sua_1_3 = sus
                            elif(ciclo_1_4 == 2):
                                sua_1_4 = sus
                            elif(ciclo_1_5 == 2):
                                sua_1_5 = sus
                            elif(ciclo_1_6 == 2):
                                sua_1_6 = sus
                        #Espaçamento
                        elif(estado_config == 8):
                            if(section_ciclo == 1):
                                if(ciclo_1_1 == 2):
                                    esp_des_1_1 = retornador()
                                elif(ciclo_1_2 == 2):
                                    esp_des_1_2 = retornador()
                                elif(ciclo_1_3 == 2):
                                    esp_des_1_3 = retornador()
                                elif(ciclo_1_4 == 2):
                                    esp_des_1_4 = retornador()
                                elif(ciclo_1_5 == 2):
                                    esp_des_1_5 = retornador()
                                elif(ciclo_1_6 == 2):
                                    esp_des_1_6 = retornador()
                        #Multiplo mutuo
                        elif(estado_config == 9):
                            if(section_ciclo == 1):
                                if(ciclo_1_1 == 2):
                                    fator1_1_1 = retornador()
                                    fator2_1_1 = retornador()
                                elif(ciclo_1_2 == 2):
                                    fator1_1_2 = retornador()
                                    fator2_1_2 = retornador()
                                elif(ciclo_1_3 == 2):
                                    fator1_1_3 = retornador()
                                    fator2_1_3 = retornador()
                                elif(ciclo_1_4 == 2):
                                    fator1_1_4 = retornador()
                                    fator2_1_4 = retornador()
                                elif(ciclo_1_5 == 2):
                                    fator1_1_5 = retornador()
                                    fator2_1_5 = retornador()
                                elif(ciclo_1_6 == 2):
                                    fator1_1_6 = retornador()
                                    fator2_1_6 = retornador()
                        #Fator1
                        elif(estado_config == 10):
                            if(section_ciclo == 1):
                                if(ciclo_1_1 == 2):
                                    fator1_1_1 = retornador()
                                elif(ciclo_1_2 == 2):
                                    fator1_1_2 = retornador()
                                elif(ciclo_1_3 == 2):
                                    fator1_1_3 = retornador()
                                elif(ciclo_1_4 == 2):
                                    fator1_1_4 = retornador()
                                elif(ciclo_1_5 == 2):
                                    fator1_1_5 = retornador()
                                elif(ciclo_1_6 == 2):
                                    fator1_1_6 = retornador()
                        #Fator2
                        elif(estado_config == 11):
                            if(section_ciclo == 1):
                                if(ciclo_1_1 == 2):
                                    fator2_1_1 = retornador()
                                elif(ciclo_1_2 == 2):
                                    fator2_1_2 = retornador()
                                elif(ciclo_1_3 == 2):
                                    fator2_1_3 = retornador()
                                elif(ciclo_1_4 == 2):
                                    fator2_1_4 = retornador()
                                elif(ciclo_1_5 == 2):
                                    fator2_1_5 = retornador()
                                elif(ciclo_1_6 == 2):
                                    fator2_1_6 = retornador()
                        #Altura inicial
                        elif(estado_config == 12):
                            if(section_ciclo == 1):
                                if(ciclo_1_1 == 2):
                                    r_init_armazenada_1_1 = retornador()
                                elif(ciclo_1_2 == 2):
                                    r_init_armazenada_1_2 = retornador()
                                elif(ciclo_1_3 == 2):
                                    r_init_armazenada_1_3 = retornador()
                                elif(ciclo_1_4 == 2):
                                    r_init_armazenada_1_4 = retornador()
                                elif(ciclo_1_5 == 2):
                                    r_init_armazenada_1_5 = retornador()
                                elif(ciclo_1_6 == 2):
                                    r_init_armazenada_1_6 = retornador()
                        #Modelo
                        elif(estado_config == 13):
                            def sel_tipo(t):
                                if(t == "m") or (t == "M"):
                                    return 1
                                elif(t == "d") or (t == "D"):
                                    return 2
                                elif(t == "ad") or (t == "Ad") or (t == "AD"):
                                    return 3
                                elif(t == "sub") or (t == "Sub") or (t == "SUB"):
                                    return 4
                                elif(t == "ra") or (t == "Ra") or (t == "RA"):
                                    return 5
                            selecionar_tipo = sel_tipo(str(input("")))
                            if(section_ciclo == 1):
                                if(ciclo_1_1 == 2):
                                    onda_1_1_t = selecionar_tipo
                                elif(ciclo_1_2 == 2):
                                    onda_1_2_t = selecionar_tipo
                                elif(ciclo_1_3 == 2):
                                    onda_1_3_t = selecionar_tipo
                                elif(ciclo_1_4 == 2):
                                    onda_1_4_t = selecionar_tipo
                                elif(ciclo_1_5 == 2):
                                    onda_1_5_t = selecionar_tipo
                                elif(ciclo_1_6 == 2):
                                    onda_1_6_t = selecionar_tipo
                        #Finalização
                        elif(estado_config == 14):
                            ciclo_des = repet_ciclo_1_1+repet_ciclo_1_2+repet_ciclo_1_3+repet_ciclo_1_4 +repet_ciclo_1_5+repet_ciclo_1_6
                            if(quant_dej_dir_1_1 != 0):
                                ciclo_1_1 = 1
                                ciclo_1_2 = 0
                                ciclo_1_3 = 0
                                ciclo_1_4 = 0
                                ciclo_1_5 = 0
                                ciclo_1_6 = 0
                                depois = 1
                            elif(quant_dej_dir_1_2 != 0):
                                ciclo_1_1 = 0
                                ciclo_1_2 = 1
                                ciclo_1_3 = 0
                                ciclo_1_4 = 0
                                ciclo_1_5 = 0
                                ciclo_1_6 = 0
                                depois = 2
                            elif(quant_dej_dir_1_3 != 0):
                                ciclo_1_1 = 0
                                ciclo_1_2 = 0
                                ciclo_1_3 = 1
                                ciclo_1_4 = 0
                                ciclo_1_5 = 0
                                ciclo_1_6 = 0
                                depois = 3
                            elif(quant_dej_dir_1_4 != 0):
                                ciclo_1_1 = 0
                                ciclo_1_2 = 0
                                ciclo_1_3 = 0
                                ciclo_1_4 = 1
                                ciclo_1_5 = 0
                                ciclo_1_6 = 0
                                depois = 4
                            elif(quant_dej_dir_1_5 != 0):
                                ciclo_1_1 = 0
                                ciclo_1_2 = 0
                                ciclo_1_3 = 0
                                ciclo_1_4 = 0
                                ciclo_1_5 = 1
                                ciclo_1_6 = 0
                                depois = 5
                            elif(quant_dej_dir_1_6 != 0):
                                ciclo_1_1 = 0
                                ciclo_1_2 = 0
                                ciclo_1_3 = 0
                                ciclo_1_4 = 0
                                ciclo_1_5 = 0
                                ciclo_1_6 = 1
                                depois = 6
                            configuracoes = 2
                    else:
                        if(comecar<0):
                            print("Por favor, não insira valores negativos")
                        elif not type(comecar) is int:
                            print("Por favor, não insira qualquer besteira, e sim números de concreto, isto é, números concretos(inteiros e postivos) XD")
                    estado_config = 1
                entra = entra+1
            if(configuracoes == 2):
                comecar = str(input(""))
        if(comecar == "C") or (comecar == "c"):
            ativador = 1
        #Execução   
        while(ativador == 1):
            ciclo = 0
            while(ciclo<ciclo_des):
                contagem_esp_armazenamento = 0
                #Comprimento
                def onda_quant(quant):
                    if( section_ciclo == 1):
                        if(ciclo_1_1 == 1) and (remover_1 != 1):
                            return quant_dej_dir_1_1
                        elif(ciclo_1_2 == 1) and (remover_1 != 2):
                            return quant_dej_dir_1_2
                        elif(ciclo_1_3 == 1) and (remover_1 != 3):
                            return quant_dej_dir_1_3
                        elif(ciclo_1_4 == 1) and (remover_1 != 4):
                            return quant_dej_dir_1_4
                        elif(ciclo_1_5 == 1) and (remover_1 != 5):
                            return quant_dej_dir_1_5
                        elif(ciclo_1_6 == 1) and (remover_1 != 6):
                            return quant_dej_dir_1_5
                quant_armazenada = onda_quant(int())
                #Largura
                #Absoluta
                def onda_d(d):
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return rigth_armazenada_1_1
                        elif(ciclo_1_2 == 1):
                            return rigth_armazenada_1_2
                        elif(ciclo_1_3 == 1):
                            return rigth_armazenada_1_3
                        elif(ciclo_1_4 == 1):
                            return rigth_armazenada_1_4
                        elif(ciclo_1_5 == 1):
                            return rigth_armazenada_1_5
                        elif(ciclo_1_6 == 1):
                            return rigth_armazenada_1_6
                rigth_armazenada = onda_d(int())
                #Relativa(?)
                #Inicial
                def onda_d_inicial(di):
                    if(ciclo_1_1 == 1):
                        return r_init_armazenada_1_1
                    elif(ciclo_1_2 == 1):
                        return r_init_armazenada_1_2
                    elif(ciclo_1_3 == 1):
                        return r_init_armazenada_1_3
                    elif(ciclo_1_4 == 1):
                        return r_init_armazenada_1_4
                    elif(ciclo_1_5 == 1):
                        return r_init_armazenada_1_5
                    elif(ciclo_1_6 == 1):
                        return r_init_armazenada_1_6
                rigth_inicial_armazenada = onda_d_inicial(int())
                #Espaçamento
                def onda_esp(esp):
                    if( section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return esp_des_1_1
                        elif(ciclo_1_2 == 1):
                            return esp_des_1_2
                        elif(ciclo_1_3 == 1):
                            return esp_des_1_3
                        elif(ciclo_1_4 == 1):
                            return esp_des_1_4
                        elif(ciclo_1_5 == 1):
                            return esp_des_1_5
                        elif(ciclo_1_6 == 1):
                            return esp_des_1_6
                esp_armazenado = onda_esp(int())
                #Número
                #Fatores
                def onda_fato1(f1):
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return fator1_1_1
                        elif(ciclo_1_2 == 1):
                            return fator1_1_2 
                        elif(ciclo_1_3 == 1):
                            return fator1_1_3 
                        elif(ciclo_1_4 == 1):
                            return fator1_1_4 
                        elif(ciclo_1_5 == 1):
                            return fator1_1_5 
                        elif(ciclo_1_6 == 1):
                            return fator1_1_6 
                fator1_armazenado = onda_fato1(int())
                def onda_fato2(f2):
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return fator2_1_1
                        elif(ciclo_1_2 == 1):
                            return fator2_1_2 
                        elif(ciclo_1_3 == 1):
                            return fator2_1_3 
                        elif(ciclo_1_4 == 1):
                            return fator2_1_4 
                        elif(ciclo_1_5 == 1):
                            return fator2_1_5 
                        elif(ciclo_1_6 == 1):
                            return fator2_1_6 
                fator2_armazenado = onda_fato2(int())
                #Suavidade
                def onda_suave(su):
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return sua_1_1
                        elif(ciclo_1_2 == 1):
                            return sua_1_2
                        elif(ciclo_1_3 == 1):
                            return sua_1_3
                        elif(ciclo_1_4 == 1):
                            return sua_1_4
                        elif(ciclo_1_5 == 1):
                            return sua_1_5
                        elif(ciclo_1_6 == 1):
                            return sua_1_6
                pro_ro_armazenamento = onda_suave(int())
                #Tipo
                def onda_tipo(t):
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            return onda_1_1_t
                        elif(ciclo_1_2 == 1):
                            return onda_1_2_t
                        elif(ciclo_1_3 == 1):
                            return onda_1_3_t
                        elif(ciclo_1_4 == 1):
                            return onda_1_4_t
                        elif(ciclo_1_5 == 1):
                            return onda_1_5_t
                        elif(ciclo_1_6 == 1):
                            return onda_1_6_t
                tipo_armazenado = onda_tipo(int())
                #DS
                if(modo_ds == 1):
                    print("Quant:", quant_armazenada, "\n", "R:", rigth_armazenada, "\n",  "E:", esp_armazenado,"\n", "Fatores", "\n", "1:", fator1_armazenado, "\n", "2:", fator2_armazenado)
                    if(section_ciclo == 1):
                        if(ciclo_1_1 == 1):
                            print("Onda 1")
                        elif(ciclo_1_2 == 1):
                            print("Onda 2")
                        elif(ciclo_1_3 == 1):
                            print("Onda 3")
                        elif(ciclo_1_4 == 1):
                            print("Onda 4")
                        elif(ciclo_1_5 == 1):
                            print("Onda 5")
                        elif(ciclo_1_6 == 1):
                            print("Onda 6")
                #Tipo
                tipo = tipo_armazenado
                #Comprimento
                quant_dej_dir = quant_armazenada
                #Largura
                #Progressiva
                rigth_desj = rigth_armazenada
                #Cortada
                rigth_inical = rigth_inicial_armazenada
                #Espaçamento
                esp_des = esp_armazenado
                #Fatores
                fator1 = fator1_armazenado
                fator2 = fator2_armazenado
                #Suavidade
                pro_ro = pro_ro_armazenamento
                contagem_esp = 0
                quant = 0
                rigth = 1
                rigth_tot = 0
                #X
                X = fator1_armazenado
                #Armazenadores
                armazenador_x = 1
                armazenador_x_2 = 0
                #Coração do sistema
                while(quant < quant_dej_dir):
                    #Onda
                    #Altura total
                    def r_t(rt):
                        if(tipo == 1):
                            return fator1*(fator2**rigth_armazenada)
                        elif(tipo == 2):
                            return rigth_desj
                    rigth_tot = r_t(int())
                    #Proporção
                    def porpor(proporcao):
                        if(tipo == 1):
                            proporcao = rigth_desj/quant_dej_dir
                        elif(tipo == 2):
                            x = rigth_tot+1
                            proporcao = 1
                            rigth = 1
                            while(x>rigth_tot):
                                armazenador_xx = x
                                x = fator1/(fator2**rigth*proporcao)
                                proporcao = proporcao+1
                                rigth = rigth+1
                            proporcao = proporcao/quant_dej_dir
                        #Proporcão nomral|grande
                        if(proporcao >= 1):
                                if((proporcao-int(proporcao))*10>= 5):
                                    return int(proporcao)+1
                                else:
                                    return int(proporcao)
                        #Proporção pequena
                        else:
                            return proporcao
                    proporcao = porpor(int())
                    #Para proporção grande
                    if(rigth_armazenada>quant_dej_dir):
                        rigth_desj = quant_dej_dir
                    #Para proporção pequena
                    elif(quant_armazenada>rigth_armazenada):
                        quant_dej_dir = rigth_armazenada
                    if(proporcao<1):
                        resto_prop = proporcao
                        proporcao = int(1)
                        resto = 1/resto_prop
                        esp_des = esp_des*resto
                        if((esp_des - int(esp_des))*10 >=5):
                            esp_des = int(esp_des)+1
                        else:
                            esp_des = int(esp_des)
                        if(modo_ds == 1):
                            print("P", proporcao ,"Res", resto, "Esp", esp_des)
                    if(modo_ds == 1):
                        print("P", proporcao)
                    #Valor inicial da altura
                    if(rigth_inical != 1):
                        fator21 = fator2
                    else:
                        fator21 = 1
                    if(modo_ds == 1):
                        print("RT:", rigth_tot)
                    #Ondas
                    while(rigth <= rigth_desj) or (quant <= quant_dej_dir):
                        #X futuro
                        def ar_fut(ff):
                            if(tipo == 1):
                                return (fator1*fator21**rigth_inical)*(fator2**((rigth+1) *proporcao))
                            elif(tipo == 2):
                                return fator1/(fator2**((rigth+1)*proporcao))
                        armazenador_x_fut = ar_fut(int())
                        if(modo_ds == 1):
                             print("ARF:", armazenador_x_fut)
                        #Inicializador
                        if(quant<=0) and (rigth_inical == 1):
                            print(int(fator1))
                        #Ondinhas
                        def ondas(x):
                            if(tipo == 1):
                                if(rigth_desj>=rigth) and (armazenador_x_fut<=rigth_tot):
                                    if(modo_ds == 1):
                                        print("RD!")
                                    return (x*fator21**rigth_inical)*(fator2**(rigth*proporcao))
                                elif(rigth_desj<=rigth) and (armazenador_x_2>=rigth_tot):
                                    if(modo_ds == 1):
                                        print("RD2", rigth_desj)
                                    return armazenador_x_2
                                elif(armazenador_x_fut>=rigth_tot):
                                    if(modo_ds == 1):
                                        print("RT")
                                    return rigth_tot
                            elif(tipo == 2):
                                if(rigth<=rigth_desj) and (armazenador_x_fut>rigth_tot):
                                    return x/(fator2**(proporcao*rigth))
                                elif(armazenador_x_fut<rigth_tot) or (rigth_desj<=rigth):
                                    return rigth_tot
                            elif(tipo == 3):
                                if(rigth<=rigth_desj):
                                    return x+((fator2*proporcao))
                        X = int(ondas(fator1))
                        armazenador_x = X
                        armazenador_x_2 = armazenador_x
                        #Exibirdores
                        #Suave
                        if(pro_ro == 1):
                            if(quant % esp_des == 0) and (quant!= 0) or (quant!=   quant_dej_dir-1):
                                esp = 0
                                while(esp < esp_des):
                                    contagem_esp = 0
                                    if(modo_ds == 1):
                                        print("Q", quant, "E", contagem_esp_armazenamento,X,"\n", "Suave, sim")
                                    else:
                                        print(X)
                                    contagem_esp = 1
                                    contagem_esp_armazenamento = contagem_esp  +contagem_esp_armazenamento
                                    esp = esp+1
                            else:
                                if(modo_ds == 1):
                                    print("Q", quant, X, "\n", "Suave, não")
                                else:
                                    print(X)
                        #Caótico
                        elif(pro_ro == 0):
                            if(quant % esp_des == 0) and (quant != 0):
                                esp = 0
                                while(esp < esp_des):
                                    if(modo_ds == 1):
                                        print("Q", quant, "E", esp, X, "Não suave sim")
                                    else:
                                        print(X)
                                    esp = esp+1
                            else:
                                if(modo_ds == 1):
                                    print("Q", quant, X, "Não suave não")
                                else:
                                    print(X)
                            rigth = rigth+1
                        quant = quant+1
                        rigth = rigth+1
                        if(rigth >= rigth_desj):
                            armazenador_x = X
                            # print(armazenador_x)
                ciclo = ciclo+1
                #Redirecionador
                #Ciclos
                if(section_ciclo == 1):
                    #1
                    if(repetidor<=repet_ciclo_1_1) and (depois == 1):
                        if(modo_ds == 1):
                            print("Certo", "R1", repet_ciclo_1_1, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_1):
                            if(quant_dej_dir_1_2 != 0):
                                if(modo_ds == 1):
                                    print("1/2", "Rep", repetidor)
                                ciclo_1_1 = 0
                                ciclo_1_2 = 1
                                depois = 2
                            elif(quant_dej_dir_1_3 != 0):
                                ciclo_1_1 = 0
                                ciclo_1_3 = 1
                                depois= 3
                            elif(quant_dej_dir_1_4 != 0):
                                ciclo_1_1 = 0
                                ciclo_1_4 = 1
                                depois = 4
                            elif(quant_dej_dir_1_5 != 0):
                                ciclo_1_1 = 0
                                ciclo_1_5 = 1
                                depois = 5
                            elif(quant_dej_dir_1_6 != 0):
                                ciclo_1_1 = 0
                                ciclo_1_6 = 1
                                depois = 6
                            else:
                                ciclo_1_1 = 1
                            repetidor = 0
                    #2
                    elif(repetidor<=repet_ciclo_1_2) and (depois == 2):
                        if(modo_ds == 1):
                            print("Certo2", "R2", repet_ciclo_1_2, "Rep", repetidor, "\n""Q",      quant_dej_dir_1_2)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_2):
                            if(quant_dej_dir_1_3 != 0):
                                ciclo_1_3 = 1
                                depois= 3
                            elif(quant_dej_dir_1_4 != 0):
                                ciclo_1_4 = 1
                                depois = 4
                            elif(quant_dej_dir_1_5 != 0):
                                ciclo_1_5 = 1
                                depois = 5
                            elif(quant_dej_dir_1_6 != 0):
                                ciclo_1_6 = 1
                                depois = 6
                            else:
                                ciclo_1_1 = 1
                            ciclo_1_2 = 0
                            repetidor = 0
                    #3
                    elif(repetidor<=repet_ciclo_1_3) and (depois == 3):
                        if(modo_ds == 1):
                            print("Certo3", "R3", repet_ciclo_1_3, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_3):
                            if(quant_dej_dir_1_4 != 0):
                                ciclo_1_4 = 1
                                depois = 4
                            elif(quant_dej_dir_1_5 != 0):
                                ciclo_1_5 = 1
                                depois = 5
                            elif(quant_dej_dir_1_6 != 0):
                                ciclo_1_6 = 1
                                depois = 6
                            else:
                                ciclo_1_1 = 1
                            ciclo_1_3 = 0
                            repetidor = 0
                    #4
                    elif(repetidor<=repet_ciclo_1_4) and (depois == 4):
                        if(modo_ds == 1):
                            print("Certo4", "R4", repet_ciclo_1_4, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_4):
                            if(quant_dej_dir_1_5 != 0):
                                ciclo_1_5 = 1
                                depois = 5
                            elif(quant_dej_dir_1_6 != 0):
                                ciclo_1_6 = 1
                                depois = 6
                            else:
                                ciclo_1_1 = 1
                            ciclo_1_4 = 0
                            repetidor = 0
                    #5
                    elif(repetidor<=repet_ciclo_1_5) and (depois == 5):
                        if(modo_ds == 1):
                            print("Certo5", "R5", repet_ciclo_1_5, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_5):
                            if(quant_dej_dir_1_6 != 0):
                                ciclo_1_6 = 1
                                depois = 6
                            else:
                                ciclo_1_1 = 1
                            ciclo_1_5 = 0
                            repetidor = 0
                    #6
                    elif(repetidor<=repet_ciclo_1_6) and (depois == 6):
                        if(modo_ds == 1):
                            print("Certo6", "R6", repet_ciclo_1_6, "Rep", repetidor)
                        repetidor = repetidor+1
                        if(repetidor == repet_ciclo_1_4):
                            ciclo_1_1 = 1
                            depois = 1
                            ciclo_1_6 = 0
                            repetidor = 0
            #Seções
            repetidor_se = repetidor_se+1
            if(repetidor_se == repet_sectio_1) and (section_ciclo == 1):
                ativador = 0
            if(modo_ds == 1):
                print("RepS", repet_sectio_1, "Repp", repetidor_se)
            depois=1
        vezes = vezes+1
        print("V", vezes)
        text = 1
#Coisas para mexer aqui:
#1- Espaçamento Estável- check
#2- Criar padrões com utilizando as section_ciclos-  check
#3- Criar outros tipos de ondas:
#   Divisão - check
#   Subtração
#   Raízes
#   Adição
#   Exponeciação
#4- Integra cálculo as ondas
#5- Altura inicial personalisável - Check
#6- Mensagens de introdução
#7- Mensagens de aviso
#8- Comjuntos de momórias [0,0,0,0,0,0,1]