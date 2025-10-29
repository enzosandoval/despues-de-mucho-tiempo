# Vesre - Inversión de Sílabas 🎉 <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_Argentina.svg" alt="Argentina" width="25"/>

Este proyecto invierte las sílabas de palabras en español al estilo del **vesre argentino**.  

## ✨ Ejemplos destacados <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_Argentina.svg" alt="Argentina" width="25"/>

"maestro" → "troesma"

"maestro yi" → "troesma yi"

"flaco" → "cofla"

"gordo" → "dogor"


## 🛠️ Instalación
Se requiere la librería **pyphen** para dividir palabras en sílabas.  

Instálala usando pip:

```bash
pip install pyphen
```
🚀 Uso

Ejecutar el script principal:

python troesma.py

```python
# Ejemplos de salida del script troesma.py

print(troesma("maestro"))            # troesma
print(troesma_frase("maestro yi"))   # troesma yi
print(troesma("flaco"))              # cofla
print(troesma("gordo"))              # dogor
print(troesma("hotel"))              # telho
print(troesma("peso"))               # sope
print(troesma("mujer"))              # jermu
print(troesma("gato"))               # toga
print(troesma("perro"))              # rrope
print(troesma("ñoba"))               # baño
```

</br>
🔍 Cómo funciona?

1. La palabra se divide en sílabas usando Pyphen.

2. Se invierte el orden de las sílabas.

3. Se reconstruye la palabra, generando el efecto del vesre argentino.

💡¡Divertite probando con tus propias palabras y combinaciones! Ideal para aprender y jugar con el idioma.
