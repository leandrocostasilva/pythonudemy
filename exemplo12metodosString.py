print("Videoaulas Neri sobre Python")
print("Acesse www.informaticon.com.br email=videoaulaneri@gmail.com")
print("------------------------------------------------------------")

dados=['Neri', 'Lisiane', 'Giulia', 'Gustavo']
print(dados)
print("-".join(dados))
print("\n".join(dados))
print("**************".join(dados))

palavra="neri"
print("ljust =", palavra.ljust(30))
print("rjust =", palavra.rjust(30))
print("partition, divide a string em uma tupla com 3 elementos ", "neri aldoir neitske".partition("aldoir"))
print("partition, divide a string em uma tupla com 3 elementos ", "xyz".partition("y"))
print("partition, divide a string em uma tupla com 3 elementos ", "xyzxyz".partition("y"))
print("partition, divide a string em uma tupla com 3 elementos ", "neri aldoir neitske".partition("neri"))
print("partition, divide a string em uma tupla com 3 elementos ", "xyz".partition("x"))
print("rpartition, divide a string em uma tupla com 3 elementos ", "neri aldoir neitske".partition("aldoir"))
print("rpartition, divide a string em uma tupla com 3 elementos ", "xyz".rpartition("y"))
print("rpartition, divide a string em uma tupla com 3 elementos ", "neri aldoir neitske".rpartition("neri"))
print("rpartition, divide a string em uma tupla com 3 elementos ", "xyz".rpartition("x"))
print("rpartition, divide a string em uma tupla com 3 elementos ", "xyzxyz".rpartition("x"))
print("split-> divide a string em uma lista: ", "Neri Aldoir Neitzke".split())
print("rsplit-> divide a string em uma lista: ", "Neri Aldoir Neitzke".rsplit())
print("split-> divide a string em uma lista: ", "Neri;Aldoir;Neitzke".split(";"))
print("rsplit-> divide a string em uma lista: ", "Neri;Aldoir;Neitzke".rsplit(";"))