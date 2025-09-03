def cifra_de_cesar(texto="", deslocamento=0):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += novo_char
        else:
            resultado += char
    return resultado

print(cifra_de_cesar("abc", 2))               
print(cifra_de_cesar("xyz", 3))                
print(cifra_de_cesar("Ataque ao Amanhecer!", 5))
print(cifra_de_cesar())
