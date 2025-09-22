import random

def jogar():
    usuario = input("Jogo de Pedra, Papel e Tesoura\nQual voce vai jogar?\n('pe' para pedra, 'pa' para papel, 'te' para tesoura): ")
    computador = random.choice(['pe', 'pa', 'te'])  

    if usuario == computador:
        return 'Empate'
    
    if ganhar(usuario, computador):
        return 'Você venceu!'
    
    return 'Você perdeu!'

def ganhar(jogador, oponente):
    # pe > te | te > pa | pa > pe
    if (jogador == 'pe' and oponente == 'te') or (jogador == 'te' and oponente == 'pa') or (jogador == 'pa' and oponente == 'pe'):
        return True
    
print(jogar())