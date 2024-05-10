from decimal import Decimal
#Modos
modo_ds = 0
#Renicialização
reniciar = 0
#Valores para as ondas
proporcao = 1
#Raízes
contador = 0
casas_aparecidadas = 1
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
repet_sectio_1 = 1
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
quant_tipo = 4
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
#Uns desejados
uns_desj = 3
#Outros
#Bloqueadores
para = 0
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
e_ant = 1
while (reniciar != 1):
    print("\n")
    onda = 1
    #Repetidor
    while(onda == 1):
        #Renicializanodres importantes. Não mexa!!!
        repetidor_se = 0
        depois = 1
        t_atual = 1
        para = 0
        #Texto
        while(text == 1):
            #Início
            if(vezes<1):
                print("Olá, bem_vindo ao ondinhas.py!","\n","Aqui você pode, como deve ter presumido, fazer ondinhas dos mais variáveis jeitos, deste de suaves á ondas ígrimes ou, até, verdadeiras tempestades, além de poder personalisa-lás.","\n", "Caso queira ver o projeto de uma vez, apenas pressione c no termianal! Porém, caso queria mudar alguma das configurações das ondas, sinta-se a vontade para fazer isso. Apenas digite config e faça as suas mudanças")
            elif(vezes != 0):
                if(vezes<2):
                    print("Gostou do programinnhas? Não importa, para ser franco contigo, não tem como enviar feedback XD, por enquanto...","\n","Entretanto, como toda via, você pode repetir quantas vezes quiser,apenas digite 'C' logo abixo e, claro, se quiser fazer alguma mudança, digite confing")
            text = 0
        while(configuracoes == 1):
            if(exibir_instrucoes == 1):
                print("\n")
                print("Olá, esta daqui é a oficina das ondinhas! Para começarmos presciso explicar algumas coisas...", "\n", "A primeira é que existem 4 tipos de ondas que você pode fazer, dois que aumentam as ondas, os tipos de multiplicação e exponenciação dos valores n1 com 2, e as outros dois que diminuem, a divisão e a radiciação entre os mesmos termos.", "\n","A segunda coisas importante de entender é para tomar cuidado com os números de entrada, principalmente quando se usa o tipo de exponenciação! Se der erro, o sistema avisa, porém, quando ele manipula valores muito altos, como x^1024(pode parecer uma realide distante, mas coloque os valore de a e t iguais a 15 para ver a baguncinha que dá), ele demorará tanto que, até exibir uma mensagem de erro, será o ano da revolução das máquinas. Apenas tome cuidado", "\n", "A Terceira coisa importante são quantas ondas distintas pode-se fazer, sendo o total de 6. Isso mesmo, você pode criar até 6 ondas distintas e repeti-lás em padrão(futuramente 'ões') por quantas vezes quiser! Isto claro, dentro dos limites que o seu computador aguenta. Infelizmente, o DS está projetando outras coisas e variedades e quantidades maiores de padrões algum dia chegarão","\n", "A quarta coisa é a parte de exibir os valores do tipo de onda e suavidade. Por conta de projetos mais importantes, o DS deixou meio cagadinha essa parte, mas o que um pouco de fala não resolve isso, não é?. Bem, os valores são os seguintes:", "\n", "Tipos de ondas", "\n", "1-Multiplicação", "\n", "2-Divisão", "\n","3-Exponenciação", "\n", "4-Radiciação","\n","\n","Valores da Suavidade", "\n", "1-Ativada", "\n", "2-Desativada","\n", "\n","A quinta coisa importante de dizer são os comandos -como eu poederia esquercer!-, eles são:", "\n", "\n","'T/t' --> Define o tamanho(vertical) da onda", "\n", "'A/a' --> Define a altura(tamanho horizontal) final da onda", "\n", "'Ai/ai' --> Define a altura(tamanho horinzontal) inicial da onda.","\n" ,"Atenção! O 'ai' ou 'AI!', não é um recurso indisponível nos tipos divisão e raíz das ondas", "\n", "'E/e' --> Define o espaçamento da onda", "\n", "'S/s' --> Define a suavidade das ondas", "\n", "'N1/n1' --> 1º valor de entrada da onda", "\n", "'N2/n2' --> 2º valor de entrada da onda", "\n", "Nota: a função do N1 varia dependendo do tipo de onda, por exemplo, no tipo 'd'(divisão) ele assume a função de dividendo, enquanto no modelo 'ex'(exponenciação), ele assume função de base. Do mesmo jeito, a variação é aplicada ao N2.", "\n", "'Mo/mo --> seleciona o modelo da onda'","\n", "Nota: para atriubuir um tipo á sua onda, digite alguns dos comandos a seguir:", "\n", "'m/M' --> Multiplicaçãp", "\n", "d/D --> Divisão", "\n", "'ex/Ex' --> Exponenciação", "\n", "'ra/Ra' --> Radiciação","\n", "\n","'O/o[1-6]' --> Seleciona a onda que irá configurar", "\n", "'Or/or' --> Define as repetições das ondas, isto é, quantas vezes a onda atual irá repetir", "\n", "O-/o- --> Seleciona a onda que será deletada","\n", "'Str/str' --> Define quantas veze o padrão ondonal(?) irá repetir","\n", "'L/l' --> Lista as configurações da onda atual", "\n", "'Lg/lg' --> Lista as configurações de todas as ondas que, teoricamente, rodarão e funcionarão durante a execução do projeto","\n","'F/f' --> finaliza as configurações", "\n", "\n", "A penúltima coisa importante de dizer é que para uma onda funcionar os seus valores de tamanho repetição devem ser >0. Senão, elas não funcionarão.", "\n", "Por último, mas não menos importante(como o velho ditado!), caso prescise de ajuda com os comandos, digite 'H/h' no terminal", "\n", "\n", "É isso! espero que goste ;)")
                exibir_instrucoes = 0
            #Confiurações
            print("Digite a configuração desejada")
            entra = 0
            while(configuracoes == 1):
                #Ciclo
                ciclo_des = 0
                #Analidador de estado anterior
                if(section_ciclo ==1):
                    if(e_ant == 1):
                        ciclo_1_1 = 2
                    elif(e_ant == 2):
                        ciclo_1_2 = 2
                    elif(e_ant == 3):
                        ciclo_1_3 = 2
                    elif(e_ant == 4):
                        ciclo_1_4 = 2
                    elif(e_ant == 5):
                        ciclo_1_5 = 2
                    elif(e_ant == 6):
                        ciclo_1_6 = 2
                    e_ant = 0
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
                            elif(onda_1_1_t == 3):
                                return 3
                            elif(onda_1_1_t == 4):
                                return 4
                        #2
                        elif(ciclo_1_2 == 2):
                            if(onda_1_2_t == 1):
                                return 1
                            elif(onda_1_2_t == 2):
                                return 2
                            elif(onda_1_2_t == 3):
                                return 3
                            elif(onda_1_2_t == 4):
                                return 4
                        #3
                        elif(ciclo_1_3 == 2):
                            if(onda_1_3_t == 1):
                                return 1
                            elif(onda_1_3_t == 2):
                                return 2
                            elif(onda_1_3_t == 3):
                                return 3
                            elif(onda_1_3_t == 4):
                                return 4
                        #4
                        elif(ciclo_1_4 == 2):
                            if(onda_1_4_t == 1):
                                return 1
                            elif(onda_1_4_t == 2):
                                return 2
                            elif(onda_1_4_t == 3):
                                return 3
                            elif(onda_1_4_t == 4):
                                return 4
                        #5
                        elif(ciclo_1_5 == 2):
                            if(onda_1_5_t == 1):
                                return 1
                            elif(onda_1_5_t == 2):
                                return 2
                            elif(onda_1_5_t == 3):
                                return 3
                            elif(onda_1_5_t == 4):
                                return 4
                        #6
                        elif(ciclo_1_6 == 2):
                            if(onda_1_6_t == 1):
                                return 1
                            elif(onda_1_6_t == 2):
                                return 2
                            elif(onda_1_6_t == 3):
                                return 3
                            elif(onda_1_6_t == 4):
                                return 4
                t_atual = tipo_atual(int())
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
                        print("Selecione a quantidade de vezes que a Seção", section_ciclo, "irá repetir")
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
                        print("Selecione a quantidade de vezes que a a Onda:", o_atual,"da Seção", section_ciclo, "será repetida")
                        estado_config = 3
                    #Remover
                    elif(comecar == "o-") or (comecar == "O-"):
                        print("Selecione alguma onda para ser deletada")
                        estado_config = 4
                    #Comprimenoto
                    elif(comecar == "T") or (comecar == "t"):
                        print("Selecione o tamanho da Onda", o_atual, "Seção:",section_ciclo)
                        estado_config = 5
                    #Altura
                    elif(comecar == "a") or (comecar == "A"):
                        print("Selecione a altura final da Onda:", o_atual, "Seção", section_ciclo)
                        estado_config = 6
                    #Suavidade
                    elif(comecar == "S") or (comecar == "s"):
                        print("Selecione a suavidade da Onda[S|N]:", o_atual, "Seção", section_ciclo)
                        estado_config = 7
                    #Espaçamento
                    elif(comecar == "e") or (comecar == "E"):
                        print("Selecione o espaçamento da Onda:", o_atual, "Seção", section_ciclo)
                        estado_config = 8
                    #Números
                    #Multiplos mútuos
                    elif(comecar == "N m") or (comecar == "n M") or (comecar == "n m"):
                        print("Número a ser multiplicado por si mesmo, equivalente a x^2, da Onda", o_atual, "Seção",  section_ciclo)
                        estado_config = 9
                    #Fatores
                    #Fator1
                    elif(comecar == "N1") or (comecar == "n1"):
                        if(t_atual == 1):
                            print("Selecione o multiplo 1 da Onda", o_atual, "Seção", section_ciclo)
                        elif(t_atual == 2):
                            print("Selecione o dividendo da Onda", o_atual, "Seção", section_ciclo)
                        elif(t_atual == 3):
                            print("Selecione a base da Onda", o_atual, "Seção", section_ciclo)
                        elif(t_atual == 4):
                            print("Selecione o radicando da Onda", o_atual, "Seção", section_ciclo)
                        estado_config = 10
                    #Fator 2
                    elif(comecar == "N2") or (comecar == "n2"):
                        if(t_atual == 1):
                            print("Selecione o multiplo 2 da Onda", o_atual, "Seção", section_ciclo)
                        elif(t_atual == 2):
                            print("Selecione o divisor da Onda", o_atual, "Seção", section_ciclo)
                        elif(t_atual == 3):
                            print("Selecione o expoente da Onda", o_atual, "Seção", section_ciclo)
                        elif(t_atual == 4):
                            print("Selecione o índice da Onda", o_atual, "Seção", section_ciclo)
                        estado_config = 11
                    #Listagem
                    #Local
                    elif(comecar == "L") or (comecar == "l"):
                        print("Lista das configurações da Onda", o_atual, "Seção", section_ciclo)
                        if(section_ciclo == 1):
                            print("\n", "==============")
                            if(repet_sectio_1>1):
                                print("Seção 1 repete", repet_sectio_1, "vezes")
                            else:
                                print("Seção 1 repete", repet_sectio_1, "vez")
                            print("\n")
                            #1
                            if(ciclo_1_1 == 2):
                                if(onda_1_1_t<1) or (onda_1_1_t>quant_tipo):
                                    print("Onda 1 | Modelo inválido")
                                else:
                                    print("Onda 1 | Tipo:", onda_1_1_t)
                                print("Tamanho:",quant_dej_dir_1_1,"\n","Espaçamento:",esp_des_1_1)
                                if(onda_1_1_t != 2) and (onda_1_1_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_1)
                                print("Altura final:", rigth_armazenada_1_1)
                                if(onda_1_1_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_1, "\n","2",fator2_1_1)
                                elif(onda_1_1_t == 2):
                                    print("Dividendo:",fator1_1_1,"\n","Divisor:", fator2_1_1)
                                elif(onda_1_1_t == 3):
                                    print("Base:", fator1_1_1,"\n","Expoente:", fator2_1_1,)
                                elif(onda_1_1_t == 4):
                                    print("Radicando:", fator1_1_1, "\n","Índice:", fator2_1_1)
                                else:
                                    print("Erro")
                                print("Suavidade:",sua_1_1,"\n","Repetição:", repet_ciclo_1_1, "\n")
                            #2
                            elif(ciclo_1_2 == 2):
                                if(onda_1_2_t<1) and (onda_1_2_t>quant_tipo):
                                    print("Onda 2 | Modelo inválido")
                                else:
                                    print("Onda 2 | Tipo:", onda_1_2_t)
                                print("Tamanho:", quant_dej_dir_1_2, "\n", "Espaçamento:", esp_des_1_2)
                                if(onda_1_2_t != 2) and (onda_1_2_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_2)
                                print("Altura final:", rigth_armazenada_1_2)
                                if(onda_1_2_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_2, "\n","2",fator2_1_2)
                                elif(onda_1_2_t == 2):
                                    print("Dividendo:",fator1_1_2,"\n","Divisor:", fator2_1_2)
                                elif(onda_1_2_t == 3):
                                    print("Base:", fator1_1_2,"\n","Expoente:", fator2_1_2)
                                elif(onda_1_2_t == 4):
                                    print("Radicando:", fator1_1_2, "\n","Índice:", fator2_1_2)
                                else:
                                    print("Erro")
                                print("Suavidade:",sua_1_2, "\n","Repetição:", repet_ciclo_1_2, "\n")
                            #3
                            elif(ciclo_1_3 == 2):
                                if(onda_1_3_t<1) or (onda_1_3_t>quant_tipo):
                                    print("Onda 3 | Modelo inválido")
                                else:
                                    print("Onda 3 | Tipo:", onda_1_3_t)
                                print("Tamanho:",quant_dej_dir_1_3,"\n","Espaçamento:",esp_des_1_3)
                                if(onda_1_3_t != 2) and (onda_1_3_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_3)
                                print("Altura final:", rigth_armazenada_1_3)
                                if(onda_1_3_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_3, "\n","2",fator2_1_3)
                                elif(onda_1_3_t == 2):
                                    print("Dividendo:",fator1_1_3,"\n","Divisor:", fator2_1_3)
                                elif(onda_1_3_t == 3):
                                    print("Base:", fator1_1_3,"\n","Expoente:", fator2_1_3)
                                elif(onda_1_3_t == 4):
                                    print("Radicando:", fator1_1_3, "\n","Índice:", fator2_1_3)
                                else:
                                    print("Erro")
                                print("Suavidade:",sua_1_3,"\n","Repetição:",repet_ciclo_1_3, "\n")
                            #4
                            elif(ciclo_1_4 == 2):
                                if(onda_1_4_t<1) or (onda_1_4_t>quant_tipo):
                                    print("Onda 4 | Modelo inválido")
                                else:
                                    print("Onda 4 | Tipo:", onda_1_4_t)
                                print("Tamanho:", quant_dej_dir_1_4, "\n","Espaçamento:", esp_des_1_4,)
                                if(onda_1_4_t != 2) and (onda_1_4_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_4)
                                print("Altura final:", rigth_armazenada_1_4)
                                if(onda_1_4_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_4, "\n","2",fator2_1_4)
                                elif(onda_1_4_t == 2):
                                    print("Dividendo:",fator1_1_4,"\n","Divisor:", fator2_1_4)
                                elif(onda_1_4_t == 3):
                                    print("Base:", fator1_1_4,"\n","Expoente:", fator2_1_4)
                                elif(onda_1_4_t == 4):
                                    print("Radicando:", fator1_1_4, "\n","Índice:", fator2_1_4)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_4, "\n","Repetição:", repet_ciclo_1_4, "\n")
                            #5
                            elif(ciclo_1_5 == 2):
                                if(onda_1_5_t<1) or (onda_1_5_t>quant_tipo):
                                    print("Onda 5 | Modelo inválido")
                                else:
                                    print("Onda 5 | Tipo:", onda_1_5_t)
                                print("Tamanho:", quant_dej_dir_1_5, "\n", "Espaçamento:", esp_des_1_5,)
                                if(onda_1_5_t != 2) and (onda_1_5_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_5)
                                print("Altura final:", rigth_armazenada_1_5)
                                if(onda_1_5_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_5, "\n","2",fator2_1_5)
                                elif(onda_1_5_t == 2):
                                    print("Dividendo:",fator1_1_5,"\n","Divisor:", fator2_1_5)
                                elif(onda_1_5_t == 3):
                                    print("Base:", fator1_1_5,"\n","Expoente:", fator2_1_5)
                                elif(onda_1_5_t == 4):
                                    print("Radicando:", fator1_1_5, "\n","Índice:", fator2_1_5)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_5, "\n","Repetição:", repet_ciclo_1_5, "\n")
                            #6
                            elif(ciclo_1_6 == 2):
                                if(onda_1_6_t<1) or (onda_1_6_t>quant_tipo):
                                    print("Onda 6 | Modelo inválido")
                                else:
                                    print("Onda 6 | Tipo:", onda_1_6_t)
                                print("Tamanho:", quant_dej_dir_1_6, "\n", "Espaçamento:", esp_des_1_6,)
                                if(onda_1_6_t != 2) and (onda_1_6_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_6)
                                print("Altura final:",rigth_armazenada_1_6)
                                if(onda_1_6_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_6, "\n","2",fator2_1_6)
                                elif(onda_1_6_t == 2):
                                    print("Dividendo:",fator1_1_6,"\n","Divisor:", fator2_1_6)
                                elif(onda_1_6_t == 3):
                                    print("Base:", fator1_1_6,"\n","Expoente:", fator2_1_6)
                                elif(onda_1_6_t == 4):
                                    print("Radicando:", fator1_1_6, "\n","Índice:", fator2_1_6)
                                else:
                                    print("Erro")
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
                            print("\n")
                            #1
                            if(quant_dej_dir_1_1 != 0):
                                if(onda_1_1_t<1) or (onda_1_1_t>quant_tipo):
                                    print("Onda 1 | Modelo inválido")
                                else:
                                    print("Onda 1 | Tipo:", onda_1_1_t)
                                print("Tamanho:",quant_dej_dir_1_1,"\n","Espaçamento:",esp_des_1_1)
                                if(onda_1_1_t != 2) and (onda_1_1_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_1)
                                print("Altura final:", rigth_armazenada_1_1)
                                if(onda_1_1_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_1, "\n","2",fator2_1_1)
                                elif(onda_1_1_t == 2):
                                    print("Dividendo:",fator1_1_1,"\n","Divisor:", fator2_1_1)
                                elif(onda_1_1_t == 3):
                                    print("Base:", fator1_1_1,"\n","Expoente:", fator2_1_1,)
                                elif(onda_1_1_t == 4):
                                    print("Radicando:", fator1_1_1, "\n","Índice:", fator2_1_1)
                                else:
                                    print("Erro")
                                print("Suavidade:",sua_1_1,"\n","Repetição:", repet_ciclo_1_1, "\n")
                            #2
                            if(quant_dej_dir_1_2 != 0):
                                if(onda_1_2_t<1) or (onda_1_2_t>quant_tipo):
                                    print("Onda 2 | Modelo inválido")
                                else:
                                    print("Onda 2 | Tipo:", onda_1_2_t)
                                print("Tamanho:", quant_dej_dir_1_2, "\n", "Espaçamento:", esp_des_1_2)
                                if(onda_1_2_t != 2) or (onda_1_2_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_2)
                                print("Altura final:", rigth_armazenada_1_2)
                                if(onda_1_2_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_2, "\n","2",fator2_1_2)
                                elif(onda_1_2_t == 2):
                                    print("Dividendo:",fator1_1_2,"\n","Divisor:", fator2_1_2)
                                elif(onda_1_2_t == 3):
                                    print("Base:", fator1_1_2,"\n","Expoente:", fator2_1_2)
                                elif(onda_1_2_t == 4):
                                    print("Radicando:", fator1_1_2, "\n","Índice:", fator2_1_2)
                                else:
                                    print("Erro")
                                print("Suavidade:",sua_1_2, "\n","Repetição:", repet_ciclo_1_2, "\n")
                            #3
                            if(quant_dej_dir_1_3 != 0):
                                if(onda_1_3_t<1) or (onda_1_3_t>quant_tipo):
                                    print("Onda 3 | Modelo inválido")
                                else:
                                    print("Onda 3 | Tipo:", onda_1_3_t)
                                print("Tamanho:",quant_dej_dir_1_3,"\n","Espaçamento:",esp_des_1_3)
                                if(onda_1_3_t != 2) and (onda_1_3_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_3)
                                print("Altura final:", rigth_armazenada_1_3)
                                if(onda_1_3_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_3, "\n","2",fator2_1_3)
                                elif(onda_1_3_t == 2):
                                    print("Dividendo:",fator1_1_3,"\n","Divisor:", fator2_1_3)
                                elif(onda_1_3_t == 3):
                                    print("Base:", fator1_1_3,"\n","Expoente:", fator2_1_3)
                                elif(onda_1_3_t == 4):
                                    print("Radicando:", fator1_1_3, "\n","Índice:", fator2_1_3)
                                else:
                                    print("Erro")
                                print("Suavidade:",sua_1_3,"\n","Repetição:",repet_ciclo_1_3, "\n")
                            #4
                            if(quant_dej_dir_1_4 != 0):
                                if(onda_1_4_t<1) or (onda_1_4_t>quant_tipo):
                                    print("Onda 4 | Modelo inválido")
                                else:
                                    print("Onda 4 | Tipo:", onda_1_4_t)
                                print("Tamanho:", quant_dej_dir_1_4, "\n","Espaçamento:", esp_des_1_4,)
                                if(onda_1_4_t != 2) and (onda_1_4_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_4)
                                print("Altura final:", rigth_armazenada_1_4)
                                if(onda_1_4_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_4, "\n","2",fator2_1_4)
                                elif(onda_1_4_t == 2):
                                    print("Dividendo:",fator1_1_4,"\n","Divisor:", fator2_1_4)
                                elif(onda_1_4_t == 3):
                                    print("Base:", fator1_1_4,"\n","Expoente:", fator2_1_4)
                                elif(onda_1_4_t == 4):
                                    print("Radicando:", fator1_1_4, "\n","Índice:", fator2_1_4)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_4, "\n","Repetição:", repet_ciclo_1_4, "\n")
                            #5
                            if(quant_dej_dir_1_5 != 0):
                                if(onda_1_5_t<1) or (onda_1_5_t>quant_tipo):
                                    print("Onda 5 | Modelo inválido")
                                else:
                                    print("Onda 5 | Tipo:", onda_1_5_t)
                                print("Tamanho:", quant_dej_dir_1_5, "\n", "Espaçamento:", esp_des_1_5,)
                                if(onda_1_5_t != 2) and (onda_1_5_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_5)
                                print("Altura final:", rigth_armazenada_1_5)
                                if(onda_1_5_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_5, "\n","2",fator2_1_5)
                                elif(onda_1_5_t == 2):
                                    print("Dividendo:",fator1_1_5,"\n","Divisor:", fator2_1_5)
                                elif(onda_1_5_t == 3):
                                    print("Base:", fator1_1_5,"\n","Expoente:", fator2_1_5)
                                elif(onda_1_5_t == 4):
                                    print("Radicando:", fator1_1_5, "\n","Índice:", fator2_1_5)
                                else:
                                    print("Erro")
                                print("Suavidade:", sua_1_5, "\n","Repetição:", repet_ciclo_1_5, "\n")
                            #6
                            if(quant_dej_dir_1_6 != 0):
                                if(onda_1_6_t<1) or (onda_1_6_t>quant_tipo):
                                    print("Onda 6 | Modelo inválido")
                                else:
                                    print("Onda 6 | Tipo:", onda_1_6_t)
                                print("Tamanho:", quant_dej_dir_1_6, "\n", "Espaçamento:", esp_des_1_6,)
                                if(onda_1_6_t != 2) and (onda_1_6_t != 4):
                                    print("Altura inicial:", r_init_armazenada_1_6)
                                print("Altura final:",rigth_armazenada_1_6)
                                if(onda_1_6_t == 1):
                                    print("Fatores:","\n", "1:", fator1_1_6, "\n","2",fator2_1_6)
                                elif(onda_1_6_t == 2):
                                    print("Dividendo:",fator1_1_6,"\n","Divisor:", fator2_1_6)
                                elif(onda_1_6_t == 3):
                                    print("Base:", fator1_1_6,"\n","Expoente:", fator2_1_6)
                                elif(onda_1_6_t == 4):
                                    print("Radicando:", fator1_1_6, "\n","Índice:", fator2_1_6)
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
                        print("Selecione a altura inicial da Onda", o_atual, "Seção", section_ciclo)
                        estado_config = 12
                    #Tipo
                    elif(comecar == "mo") or (comecar == "Mo"):
                        print("Selecione o modelo da onda", o_atual, "Seção", section_ciclo)
                        estado_config = 13
                    #Ajuda
                    elif(comecar == "h") or (comecar == "H"):
                        print("\n", "~~Comandos~~","\n","'T/t' --> Define o tamanho(vertical) da onda", "\n", "'A/a' --> Define a altura(tamanho horizontal) final da onda", "\n", "'Ai/ai' --> Define a altura(tamanho horinzontal) inicial da onda.","\n" ,"Nota: o ai é indisponível nos tipos d e ra", "\n", "'E/e' --> Define o espaçamento da onda", "\n", "'S/s' --> Define a suavidade das ondas", "\n", "'N1/n1' --> 1º valor de entrada da onda", "\n", "'N2/n2' --> 2º valor de entrada da onda", "\n", "Nota: a função do N1 varia dependendo do tipo de onda.", "\n", "'Mo/mo --> seleciona o modelo da onda'","\n", "\n","Nota: comandos para atribuir tipos a sua onda:", "\n", "'m/M' --> Multiplicaçãp", "\n", "d/D --> Divisão", "\n", "'ex/Ex' --> Exponenciação", "\n", "'ra/RA' --> Radiciação","\n", "\n","'O/o[1-6]' --> Seleciona a onda que irá configurar", "\n", "'Or/or' --> Define quantas vezes a onda atual irá repetir", "\n", "O-/o- --> Seleciona a onda que será deletada", "\n", "'Str/str' --> Define quantas vezes o padrão atual irá repetir","\n", "'L/l' --> Lista as configurações da onda atual", "\n", "'Lg/lg' --> Lista as configurações de todas as ondas que, teoricamente, rodarão e funcionarão durante a execução do projeto","\n","'F/f' --> finaliza as configurações", "\n", "\n",)
                    #Erro
                    else:
                        print("Inválido, tente novamente")
                else:
                    if(estado_config != 7) and (estado_config != 13) and (estado_config != 14):
                        comecar = input("")
                        try:
                            comecar = int(comecar)
                        except:
                            coemcar = str(comecar)
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
                                elif(t == "ex") or (t == "Ex"):
                                    return 3
                                elif(t == "ra") or (t == "Ra") or (t == "RA"):
                                    return 4
                                else:
                                    print("Modelo de onda inválido, altere-a para não ocorre erros")
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
                            #Salavemento de estado
                            if(o_atual == 1):
                                e_ant = 1
                            elif(o_atual == 2):
                                e_ant = 2
                            elif(o_atual == 3):
                                e_ant = 3
                            elif(o_atual == 4):
                                e_ant = 4
                            elif(o_atual == 5):
                                e_ant = 5
                            elif(o_atual == 6):
                                e_ant = 6
                            configuracoes = 0
                    else:
                        if not type(comecar) is int:
                            print("Por favor, não insira qualquer besteira, e sim números de concreto, isto é, números concretos(inteiros e postivos) XD")
                        elif(comecar<0):
                            print("Por favor, não insira valores negativos")
                        elif(comecar == 0):
                            print("Eitanois! Não coloque, em hípotese alguma, algum valor aqui igual a 0!")
                    estado_config = 1
                entra = entra+1
        if(ativador != 1):
            comecar = str(input("* "))
        if(comecar == "config"):
            configuracoes = 1
        elif(comecar == "C") or (comecar == "c"):
            ativador = 1
            comecar = None
            break
        else:
            if(comecar != None):
                print("Inválido, digite novamente, algo válido dsta vez, hein!")
        #Execução   
        while(ativador == 1) and (comecar == None):
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
                            return quant_dej_dir_1_6
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
                #Raízes
                casas_aparecidadas = 1
                #Suavidade
                pro_ro = pro_ro_armazenamento
                contagem_esp = 0
                quant = 0
                rigth = 0
                rigth_tot = 0
                #X
                X = fator1_armazenado
                #Armazenadores
                armazenador_x = 1
                armazenador_x_2 = 0
                #Coração do sistema
                try:
                    while(quant<quant_dej_dir):
                        #Onda
                        #Altura total
                        def r_t(rt):
                            if(tipo == 1):
                                return fator1*(fator2**rigth_armazenada)
                            elif(tipo == 2) and (tipo == 4):
                                return rigth_armazenada
                            elif(tipo == 3):
                                return fator1**(fator2**rigth_armazenada)
                            elif(tipo == 4): #and (decimal == 0)
                                return 1
                                #return fator1**(1/(fator2**rigth_armazenada))
                            else:
                                return rigth_armazenada
                        rigth_tot = r_t(int())
                        #Proporção
                        def porpor(proporcao):
                            if(tipo == 1) or (tipo == 3):
                                proporcao = rigth_desj/quant_dej_dir
                            elif(tipo == 2) or (tipo == 4):
                                x = rigth_tot+1
                                proporcao = 1
                                rigth = 1
                                while(x>rigth_tot):
                                    if(tipo == 2):
                                        x = fator1/(fator2**rigth*proporcao)
                                    else:
                                        x = fator1**(1/(fator2**rigth*proporcao))
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
                            if(tipo != 2) and (tipo != 4):
                                quant_dej_dir = rigth_desj
                            else:
                                rigth_desj = quant_dej_dir
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
                                rigth_a = rigth+1
                                if(tipo == 1):
                                    return (fator1*fator21**rigth_inical)*(fator2**rigth_a*proporcao)
                                elif(tipo == 2):
                                    return fator1/(fator2**(rigth_a*proporcao))
                                elif(tipo == 3):
                                    return fator1**(fator2**rigth_a*proporcao)
                                elif(tipo == 4):
                                    return fator1**((1/fator2)**rigth_a*proporcao)
                            armazenador_x_fut = ar_fut(int())
                            #Inicializador
                            if(quant<=0) and (rigth_inical == 1):
                                print(int(fator1))
                            #Ondinhas
                            def ondas(x):
                                #Multiplicação
                                if(tipo == 1):
                                    if(rigth_desj>rigth) and (armazenador_x_fut<rigth_tot):
                                        return (x*fator21**rigth_inical)*(fator2**  (rigth*proporcao))
                                    else:
                                        return rigth_tot
                                #Divisão
                                elif(tipo == 2):
                                    if(rigth<=rigth_desj) and (armazenador_x_fut>=rigth_tot) :
                                        return x/(fator2**(proporcao*rigth))
                                    elif(armazenador_x_fut<rigth_tot) or (rigth_desj<=rigth):
                                        return rigth_tot
                                #Potenciação
                                elif(tipo == 3):
                                    if(rigth<=rigth_desj) and (armazenador_x_fut<rigth_tot):
                                        return (x*fator21**rigth_inical)**(fator2**rigth*proporcao)
                                    else:
                                        return rigth_tot
                                elif(tipo == 4):
                                    if(rigth<=rigth_desj) and (armazenador_x_fut>rigth_armazenada):
                                        return x**(1/(fator2**rigth*proporcao))
                                    else:
                                        return rigth_armazenada
                            if(tipo != 4):
                                X = int(ondas(fator1))
                            else:
                                X = float(ondas(fator1))
                            #Exibirdores
                            #Suave
                            if(pro_ro == 1):
                                if(tipo != 4):
                                    if(quant % esp_des == 0) and (quant!= 0) or (quant!=quant_dej_dir-1):
                                        esp = 0
                                        while(esp<esp_des):
                                            if(modo_ds == 1):
                                                print("Q",quant,"E",contagem_esp_armazenamento, X)
                                            else:
                                                print(int(X))
                                            contagem_esp = 1
                                            contagem_esp_armazenamento = contagem_esp +contagem_esp_armazenamento
                                            esp = esp+1
                                    else:
                                        print(X)
                                else:
                                    if(quant % esp_des == 0) and (quant!= 0) or (quant!=quant_dej_dir-1):
                                        esp = 0
                                        while(esp<esp_des):
                                            if(modo_ds == 1):
                                                print("Q",quant,"E",contagem_esp_armazenamento, X)
                                            else:
                                                print(int(X))
                                            # if(tipo != 4) and (decimal == 0):
                                            #     print(X)
                                            # else:
                                            #     if(X>2):
                                            #         print(int(X))
                                            #     else:
                                            #         y = Decimal(X)
                                            #         print(round(y,casas_aparecidadas))
                                            #         if(casas_aparecidadas<27):
                                            #             casas_aparecidadas += 1
                                            contagem_esp = 1
                                            contagem_esp_armazenamento = contagem_esp +contagem_esp_armazenamento
                                            esp = esp+1
                                    if(armazenador_x_fut<=rigth_desj):
                                        if(para == 0):
                                            quant = quant_dej_dir-uns_desj
                                            rigth = rigth_desj-uns_desj
                                        print(int(X))
                                        para = 1
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
                                if(tipo == 4) and (armazenador_x_fut>rigth_desj):
                                    if(tipo == 4):
                                        if(para == 0):
                                            quant = quant_dej_dir-uns_desj
                                            rigth = rigth_desj-uns_desj
                                        print(int(X))
                                        para = 1
                            contador -= 1
                            quant += 1
                            rigth += 1
                    ciclo += 1
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
                        #2
                        elif(repetidor<=repet_ciclo_1_2) and (depois == 2):
                            if(modo_ds == 1):
                                print("Certo2", "R2", repet_ciclo_1_2, "Rep", repetidor,    "\n""Q",      quant_dej_dir_1_2)
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
                        #6
                        elif(repetidor<=repet_ciclo_1_6) and (depois == 6):
                            if(modo_ds == 1):
                                print("Certo6", "R6", repet_ciclo_1_6, "Rep", repetidor)
                            repetidor = repetidor+1
                            if(repetidor == repet_ciclo_1_6):
                                ciclo_1_1 = 1
                                ciclo_1_6 = 0
                        repetidor = 0
                except ValueError:
                    print("Deu ruim! Chame o Desenvolvedor!!! Um número estourou o sistema!")
                    break
                except TypeError:
                    print("O que aconteceu aqui???!!! Alguém colcocou o que não devera no lugar errado!")
                    break
                except:
                    print("Seja o que ocorreu aqui.. Chamem o DS!!!")
                    break
            #Seções
            repetidor_se += 1
            if(repetidor_se == repet_sectio_1) and (section_ciclo == 1):
                ativador = 0
            if(modo_ds == 1):
                print("RepS", repet_sectio_1, "Repp", repetidor_se)
            depois=1
        if(comecar == None):
            vezes = vezes+1
            # print("V", vezes)
            text = 1
#Coisas para mexer aqui:
#4- Integra cálculo as ondas 
#8- Otimização