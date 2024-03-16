# 3) Descubra a lógica e complete o próximo elemento:



# a) 1, 3, 5, 7, ___: Adiciona 2 ao termo anterior


# b) 2, 4, 8, 16, 32, 64, ____: Cada termo é o dobro do anterior


# c) 0, 1, 4, 9, 16, 25, 36, ____: São os quadrados de -> 0,1,2,3,4,5,6 e 7 


# d) 4, 16, 36, 64, ____: São os quadrados dos números pares, começando por 2


# e) 1, 1, 2, 3, 5, 8, ____: Sequência de Fibonacci


# f) 2,10, 12, 16, 17, 18, 19, ____: A única lógica qua consegui atribuir a esse foi que o próximo número some 1 com o anterior, de acordo com a sequência dele mesmo

#----------------------------------------------------------------#
#Sequência a:
def next_a (sequencia):
    return sequencia [-1] + 2


#Sequência b:
def next_b (sequencia):
    return sequencia [-1] * 2


#Sequência c:
def next_c (sequencia):
    return (len(sequencia)) ** 2

#Sequência d:
def next_d (sequencia):
    return (len(sequencia) * 2) ** 2

#Sequência e:
def next_e (sequencia):
    return sequencia [-1] + sequencia [-2]

#Sequência f:
def next_f (sequencia):
    return sequencia [-1] + 1

dados ={
    'a': [1, 3, 5, 7],
    'b': [2, 4, 8, 16, 32, 64],
    'c': [0, 1, 4, 9, 16, 25, 36],
    'd': [4, 16, 36, 64],
    'e': [1, 1, 2, 3, 5, 8],
    'f': [2, 10, 12, 16, 17, 18, 19]
}

for n, sequencia in dados.items():
    next_element = None
    if n == 'a':
        next_element = next_a(sequencia)
    elif n == 'b':
        next_element = next_b(sequencia)
    elif n == 'c':
        next_element = next_c(sequencia)
    elif n == 'd':
        next_element = next_d(sequencia)
    elif n == 'e':
        next_element = next_e(sequencia)
    elif n == 'f':
        next_element = next_f(sequencia)
    
    print(f"A próxima sequência para '{n}' é: {next_element}!")
