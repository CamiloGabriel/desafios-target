"""4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. 
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?"""
#----------------------------------------------------------------#

def desc_inter():
    print ('Ligando o primeiro interruptor...')

    print ('Ligando o segundo interruptor...')

    condicao = input("Você pode  ver a lâmpada? (Digite 'acesa' ou 'apagada'): ").lower()

    if condicao == 'acesa':
        print ('A lâmpada é controlada pelo segundo interruptor!')
    elif condicao == 'apagada':
        print ('A lâmpada está apagada!')
        print ('É a lâmpada do interruptor que não foi ligado...')
    else:
        print("Entrada inválida. Por favor, digite 'acesa' ou 'apagada'.")

desc_inter()