"""5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;"""
#----------------------------------------------------------------#

def invert_string(str):
    string_invertida = ''
    for i in range(len(str) - 1, -1, -1):
        string_invertida += str[i]
    return string_invertida

entrada = str(input('Digite qualquer palavra: '))
texto_invertido = invert_string(entrada)
print("O texto digitado foi:", entrada)
print("O texto invertido ficou:", texto_invertido)