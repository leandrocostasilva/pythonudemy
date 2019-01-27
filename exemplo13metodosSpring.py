print("Videoaulas Neri sobre Python")
print("Acesse www.informaticon.com.br email=videoaulaneri@gmail.com")
print("------------------------------------------------------------")

dados=['Neri', 'Lisiane', 'Giulia', 'Gustavo']
print(dados)
print("-".join(dados))
print("\n".join(dados))
print("**************".join(dados))

palavra="neri aldoir neitzke"
print("startswitch=retorna verdadeiro se a string inicia com uma substring: ", palavra.startswith("neri"))
print("startswitch=retorna verdadeiro se a string inicia com uma substring: ", palavra.startswith("aneri"))
print("startswitch=retorna verdadeiro se a string inicia com uma substring: ", palavra.startswith("neri"))
print("startswitch=retorna verdadeiro se a string inicia com uma substring: ", palavra.startswith("aneri"))
print("strip elimina espaços em branco a esquerda e a direita ","." ,"    neri neitzke             ".strip(),".")
print("lstrip elimina espaços em branco a direita ","." ,"    neri neitzke             ".lstrip(),".")
print("rstrip elimina espaços em branco a esquerda ",".", "    neri neitzke               ".rstrip(),".")
print("zstrip preenche a esquerda com zero(0) ", "465".zfill(8))
print("swapcase - inverte caracteres ", "Neri Neitske".swapcase())