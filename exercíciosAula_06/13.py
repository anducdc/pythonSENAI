estacaoAno = int(input('Digite o número correspondente ao mês para retornar a estação do ano:\n'))

if estacaoAno <= 3:
    print('Verão')
    print( """
      *
     ***        \ | /
    *****      -- O --
   *******      / | \ 
  *********
    |||
    |||
    """)
elif estacaoAno >= 9 and estacaoAno < 13:
    print('Primavera')
    print( """
      *
     ***  ~       ~
    *****
   *******    ~
  *********
    |||       (@)  (@)(@)
    |||        |    |  |
    """)
elif estacaoAno > 3 and estacaoAno < 7:
    print('Outono')
    print( """
   _    /__
 __ \  /
   \ || __/_
__\_|  /
    |||
    |||
    """)
elif estacaoAno >=7 and estacaoAno < 9:
    print('Inverno')
    print( """
      *
     ***
    *****              _
   *******           _|_|_
  *********      v   ('>')  v
    |||           \(   o   )/
    |||            (___o___)
    """)
else:
    print('Parâmetro Inválido')