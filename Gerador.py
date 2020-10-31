try:
    import os
    import random
    from time import sleep
except Exception:
    import os
    import random
    from time import sleep

logo = r"""

   ********                                **                
  **//////**                              /**                
 **      //   *****  ******  ******       /**  ******  ******
/**          **///**//**//* //////**   ****** **////**//**//*
/**    *****/******* /** /   *******  **///**/**   /** /** / 
//**  ////**/**////  /**    **////** /**  /**/**   /** /**   
 //******** //******/***   //********//******//****** /***   
  ////////   ////// ///     ////////  //////  //////  ///    

    **            ****            ******    ****** 
    /**           /**/            **////**  **////**
    /** *******  ******  ******  **    //  **    // 
    /**//**///**///**/  **////**/**       /**       
    /** /**  /**  /**  /**   /**/**       /**       
    /** /**  /**  /**  /**   /**//**    **//**    **
    /** ***  /**  /**  //******  //******  //****** 
    // ///   //   //    //////    //////    //////  

       *******                  **                 
       /**////**                /**                 
       /**    /**  ******       /**  ******   ******
       /**    /** //////**   ****** **////** **//// 
       /**    /**  *******  **///**/**   /**//***** 
       /**    **  **////** /**  /**/**   /** /////**
       /*******  //********//******//******  ****** 
       ///////    ////////  //////  //////  //////  
                    @Created BY: hypn0thcy
                           #AoGiri

"""

def menu():
    print('')
    print(r'**************************************')
    print(r'**************************************')
    print(r'**       __  __________   ____  __  **')
    print(r'**      /  |/  / ____/ | / / / / /  **')
    print(r'**     / /|_/ / __/ /  |/ / / / /   **')
    print(r'**    / /  / / /___/ /|  / /_/ /    **')
    print(r'**   /_/  /_/_____/_/ |_/\____/     **')
    print(r'**                                  **')
    print(r'**************************************')
    print(r"**     a -> Gerador Cpf's           **")
    print(r"**     b -> Gerador Info CC'S       **")
    print(r"**     c -> Gerador De Nomes        **")
    print(r"**     s -> Sair                    **")
    print(r'**************************************')
    print(r'**************************************')
    print('')

NamesMasculinosONE = ['lucas', 'vitor', 'joao', 'ricardo', 'daniel', 'victor', 'italo', 'junior', 'amaury', 'jose', 'kauan', 'gustavo']
NamesMasculinosTWO = ['pereia', 'costa', 'santos', 'silva', 'pinheiro', 'fernandes', 'da']
NamesMasculinosTREE = ['alves', 'cunha', 'santos', 'ramos', 'cris', 'camargo']
NamesFemininosONE = ['julia', 'roberta', 'samanta', 'amanda', 'lorena', 'maria', 'larissa', 'cristina', 'elizabete', 'iris']
NamesFemininosTWO = ['santos', 'camargo', 'pereira', 'cristovao', 'alves', 'pinheiro', 'ramos']
NamesFemininosTREE = ['fernandes', 'costas', 'eduarda', 'carmos', 'camargo', 'efigênia']

cpffs = ['072.601.737-00', '659.137.447-72', '077.780.247-30', '102.632.747-48', '517.560.057-53', '104.362.497-07', '054.872.467-93', '116.684.497-81', '535.855.347-91', '071.497.067-03', '141.479.598-06', '003.926.141-70', 
'005.270.580-33', '940.083.967-72', '030.218.016-84', '959.658.238-00', '105.201.218-30', '289.415.038-50', '089.896.317-69', '679.598.066-91', '398.132.388-28',
'776.220.497-00', '108.761.467-87', '163.951.688-35', '011.581.937-18', '923.848.548-87', '148.027.910-20', '297.619.108-57', '330.922.478-33', '259.059.178-09',
'804.880.649-53', '948.586.326-87', '426.829.243-87', '100.889.977-15', '522.845.812-34', '799.600.651-20', '042.246.896-77', '083.980.368-00', '004.248.807-92',
'702.489.311-72', '263.849.358-99', '225.618.238-06', '605.989.997-87', '678.599.848-49', '169.764.601-87', '061.932.598-48', '084.007.907-90', '025.007.127-45', '170.177.878-54']


