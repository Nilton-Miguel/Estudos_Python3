ex = input("Digite uma expressão matemática: \n")
abertos = ex.count('(')
fechados = ex.count(')')
erros = 0

for pos, letra in enumerate(ex):
    if letra == '(' and (pos != (len(ex) - 1)):
        if ((ex[pos + 1] == "+" or ex[pos + 1] == "-") or (ex[pos + 1] == "*" or ex[pos + 1] == "/")) or ex[pos + 1] == ")":
            erros += 1

    if letra == ')' and (pos != 0):
        if (ex[pos - 1] == "+" or ex[pos - 1] == "-") or (ex[pos - 1] == "*" or ex[pos - 1] == "/") or ex[pos - 1] == "(":
            erros += 1

if abertos != fechados:
    erros += 1

if erros == 0:
    print("EXPRESSÃO VÁLIDA")
else:
    print("EXPRESSÃO INVÁLIDA")
