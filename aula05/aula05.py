candidato = int(input('Informe o numero do candidato\n'))

if(candidato == 13):
    print('Votou no Lula')
elif(candidato == 22):
    print('Votou no Bolsonaro')
else:
    print('Candidato inválido')



    match candidato:
        case 13:
            print('Votou no lula')
        case 22:
            print('votou no Bolsonaro')
        case _:
            print('opção inválida')