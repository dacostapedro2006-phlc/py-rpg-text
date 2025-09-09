# jogo.py import
import personagens as pers
import time
import os
import random
import textos as tx

# def de estilo
def linha(x):
    print("-" * x)


def slow_print(text, delay):   
    for letra in text:
        print(letra, end='', flush=True)
        time.sleep(delay)


def limpar_tela(jogador=None):
    """Limpa a tela e mostra o status se jogador existir"""
    os.system('cls' if os.name == 'nt' else 'clear')
    if jogador:  # só imprime status se jogador já foi criado
        print(jogador.status_horizontal())
        print("-" * 80)


# Tela de seleção de personagens
init = True
while init: 
    # Limpa a tela (antes de criar personagem não mostra status)
    limpar_tela()

    # História inicial
    print("Capítulo 1 – Despertar na Clareira Misteriosa".upper())
    linha(50)
    # slow_print(tx.textos.text1(), 0.08)
    linha(50)
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

    # Menu de seleção
    # slow_print(tx.textos.fala_fantasma_0001(), 0.05)
    linha(50)
    input("\nPressione Enter para continuar...")
    limpar_tela()  # ainda sem jogador, não vai mostrar status

    # Escolha do personagem
    while True:
        limpar_tela()  # limpa tela a cada tentativa
        print("1 - Mago\n2 - Guerreiro\n3 - Arqueiro")
        try:
            escolha = int(input("Digite o número do personagem escolhido: "))
            if escolha not in [1, 2, 3]:
                print("Escolha inválida. Tente novamente.")
                time.sleep(0.5)
                continue
        except ValueError:
            print("Por favor, digite um número válido.")
            time.sleep(0.5)
            continue
        break 

    # Cria o personagem escolhido
    jogador1 = pers.personagens.cria_personagem(escolha)
    limpar_tela(jogador1)  # agora o status é mostrado corretamente
    
    init = False