try:
    os.system('cls')
    print(logo)
    user = str(input(" Qual o Usuàrio ADMIN? -> ")).strip()
    print('')
    passw = str(input("  Qual a Senha ADMIN? -> ")).strip()

    if user.lower() == 'admin@root' and passw.lower() == 'root':
        print('\n      [!] Verificando... [User -> {}, Password -> {}'.format(user, passw))
        sleep(1.5)
        os.system('cls')
        os.system('color 0a')
        print('\n    Usuàrio Autenticado com SUCESSO!')
        input('\n Pressione (ENTER) Para Abrir o MENU! ')
        os.system('cls')
        menu()
        opc = str(input(' Qual Opção Deseja Usar? (LETRA) -> ')).strip()
        if opc == 's':
            os.system('color')
            os.system('color 0')
            sleep(0.3)
            exit()
        elif opc == 'a':
            qntddde = int(input("\nQuantos CPF'S Deseja Gerar? -> "))
            print("\n\n\n CPFS'S:\n")
            for iii in range(0, qntddde):
                cpfs = random.choice(cpffs)
                print(cpfs)
            input('\n            Pressione (ENTER) Para ENCERRAR!           ')
            exit()
        elif opc == 'b':
            arq = str(input("\nQual Nome Do Arquivo? (EX: teste) -> ")).strip()
        
            binn = str(input("\n[?] bin (EX: 43563) -> ")).strip()
            
            dataV = str(input("\n[?] Validade (EX: 05/24) -> ")).strip()
            
            cvv = str(input("\n[?] Validade (EX: 023) -> ")).strip()
            
            qntd = int(input("\n[?] Quantas Unidades Deseja Gerar (EX: 30) -> "))
            with open(f"{arq}.txt", 'w') as escrever:
                for x in range(1, qntd):
                    os.system('cls')
                    listaN = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                    r1 = random.choice(listaN)
                    r2 = random.choice(listaN)
                    r3 = random.choice(listaN)
                    r4 = random.choice(listaN)
                    r5 = random.choice(listaN)
                    r6 = random.choice(listaN)
                    r7 = random.choice(listaN)
                    r8 = random.choice(listaN)
                    r9 = random.choice(listaN)
                    r10 = random.choice(listaN)
                    r11 = random.choice(listaN)

                    binC = binn+'xxxxxxxxxx'
                    dataC = dataV.replace('/', '|')
                    cartaoCVG = binC+'|'+dataC+'|'+cvv

                    
                    cartaoCPTN = f'{binn}{r1}{r2}{r3}{r4}{r5}{r6}{r7}{r8}{r9}{r10}{r11}'
                    
                    result = cartaoCPTN+'|'+dataC+'|'+cvv
                    print('\n Gerando Cartões e Salvando No Arquivo -> {}.txt'.format(arq))
                    escrever.write('@Created BY: hypn0thcy! -> ' + result + '\n')
                    os.system('cls')
            print('\n                       SUCESSO!!')
            input('\n            Pressione (ENTER) Para ENCERRAR!           ')
            exit()
        elif opc == 'c':
            qntddddd = int(input('\nQuantos Nomes Deseja Gerar? -> '))

            print('\n\n\n Nomes Masculinos:\n')
            for i in range(0, qntddddd): 
                nmo = random.choice(NamesMasculinosONE)
                nmot = random.choice(NamesMasculinosTWO)
                nmott = random.choice(NamesMasculinosTREE)

                print(nmo, nmot, nmott)

            print('\n\n\n Nomes Femininos:\n')
            for ii in range(0, qntddddd):
                nmm = random.choice(NamesFemininosONE)
                nmmt = random.choice(NamesFemininosTWO)
                nmmtt = random.choice(NamesFemininosTREE)

                print(nmm, nmmt, nmmtt)
            input('\n            Pressione (ENTER) Para ENCERRAR!           ')
            exit()
        else:
            print("\n Houve Algum Problema, Use A letra Referente à cada opção!")
            bbb = str(input("\n Deseja Tentar Novamente? (s/n) -> ")).strip()
            if bbb == 's':
                menu()
                opp = str(input(' Qual Opção Deseja Usar? (LETRA) -> '))
                if opp == 's' :
                    os.system('color')
                    os.system('color 0')
                    sleep(0.3)
                    exit()
                elif opp == 'a':
                    qntddde = int(input("\nQuantos CPF'S Deseja Gerar? -> "))
                    print("\n\n\n CPFS'S:\n")
                    for iii in range(0, qntddde):
                        cpfs = random.choice(cpffs)
                        print(cpfs)
                    input('\n            Pressione (ENTER) Para ENCERRAR!           ')
                    exit()
                elif opp == 'b':
                    arq = str(input("\nQual Nome Do Arquivo? (EX: teste) -> ")).strip()
        
                    binn = str(input("\n[?] bin (EX: 43563) -> ")).strip()
                    
                    dataV = str(input("\n[?] Validade (EX: 05/24) -> ")).strip()
                    
                    cvv = str(input("\n[?] Validade (EX: 023) -> ")).strip()
                    
                    qntd = int(input("\n[?] Quantas Unidades Deseja Gerar (EX: 30) -> "))
                    with open(f"{arq}.txt", 'w') as escrever:
                        for x in range(1, qntd):
                            os.system('cls')
                            listaN = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                            r1 = random.choice(listaN)
                            r2 = random.choice(listaN)
                            r3 = random.choice(listaN)
                            r4 = random.choice(listaN)
                            r5 = random.choice(listaN)
                            r6 = random.choice(listaN)
                            r7 = random.choice(listaN)
                            r8 = random.choice(listaN)
                            r9 = random.choice(listaN)
                            r10 = random.choice(listaN)
                            r11 = random.choice(listaN)

                            binC = binn+'xxxxxxxxxx'
                            dataC = dataV.replace('/', '|')
                            cartaoCVG = binC+'|'+dataC+'|'+cvv

                            
                            cartaoCPTN = f'{binn}{r1}{r2}{r3}{r4}{r5}{r6}{r7}{r8}{r9}{r10}{r11}'
                            
                            result = cartaoCPTN+'|'+dataC+'|'+cvv
                            print('\n Gerando Cartões e Salvando No Arquivo -> {}.txt'.format(arq))
                            escrever.write('@Created BY: hypn0thcy! -> ' + result + '\n')
                            os.system('cls')
                    print('\n                       SUCESSO!!')
                    input('\n            Pressione (ENTER) Para ENCERRAR!           ')
                    exit()
                elif opp == 'c':
                    qntddddd = int(input('\nQuantos Nomes Deseja Gerar? -> '))
                    print('\n\n\n Nomes Masculinos:\n')
                    for i in range(0, qntddddd): 
                        nmo = random.choice(NamesMasculinosONE)
                        nmot = random.choice(NamesMasculinosTWO)
                        nmott = random.choice(NamesMasculinosTREE)

                        print(nmo, nmot, nmott)

                    print('\n\n\n Nomes Femininos:\n')
                    for ii in range(0, qntddddd):
                        nmm = random.choice(NamesFemininosONE)
                        nmmt = random.choice(NamesFemininosTWO)
                        nmmtt = random.choice(NamesFemininosTREE)

                        print(nmm, nmmt, nmmtt) 
                    input('\n            Pressione (ENTER) Para ENCERRAR!           ')
                    exit()

                else:
                    print("\n Houve Algum Problema, Use A letra Referente à cada opção!")
                    input('\n            Pressione (ENTER) Para ENCERRAR!           ')
                    os.system('color')
                    os.system('color 0')
                    sleep(0.3)
                    exit()
            elif bbb == 'n':
                exit()
            else:
                exit()
    else:
        print('\n      [!] Verificando... [User -> {}, Password -> {}'.format(user, passw))
        sleep(1.2)
        os.system('cls')
        os.system('color 4')
        print('\n         Usuàrio NEGADO!')
        input('\n Pressione (ENTER) Para ENCERRAR! ')
        os.system('color')
        os.system('color 0')
        sleep(0.3)
        exit()
except KeyboardInterrupt:
    input('\n  Pressione (ENTER) Para Fechar! ')
    print("\n          ATÉ MAIS! ^^   ")
    sleep(1)
    exit()
except Exception as yy:
    print("\n Houve Algum Erro CRITICO! -> {}".format(yy))
    sleep(1.5)
    input('\n  Pressione (ENTER) Para Fechar! ')
    exit()
