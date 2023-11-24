ej1 = input('Introduce una frase que la paso a mayusculas: ')
print(ej1.upper())

ej2 = input('Introduce una frase que voy a contar las palabras: ')
print(f'Tu trase tiene {len(ej2.split())}')

ej3 = input('Introduce algo que solo sera verdad si son todos numeros: ')
print(ej3.isdigit())

ej4 = input('Introduce algo que que voy a cambiar las a por o: ')
print(ej4.replace('a','o'))
