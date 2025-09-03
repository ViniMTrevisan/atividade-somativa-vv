def sao_anagramas(string1, string2):
    #TODO:
    s1 = string1.replace(" ", "").lower()
    s2 = string2.replace(" ", "").lower()

    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


print(sao_anagramas("amor", "roma"))
print(sao_anagramas("A gentleman", "Elegant man"))
print(sao_anagramas("gato", "cabra"))
pass
