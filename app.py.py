print(30*'-')
print("TESTE DE IMC")
print(30*'_')
input("Digite seu nome: ")
peso=float(input("Informe seu peso: "))
Altura=float(input("Informe sua altura: "))

IMC=peso/Altura**2

Total=round(IMC,2)
print(f'Seu IMC é {Total}.')
print(30*"_")
if Total<=18.5:
    print(30*'-')
    print("ABAIXO DO PESO")
    print(30*'.')
    print("OBS: Busque ajuda física e psicologica.")
    print(30*'.')


elif Total<=24.9:
    print(30*'-')
    print('PESO NORMAL')
    print(30*'.')
    print("OBS:EStá de parabens,é importante cuidar de você")
    print(30*'.')


elif Total<=29.9:
    print(30*'-')
    print("SOBREPESO")
    print(30*'.')
    print("OBS:Cuide um pouco mais de sua saúde!")
    print(30*'.')


elif Total<=34.9:
    print(30*'-')
    print("OBESIDADE 1")
    print(30*'.')
    print("OBS:Cuidado lá esta avançando o estágio")
    print(30*'.')

elif Total<=39.9:
    print(30*'-')
    print("OBESIDADE 2")
    print(30*'.')
    print("OBS:Tome cuidado com sua saúde,para de ser sedentario")
    print(30*'.')


else:
    print('OBESIDADE MÓRBIDA')
    print(30*'-')
    print('OBS:É meu amigo(a), está dificil te ajudar agora,ninguém ta te aguentando.')