import time

# funções
def mostraDiario():
    cont = 1
    print('\n-------DIARIO-------')
    for dica in diario:
        print(str(cont)+" "+dica)
        cont += 1
    
    input("")
        
def mostraInventario():
    
    cont = 1
    print('\n----Inventário----')
    for item in inventario:
        print(str(cont)+" "+item)
        cont += 1
        
    input("")
    
def adicionarDica(dica):
    for dica1 in diario:
        if(dica1 == dica):
            return
    diario.append(dica)

def adicionarInventario(item):
    for item1 in inventario:
        if(item1 == item):
            print('😮 Você já tem o item adicionado!!')
            return
    if (len(inventario) >= quantidade_max_inventario):
        print("Você ja atingiu o limite do inventario.")
        cont = 1
        for item in inventario:
            print(str(cont)+" "+item)
            cont += 1
        res = input('Deseja excluir algum item?s/n\nR: ')
        if(res == 's'):
            nItem = int(input('Digite o número a ser excluido: '))
            inventario.pop(nItem - 1)
            inventario.append(item)
    else:
        inventario.append(item)
    
# cód. principal

inventario = []
diario= []

quantidade_max_inventario = 5   
    
print("\n\n\n\n\n")
print("Você é Natan, um perito criminal de 23 anos, muito reconhecido pelo seu trabalho.")
#time.sleep(2)

print("No dia de hoje, você foi chamado para resolver um caso de assassinato em uma universidade em Curitiba - PR, que não tem um culpado ainda...")
#time.sleep(3)

print("Ao chegar no prédio principal do campus, você tem a sua frente uma larga escadaria, separada em 2 lados por um corrimão no meio.")
#time.sleep(3)

print("Na parte de baixo da escadaria, é possível ver um mural à sua esquerda, com alguns papeis bagunçados. À direita, é possível ver uma porta alta de madeira, com uma pequena placa ao lado.")
#time.sleep(3)

print("Acima da escada, você consegue enxegar duas portas, uma de cada lado da escadaria, iguais à porta vista no andar de baixo.")
#time.sleep(3)

print("Mas o que chama a sua atenção é o que há no pé da escadaria: a vítima. \n")
#time.sleep(2)


