def encontrar_maior_palavra(frase):
    import string
    palavras = frase.split()
    maior = ""
    for palavra in palavras:
        limpa = palavra.strip(string.punctuation)
        if len(limpa) > len(maior):
            maior = limpa
    return maior

frase = input()
print(encontrar_maior_palavra(frase))