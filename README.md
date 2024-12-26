# Cifras y letras
Código para generar posibles soluciones de las pruebas del programa "Cifras y Letras"

Prueba de cifras: con seis números de entrada y una cifra objetivo, el código te devuelve las operaciones necesarias para alcanzar el objetivo. Usa todas las permutaciones de los seis números, reduciendo en una unidad las cifras si no encuentra ninguna solución para repetir el proceso. 

Prueba de letras: con diez letras de entrada, busca todas sus permutaciones hasta encontrar una palabra válida según la RAE, listadas en el archivo de texto adjunto `palabras_RAE.txt`. En el caso de no encontrar ninguna palabra con diez letras, borra una al azar y repite el proceso. 

Para ejecutar los archivos, sólo es necesario modificarlos en las primeras líneas para cambiar las letras en `letras.py` y los números y cifra objetivo en `cifras.py`, y correrlos en el terminal. 


```
>>>python3 cifras.py
==================================================================
  ____ _  __                         _         _                 
 / ___(_)/ _|_ __ __ _ ___   _   _  | |    ___| |_ _ __ __ _ ___ 
| |   | | |_| '__/ _` / __| | | | | | |   / _ \ __| '__/ _` / __|
| |___| |  _| | | (_| \__ \ | |_| | | |__|  __/ |_| | | (_| \__ \ 
 \____|_|_| |_|  \__,_|___/  \__, | |_____\___|\__|_|  \__,_|___/
                             |___/                               
==================================================================
 
Cifras:  [6, 50, 9, 8, 4, 10]
Objetivo:  617


Operaciones: 
1. 6+50 = 56
2. 56+4 = 60
3. 60*10 = 600
4. 600+9 = 609
5. 609+8 = 617
```

```
>>>python3 letras.py
==================================================================
  ____ _  __                         _         _                 
 / ___(_)/ _|_ __ __ _ ___   _   _  | |    ___| |_ _ __ __ _ ___ 
| |   | | |_| '__/ _` / __| | | | | | |   / _ \ __| '__/ _` / __|
| |___| |  _| | | (_| \__ \ | |_| | | |__|  __/ |_| | | (_| \__ \ 
 \____|_|_| |_|  \__,_|___/  \__, | |_____\___|\__|_|  \__,_|___/
                             |___/                               
==================================================================
 
Letras:  seatpulord
 
Palabra encontrada: sepultador, con 10 letras
```
