

## Letras para jugar 
letras = ['s', 'e', 'a', 't', 'p', 'u', 'l', 'o', 'r', 'd']
## En principio no tienes que cambiar más

## -----------------------------------------------------------

# Leer archivo con palabras RAE
palabras_archivo = "palabras_RAE.txt"
try:
    with open(palabras_archivo, 'r') as file:
        palabras = [line.strip() for line in file]
except FileNotFoundError:
    print(f"El archivo {palabras_archivo} no existe.")

# Hacer set para búsqueda más eficiente
set_palabras = set(palabras)



def find_word(letters):
 from itertools import permutations
 import random
 length_word = len(letters)
 if length_word != 10: 
  raise ValueError("El número de letras debe ser diez")
 letters_copy = letters[:]
 for k in range(length_word, 2, -1):
  for perm_lett in permutations(letters_copy, k):
   word = ''.join(perm_lett)
   if word in set_palabras:
    return word 
  random.sample(letters_copy, k-1)

 return None


def print_head():
 print("==================================================================")
 print("  ____ _  __                         _         _                 ")
 print(" / ___(_)/ _|_ __ __ _ ___   _   _  | |    ___| |_ _ __ __ _ ___ ")
 print("| |   | | |_| '__/ _` / __| | | | | | |   / _ \ __| '__/ _` / __|")
 print("| |___| |  _| | | (_| \__ \ | |_| | | |__|  __/ |_| | | (_| \__ \ ")
 print(" \____|_|_| |_|  \__,_|___/  \__, | |_____\___|\__|_|  \__,_|___/")
 print("                             |___/                               ")
 print("==================================================================")

print_head()
print(" ")
palabra = find_word(letras)
print("Letras: ", ''.join(letras))
print(" ")
if palabra: 
 print("Palabra encontrada: " + palabra + ", con " + str(len(palabra)) + " letras")
print(" ") 










