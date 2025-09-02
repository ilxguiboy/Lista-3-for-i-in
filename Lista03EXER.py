# Execio 1
# somaPos=0
# contaNeg=0
# for i in range(20):
#     valor=int(input("Digiti o valor: "))
#     if valor>=0:
#         somaPos+=valor
#     else:
#         contaNeg+=1
#  print("A soma dos numeros positivo é ",somaPos)
#  print("A quantidade dos numeros negativo é ",contaNeg)             

# Execio 2
# for i in range (100,201):
#     if i%2!=0:
#         print(i)

# Execio 3
# somaNum=0
# numero=int(input("Digite um numero inteiro: "))
# for i in range(1,numero+1):
#     somaNum+=i
# print("A soma dos numeros entre 1 e ",numero," é ",somaNum)    

# Execio 4
# somaAltura=0
# qtdeJog=int(input("Digite a quantidade de jogadores: "))
# for i in range(qtdeJog):
#     altura=float(input("Digite a altura do jogador: "))
#     somaAltura+=altura
#     media=somaAltura/qtdeJog
# print("A media de altura dos jogadores é ",media)

# Execio 5
# for i in range(1,51):
#     if i%2==0:
#         print(i)

# Execio 6
# maiorMedia=0
# menorMedia=999
# qtdeAp=0
# qtdeRP=0
# for i in range(10):
#     nota1=float(input("Digite a primeira noata: "))
#     nota2=float(input("Digite a segunda noata: "))
#     nota3=float(input("Digite a terceira noata: "))
#     media=(nota1+nota2+nota3)/3
#     if media>maiorMedia:
#         maiorMedia=media
#     if media<menorMedia:
#         menorMedia=media     
#         if media>=6:
#             qtdeAp+=1
#         else:
#             qtdeRP+=1
# print("A maior media foi" ,maiorMedia)     
# print("A menor media foi", menorMedia)   
# print("A quantidade de alunos aprovados foi ",qtdeAp)    
# print("A quantidade de alunos reprovados foi ",qtdeRP)    

# Execio 7
# Thanos=1.50
# Miranha=1.10
# for i in range (1000):
#     if Miranha>Thanos:
#         break
#     Thanos+=0.02
#     Miranha+=0.03
# print("Vai demorar ",i," anos para que o Homem Aranha seja maior que o Thanos!")

# Execio 8
# numero=int(input("Digite um numero: "))
# fatorial=1
# for i in range (1,numero+1):
#     fatorial*=i
# print(numero, "! = ",fatorial)