while(True):
    print("Você pode:\n"+
        "1- 🪜 Olhar a escadaria\n"+
        "2- 💀 Olhar o corpo\n"+
        "3- 🖼️  Olhar o mural\n"+
        "4- 📘 Olhar as salas\n"+
        "5- Diário e Inventário\n"+
        "6- Dar palpite (você tem apena 1 chance)\n"+
        "7-❌ Sair do programa")
    time.sleep(1)
    
    escolha01 = int(input("Qual ação você deseja tomar?\nR: "))
    time.sleep(1)
    
    while type(escolha01) != int:
        escolha01 = int(input("Qual ação você deseja tomar?\nR: "))


    if(escolha01 == 1):
        time.sleep(1)
        
        print('\nAo observar a escadaria, é possível ver um rastro de algo vermelho, aparentemente sangue, em vários degraus, que parece ter sido interrompido em um certo ponto.')
        time.sleep(1)
        
        escolha01_01 = input('Você quer verificar se é sangue mesmo? s/n \nR: ')
        time.sleep(1)

        if(escolha01_01 == 's'):

            print(".")
            time.sleep(1)
            
            print(".")
            time.sleep(1)
            
            print(".")
            time.sleep(2)
            
            print('\nÉ sangue mesmo.')
            adicionarDica("Há sangue na escadaria")
            time.sleep(1)
            
            print("Você volta para a frente da escada\n")
            time.sleep(1)
        
        

    while(escolha01 == 2):
        
        print("\nVocê se aproxima do corpo jogado no chão.")
        time.sleep(1)

        print("A vítima aparentemente é um estudante, masculino. Próximo ao corpo, jogado no chão, há um galho com uma ponta afiada, se assemelhando a uma flecha, coberto por sangue.")
        time.sleep(2)

        print('\nVocê aproxima no corpo e encontra um pedaço de madeira ao lado coberto de sangue')
        time.sleep(1)

        escolha01_01= int(input('Você deseja investigar o corpo ou o pedaço de madeira?\n'+
                                '1- Corpo\n'+
                                '2- Madeira\n'+
                                '3- Sair\n'+
                                'R:'))
        time.sleep(1)
        
        if(escolha01_01 == 1):
            
            print('Ao analisar o corpo detalhadamente, você nota um ferimento brutal na cabeça da vítima e uma identidade em seu bolso.')
            time.sleep(1)
            
            print('A vítima sofreu um golpe na parte de trás da cabeça, aparentemente com muita força, por um objeto que deixou uma marca roxa bem perceptível, com um pouco de sangue apenas.')
            adicionarDica("A morte foi causada por um objeto sem pontas ou capacidade de corte")
            adicionarInventario("Amostra de sangue (Vitor)")
            time.sleep(1)
            
            escolha01_01_01 = input('Você deseja verificar a identidade? s/n \n'+
                                    'R: ')
            time.sleep(1)
            
            if (escolha01_01_01 == 's'):
                
                print("De acordo com a identidade, esse era Vitor.... ")
                time.sleep(1)
                
                print("Vitor alguma coisa, o resto do nome está coberto com sangue")
                adicionarDica("aparentemente a vítima se chamava Vitor --- ------")
                time.sleep(1)
                
                escolha01_01_01_01= input("Você deseja guardar a identidade com você? s/n")
                time.sleep(1)
                
                if escolha01_01_01_01 == 's':
                    
                    print("Você guarda a identidade no seu bolso")
                    adicionarInventario("Identidade")
                    time.sleep(1)
                    
                if escolha01_01_01_01 == 'n':
                    continue
            
            if(escolha01_01_01 == 'n'):
                continue

            
        if(escolha01_01 == 2):
            
            print("Você observa o pedaço de madeira ao lado do corpo.")
            time.sleep(1)
            
            print("Parece ser um galho qualquer, mas com uma ponta feita propositalmente.")
            adicionarDica("Há um pedaço de madeira pontiagudo com sangue perto do corpo")
            time.sleep(1)
            
            escolha01_01_01 = input('Você deseja pegar o pedaço de madeira? s/n \nR: ')
            time.sleep(1)
            
            if(escolha01_01_01 == 's'):
                
                adicionarInventario("Pedaço de madeira")
                time.sleep(1)
                
                print("Você guarda o pedaço de madeira")
                time.sleep(1)
                
            if escolha01_01_01 == 'n':

                continue
            
        if(escolha01_01 == 3):
            
            print("Você volta para a frente da escada\n")
            time.sleep(1)
            
            break
        
        
    if(escolha01 == 3):
        
        print('🖼️ Você olha o mural e se depara com a seguinte paisagem: '+
            'Um cachorro e uma pessoa')
        time.sleep(1)
        
        escolha01_01 = input('🖼️ Você deseja pegar a imagem como uma dica? s/n \nR: ')
        time.sleep(1)
        
        if(escolha01_01 == 's'):
            
            adicionarInventario("Foto do mural")
            print("Você pega a foto do cachorro e seu dono")
            time.sleep(1)
            
            if "Identidade" in inventario:
                print("A pessoa na foto é a vítima: Vitor")
                adicionarDica("Vitor tem um cachorro")
                time.sleep(1)
                
    while(escolha01 == 4):
        
        print("📘 Você repara que desse saguão é possível ver 3 portas: 2 acima da escadaria e 1 abaixo")
        time.sleep(1)
        
        escolha01_01 = int(input("📘 Qual delas você deseja investigar?\n1- A porta de baixo\n2- A porta de cima à esquerda\n3- A porta de cima à direita\n4- Sair\nR: "))
        time.sleep(1)
        
        if escolha01_01 == 1:
            
            print("📘 Ao lado da porta há uma pequena placa, que diz: Laboratório do curso de farmácia")
            time.sleep(1)

            escolha01_01_01 = input("📘 Deseja entrar? s/n")
            time.sleep(1)

            if escolha01_01_01 == "s":
                
                
                print("Ao entrar na sala você vê um laboratorio comum, com diversos equipamentos.")
                time.sleep(1)
                
                print("Mas um equipamento chama a sua atenção por você já saber o que é:  uma maquina capaz de realizar comparações de DNA")
                time.sleep(1)
                
                escolha01_01_01_01 = input("Deseja utilizar o equipamento? s/n \nR: ")
                time.sleep(1)
                
                if (escolha01_01_01_01 == 's'):

                    if  "Pedaço de madeira" in inventario and "Amostra de sangue (Vitor)" in inventario:

                        print("Ao comparar o sangue no graveto com o sangue na ferida que causou a morte do estudante, você percebe que o sangue no graveto pertence a outra pessoa")
                        adicionarDica("O sangue do graveto não é de Vitor")
                        time.sleep(1)
                        
                    else:

                        print("Você não tem itens suficientes para usar a máquina no momento")
                        time.sleep(1)
                        
            if escolha01_01_01 == 'n':

                print("Você volta para a frente da escada")
                time.sleep(1)
                
        if escolha01_01 == 2:
            
            print("Ao lado da porta há uma pequena placa, que diz: Sala de revelação")
            time.sleep(1)
            
            escolha01_01_01 =input("Deseja entrar? s/n \nR: ")
            time.sleep(1)

            if escolha01_01_01 == "s":
            
                print("A sala de revelação é pequena, iluminada somente por uma luz avermelhada. Dentro dela é possível ver vários recipientes cheios de líquidos diferentes,"+
                    "e alguns equipamentos para auxiliar na revelação de fotos. Logo acima dos equipamentos, há 2 fotos penduradas")
                time.sleep(1)
                
                
                escolha01_01_01_01 = input("Deseja observar as fotos? s/n \nR:")
                time.sleep(1)
                
                if escolha01_01_01_01 == "s":
                    print("Em uma das fotos, é possível ver um estudante andando a caminho de um banco de madeira no canto, e, ao fundo, o prédio principal do campus, no qual você está agora")
                    time.sleep(2)

                    print("A outra imagem parece ter sido tirada alguns segundos após a primeira. Nela é possível ver a mochila do mesmo aluno caindo para trás do banco, logo acima de um pequeno cachorro")
                    time.sleep(1)
                    
                    if "Foto do mural" in inventario:

                        print("O mesmo cachorro que você viu na foto do mural: o cachorro da vítima")
                        time.sleep(1)
                        
                    if "Identidade" in inventario:
                        
                        print("O dono do cachorro é o Vitor")
                        time.sleep(1)
                
                    print("Você volta para a frente da escada")                    
                    time.sleep(1)
                        
            if escolha01_01_01 == "n":
                
                print("Você volta para a frente da escada")
                time.sleep(1)
            
        if escolha01_01 == 3:
            
            print("Ao lado da porta há uma pequena placa, que diz: Laboratório de Mecânica")
            time.sleep(1)
            
            escolha01_01_01 =input("Deseja entrar? s/n")
            time.sleep(1)

            if escolha01_01_01 == "s":
                
                print("O Laboratório de Mecânica é grande, com varios intrumentos de grande e pequeno porte, geralmente utilizados em construção")
                time.sleep(1)

                print("Todos eles estão em grades de ferro, organizados por tamanho.")
                time.sleep(1)

                
                escolha01_01_01_01 = input("Deseja observar a organização dos materias? s/n")
                time.sleep(1)

                if (escolha01_01_01_01 == 's'):
                    
                    print("Você nota que existe uma ficha com as ferramentas da sala e uma coluna para assinaturas\n"+
                            "nela se lê o seguinte: ")
                    time.sleep(1)
                    
                    print("|   Ferramenta    |    Empréstimo   |")
                    print("|-----------------|-----------------|")
                    print("|    Serrote      |      Martin     |")
                    print("|   Furadeira     |      Nicolas    |")
                    print("|    Martelo      |      Mateus     |")
                    print("|                ...                |")
                    time.sleep(2)

                    print("Natan: Foram feitos 3 empréstimos de ferramentas no dia do crime.\n" +
                            "Serrote e furadeira não parecem ser capazes de causar aquele tipo de ferimento...")
                    time.sleep(1)
                    
                    adicionarDica("Arma suspeita: Martelo")
                    
                    escolha01_01_01_01_01 = input("Voce deseja voltar para o corpo ou continuar investigando? \n1- Voltar para o local do crime \n2- Continuar investigando")
                    time.sleep(1)

                    if (escolha01_01_01_01_01 == 1):
                        
                        print("Você volta para o corpo")
                        time.sleep(1)

                    elif (escolha01_01_01_01_01 == 2):
                        
                        print("Você nota que na ficha de estudantes, não há nenhum aluno que não devolveu algum instrumento.")
                        time.sleep(1)

                        print("Dica: um martelo sumiu do Laboratório de Mecânica")
                        adicionarDica("Dica: um martelo sumiu do Laboratório de Mecânica")
                        time.sleep(1)
                    
            if escolha01_01_01 == "n":
                print("Você volta para frente da escada")
                time.sleep(1)

        if escolha01_01 == 4:
            print("Você volta para frente da escada")
            time.sleep(1)

    if escolha01 == 6:
        mostraInventario()
        
    if(escolha01 == 7):        
        break

print("fim do programa. Natan.")
