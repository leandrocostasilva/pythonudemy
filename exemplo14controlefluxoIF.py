print("Videoaulas Neri sobre Python")
print("Acesse www.informaticon.com.br email=videoaulaneri@gmail.com")
print("------------------------------------------------------------")

notaaluno=int(input("Digite a nota do aluno.: "))
mediaparapassar=6

if notaaluno >=mediaparapassar:
    print("Aluno aprovado")
    print("Parabéns!")
elif notaaluno >= 4:
    print("Aluno recuperaçao")
    print("Seu burro!")
else:
    print("Aluno reprovado")
    print("Seu burro!")

