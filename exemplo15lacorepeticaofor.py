print("Videoaulas Neri sobre Python")
print("Acesse www.informaticon.com.br email=videoaulaneri@gmail.com")
print("------------------------------------------------------------")

for numeros in "0123456789":
    print("Numero.:",numeros)
else:
    print("Fim")

for numeros in range(10):
    print("Numero.:",numeros)
    if numeros >6:
        break
else:
    print("Fim")

for nomes in ["Neri", "Giulia", "Gustavo", "Lisiane"]:
    print("Nomes.:",nomes)
else:
    print("Fim nomes")

dadostupla = [("a","b"),("c","d"),("d","f")]
for(alf1, alf2) in dadostupla:
    print(alf1,alf2)

for numeros in range(20,30,2):
    if numeros == 25:
        continue
    print("Numero.:",numeros)
else:
    print("Fim")

for numeros in range(50,40,-1):
    print("Numero.:",numeros)
else:
    print("Fim")

for numeros in range(-6, 6):
    print("Numero.:",numeros)
else:
    print("Fim")

numerotabuada = int(input("Digite um numero para tabuada.: "))
for tabuada in range(1, 11):
    print(" %d * %d = %d" % (numerotabuada,  tabuada, (numerotabuada*tabuada)))

somatotal=0
for soma in range(1,12):
    somatotal += soma 
    
print("A soma é %d" %somatotal)