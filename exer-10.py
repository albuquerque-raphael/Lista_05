#Palíndromo são palavras, frases ou sequencia, que mantém mesma forma quando 
#invertido. Por exemplo, a palavra 'radar' é um políndromo, pois se você ler de trás
#para frente, ela ainda será 'radar'. Construa um programa que possa ler uma palavra
#ou frase e dizer se ela é um políndromo. Use a estrutura pilha para resolver a questão.

def is_palindromo(palavra):
    letras = list(palavra)
    palavra_invertida = letras[::-1]
    
    print(f'Palavra: {palavra}')
    print(f'Palavra invertida: ', end=' ')
    for letra in palavra_invertida:
        print(letra, end='')
    print(f'\n É palíndromo: {palavra =="".join(palavra_invertida)}\n')
    
is_palindromo('poema')
is_palindromo('asa')