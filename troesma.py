import pyphen

dic = pyphen.Pyphen(lang='es')

def troesma(palabra):
    silabas = dic.inserted(palabra).split('-')
    invertida = "".join(reversed(silabas))
    return invertida

def troesma_frase(frase):
    palabras = frase.split()
    transformadas = [troesma(p) for p in palabras]
    return " ".join(transformadas)


print(troesma_frase("maestro yi"))  # troesma yi
print(troesma("maestro"))           # troesma
print(troesma("gordo"))             # dogor
print(troesma("flaco"))             # cofla
print(troesma("hotel"))             # telho
print(troesma("peso"))              # sope
print(troesma("mujer"))             # jermu
print(troesma("gato"))              # toga
print(troesma("perro"))             # rrope
print(troesma("ñoba"))              # baño
