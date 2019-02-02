print("Videoaulas Neri sobre Python")
print("Acesse www.informaticon.com.br email=videoaulaneri@gmail.com")
print("------------------------------------------------------------")

#while True:
#    print("laço infinito ... não para nunca")

for numeros in range(1,10):
    print("Numero.:",numeros)
else:
    print("Fim for")

x=1
while x <= 9:
    if x == 3:
        x += 1
        continue
    if x == 8:
        break

    print("Numero.: ", x)
    x += 1
else:
    print("Fim while")

for nomes in ["Neri", "Giulia", "Gustavo", "Lisiane", "Romilda", "Selvino"]:
    print("Nomes.:",nomes)
else:
    print("Fim nomes laço for")

nomes =  ["Neri", "Giulia", "Gustavo", "Lisiane", "Romilda", "Selvino", "Lisete"]
indice = 0
while indice < len(nomes):
    print("Nomes.: ",nomes[indice])
    indice +=1
else:
    print("Fim laço while")

numerotabuada = int(input("Digite um numero para tabuada.: "))

for tabuada in range(1, 10):
    print(" %d * %d = %d" % (numerotabuada,  tabuada, (numerotabuada*tabuada)))
print("Fim tabuada for")

indice=1
while indice <= 9:
    print(" %d * %d = %d" % (numerotabuada,  indice, (numerotabuada*indice)))
    indice+=1
print("Fim tabuada while")