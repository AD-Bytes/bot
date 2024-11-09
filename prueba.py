import os
# Este fragmento nos permite leer la totalidad de un archivo de texto

f = open('bot//text.txt', 'w', encoding='utf-8')
text = "Esta es la nueva prueba"
f.write(text)
print(text)
f.close()

# Y he aquí una versión más corta
with open('bot//text.txt', 'r', encoding='utf-8') as f:
    print(f.read())

print(os.listdir('bot//images'))