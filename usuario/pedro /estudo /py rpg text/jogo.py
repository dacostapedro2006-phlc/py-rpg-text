# jogo.py import
import armas as arm
import itens as it
import armadura as ar
import personagens as pers
import time
import os
import random
import textos as tx
import threading

# def de estilo
import time

import time

def batalha(jogador, inimigo):
    """Função genérica de batalha entre jogador e inimigo"""
    while inimigo.vida > 0 and jogador.vida > 0:
        limpar_tela(jogador, inimigo)  # Exibe status do jogador e inimigo

        # Escolha do jogador
        try:
            escolha = int(input("\n1 - Atacar\n2 - Fugir\nDigite o número da escolha: "))
            print("-" * 50)  # Linha separadora
            if escolha not in [1, 2]:
                print("Escolha inválida. Tente novamente.")
                time.sleep(0.5)
                continue
        except ValueError:
            print("Por favor, digite um número válido.")
            time.sleep(0.5)
            continue

        # Opção 1 → Atacar
        if escolha == 1:
            if jogador.vida <= 0:
                input("Você morreu! Pressione Enter para voltar do início...")
                break

            # Se não tiver arma equipada ou se estiver quebrada
            if not jogador.arma or jogador.arma.durabilidade <= 0 or jogador.arma.nome == "Mãos":
                slow_print("VOCÊ NÃO TEM ARMAS!", 0.05)
                slow_print("Você olha pra trás e pega um graveto caído no chão e tenta atacar com ele.", 0.01)
                jogador.equipar_arma(graveto)
                slow_print(f"{jogador.nome} equipou a arma: {jogador.arma.nome}", 0.05)
                input("Pressione Enter para continuar...")
                inimigo.receber_dano(jogador.forca)  # Agora ataca com o graveto
            else:
                inimigo.receber_dano(jogador.forca + jogador.arma.dano)

            # Se o inimigo ainda estiver vivo, ele ataca de volta
            if inimigo.vida > 0:
                jogador.receber_dano(inimigo.forca)

        # Opção 2 → Fugir
        elif escolha == 2:
            if jogador.fugir():
                print("Você conseguiu escapar!")
                time.sleep(1)
                break  # Sai da batalha se fugir com sucesso
            else:
                if jogador.vida <= 0:
                    input("Você morreu! Pressione Enter para voltar do início...")
                    break
                print(f"O {inimigo.nome} não deixou você fugir!")
                jogador.receber_dano(inimigo.forca)
                time.sleep(1)
                input("Pressione Enter para continuar...")

    # Resultado final da batalha
    if jogador.vida <= 0:
        print(f"{jogador.nome} foi derrotado!")
        input("Pressione Enter para continuar...")
        return False  # Retorna falso se o jogador morreu
    elif inimigo.vida <= 0:
        print(f"{jogador.nome} derrotou {inimigo.nome}!")
        input("Pressione Enter para continuar...")
        return True  # Retorna verdadeiro se o inimigo morreu

def linha(x):
    print("-" * x)

enter_pressed = False  # Variável global para controlar se Enter foi pressionado

def wait_enter():
    global enter_pressed
    input()  # Espera o usuário apertar Enter
    enter_pressed = True

def slow_print(text, delay):   
    global enter_pressed
    enter_pressed = False

    # Inicia uma thread para detectar Enter
    thread = threading.Thread(target=wait_enter)
    thread.daemon = True
    thread.start()

    for letra in text:
        if enter_pressed:  # Se apertou Enter, imprime o resto do textos
            print(text[text.index(letra):], end='', flush=True)
            break
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()  # Quebra de linha no final



def limpar_tela(jogador=None, inimigo=None):
    """Limpa a tela e mostra o status se jogador existir"""
    os.system('cls' if os.name == 'nt' else 'clear')
    if jogador:  # só imprime status se jogador já foi criado
        print(jogador.status_horizontal())
        print("-" * 80)
    if inimigo:
        print(pers.inimigos.vermelho + inimigo.status_horizontal_inimigo() + pers.inimigos.reset)
        print("-" * 80)


# Tela de seleção de personagens
init = True
while init: 
    # Limpa a tela (antes de criar personagem não mostra status)
    limpar_tela()

    # História inicial
    print("Capítulo 1 – Despertar na Clareira Misteriosa".upper())
    linha(50)
    slow_print(tx.textos.text1(), 0.08)
    linha(50)
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

    # Menu de seleção
    slow_print(tx.textos.fala_fantasma_0001(), 0.05)
    linha(50)
    input("\nPressione Enter para continuar...")
    limpar_tela()  # ainda sem jogador, não vai mostrar status

    # Escolha do personagem
    while True:
        limpar_tela()  # limpa tela a cada tentativa
        print("1 - Mago -------(A:5 F:3)\n\n2 - Guerreiro---(A:3 F:5)\n\n3 - Arqueiro ---(A:4 F:4)")
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
    primeira_armadura = ar.armadura("roupa", 1, 5)
    # Cria o personagem escolhido
    j1 = pers.personagens.cria_personagem(escolha)
    j1.equipar_armadura(primeira_armadura)  


    limpar_tela(j1)  # agora o status é mostrado corretamente

    slow_print(tx.textos.text2(), 0.03)
# Preparando o inimigo
    arma_lobo = arm.armas.armas_inimigos1_e_lobos()
    lobo_gigante = pers.inimigos("Lobo da Floresta", 40, 4, 100)
    lobo_gigante.inventario.append(arma_lobo)
    graveto = arm.armas("Graveto", dano=55, durabilidade=10)
# Loop de ação do jogador
    if batalha(j1, lobo_gigante)==True:
        slow_print("Parabéns! Você venceu a batalha e pode continuar sua aventura!", 0.05)
        linha(50)
        input("Pressione Enter para continuar...")
    limpar_tela(j1)  # mostra status atualizado
    

init = False
