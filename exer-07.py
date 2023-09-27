#Crie uma calculadora que avalia expressão matemática no formato Notação Polonesa
#Reversa (RPN). Use uma pilha para armazenar os operandos e operadores e realizar os
#calculos

def calculadora_rpn(expressao):
    pilha = []
    for token in expressao.split():
        if token in ['+', '-', '*', '/']:
            num2 = pilha.pop()
            num1 = pilha.pop()
            if token == '+':
                resultado = num1 + num2
            elif token == '-':
                resultado = num1 - num2
            elif token == '*':
                resultado = num1 * num2
            elif token == '/':
                resultado = num1 / num2
            pilha.append(resultado)
        else:
            pilha.append(float(token))
    return round(pilha.pop(), 4)

resultado = calculadora_rpn('4 5 6 + * 5 / 6 -')
print(resultado)
