"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...).
Escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""
#----------------------------------------------------------------#

def fibo (n):
    a, b = 0, 1

    if n == a or n == b:
        return True
    
    while True:
        k = a + b
        if k == n:
            return True
        elif k > n:
            return False
        a, b = b, k

numero = int(input("Digite um número para verificar se ele pertence a sequência de Fibonacci: "))

if fibo(numero):
    print(f'O número {numero} pertence a sequência!')

else:
    print(f'O número {numero} não pertence a sequência!')