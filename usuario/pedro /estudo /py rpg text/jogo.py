# jogo.py import
import armas as arm           # Importa o módulo de armas
import itens as it            # Importa o módulo de itens (consumíveis, quests, etc.)
import armadura as ar        # Importa o módulo de armaduras
import personagens as pers   # Importa o módulo de personagens
import time
import os
import random
import textos as tx           # Importa os textos do jogo
import threading              # Para impressão lenta com possibilidade de Enter

# ===================== FUNÇÃO DE BATALHA SIMPLES =====================
def batalha_simples(jogador, inimigo):
    """
    Batalha simples entre jogador e inimigo:
    Opções:
    1 - Atacar
    2 - Fugir
    """
    while inimigo.vida > 0 and jogador.vida > 0:
        limpar_tela(jogador, inimigo)  # Limpa tela e exibe status

        # Escolha do jogador
        try:
            escolha = int(input("\n1 - Atacar\n2 - Fugir\nDigite o número da escolha: "))
            if escolha not in [1, 2]:
                print("Escolha inválida. Tente novamente.")
                time.sleep(0.5)
                continue
        except ValueError:
            print("Por favor, digite um número válido.")
            time.sleep(0.5)
            continue

        # Ataque do jogador
        if escolha == 1:
            if not jogador.arma or jogador.arma.durabilidade <= 0 or jogador.arma.nome.lower() == "mãos":
                slow_print("VOCÊ NÃO TEM ARMAS!", 0.05)
                slow_print("ghost: Aqui, pegue esse graveto para se defender!", 0.05)
                graveto = arm.armas("graveto", dano=random.randint(30,50), durabilidade=999)  # Arma improvisada
                jogador.equipar_arma(graveto)
            jogador.atacar(inimigo)
            input("Pressione Enter para continuar...")

        # Tentativa de fuga
        elif escolha == 2:
            if jogador.fugir():
                slow_print("Você conseguiu escapar!", 0.05)
                time.sleep(1)
                return "skip"
            else:
                slow_print(f"O {inimigo.nome} não deixou você fugir!", 0.05)
                jogador.receber_dano(inimigo.forca)
                input("Pressione Enter para continuar...")

        # Ataque do inimigo se ainda estiver vivo
        if inimigo.vida > 0 and escolha != 2:
            inimigo.atacar(jogador)
            input("Pressione Enter para continuar...")

    # Resultado final da batalha
    if jogador.vida <= 0:
        slow_print(f"{jogador.nome} foi derrotado!", 0.05)
        input("Pressione Enter para continuar...")
        return False
    elif inimigo.vida <= 0:
        slow_print(f"{jogador.nome} derrotou {inimigo.nome}!", 0.05)
        input("Pressione Enter para continuar...")
        return True

# ===================== FUNÇÃO DE BATALHA COMPLETA =====================
def batalha_completa(jogador, inimigo):
    """
    Batalha completa com opções:
    1 - Atacar
    2 - Fugir
    3 - Usar Item
    4 - Defender
    """
    while inimigo.vida > 0 and jogador.vida > 0:
        limpar_tela(jogador, inimigo)

        # Escolha do jogador
        try:
            escolha = int(input("\n1 - Atacar\n2 - Fugir\n3 - Usar Item\n4 - Defender\nDigite o número da escolha: "))
            if escolha not in [1, 2, 3, 4]:
                print("Escolha inválida. Tente novamente.")
                time.sleep(0.5)
                continue
        except ValueError:
            print("Por favor, digite um número válido.")
            time.sleep(0.5)
            continue

        # Ataque
        if escolha == 1:
            if not jogador.arma or jogador.arma.durabilidade <= 0 or jogador.arma.nome.lower() == "mãos":
                slow_print("VOCÊ NÃO TEM ARMAS!", 0.05)
                graveto = arm.armas("graveto", dano=1, durabilidade=999)
                jogador.equipar_arma(graveto)
            jogador.atacar(inimigo)
            input("Pressione Enter para continuar...")

        # Fugir
        elif escolha == 2:
            if jogador.fugir():
                slow_print("Você conseguiu escapar!", 0.05)
                time.sleep(1)
                break
            else:
                slow_print(f"O {inimigo.nome} não deixou você fugir!", 0.05)
                inimigo.atacar(jogador)
                input("Pressione Enter para continuar...")

        # Usar item
        elif escolha == 3:
            if jogador.inventario:
                print("Itens disponíveis:")
                for i, item in enumerate(jogador.inventario, 1):
                    print(f"{i} - {item.nome}")
                try:
                    escolha_item = int(input("Escolha o número do item: "))
                    if 1 <= escolha_item <= len(jogador.inventario):
                        item = jogador.inventario[escolha_item - 1]
                        jogador.usar_item(item)
                    else:
                        print("Escolha inválida!")
                        time.sleep(0.5)
                        continue
                except ValueError:
                    print("Entrada inválida!")
                    time.sleep(0.5)
                    continue
            else:
                print("Você não tem itens!")
                time.sleep(0.5)

        # Defender
        elif escolha == 4:
            if jogador.armadura and "escudo" in jogador.armadura.nome.lower():
                slow_print(f"{jogador.nome} se defende com {jogador.armadura.nome}!", 0.05)
                defesa = jogador.armadura.defesa * 2
                jogador.receber_dano(max(0, inimigo.forca - defesa))
            else:
                print("Você não tem um escudo para defender!")
                time.sleep(0.5)

        # Turno do inimigo
        if inimigo.vida > 0 and escolha != 4:
            inimigo.atacar(jogador)
            input("Pressione Enter para continuar...")

    # Resultado final
    if jogador.vida <= 0:
        slow_print(f"{jogador.nome} foi derrotado!", 0.05)
        input("Pressione Enter para continuar...")
        return False
    elif inimigo.vida <= 0:
        slow_print(f"{jogador.nome} derrotou {inimigo.nome}!", 0.05)
        input("Pressione Enter para continuar...")
        return True

# ===================== FUNÇÕES AUXILIARES =====================
def linha(x):
    """Imprime linha de separação"""
    print("-" * x)

enter_pressed = False  # Detecta se Enter foi pressionado

def wait_enter():
    """Thread para detectar Enter"""
    global enter_pressed
    input()
    enter_pressed = True

def slow_print(text, delay):
    """Imprime texto lentamente com possibilidade de pular com Enter"""
    global enter_pressed
    enter_pressed = False
    thread = threading.Thread(target=wait_enter)
    thread.daemon = True
    thread.start()
    for letra in text:
        if enter_pressed:
            print(text[text.index(letra):], end='', flush=True)
            break
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()

def limpar_tela(jogador=None, inimigo=None):
    """Limpa tela e mostra status de jogador/inimigo"""
    os.system('cls' if os.name == 'nt' else 'clear')
    if jogador:
        print(jogador.status_horizontal())
        print("-" * 80)
    if inimigo:
        print(pers.inimigos.vermelho + inimigo.status_horizontal_inimigo() + pers.inimigos.reset)
        print("-" * 80)

# ===================== INÍCIO DO JOGO =====================
init = True
while init:
    limpar_tela()
    print("Capítulo 1 – Despertar na Clareira Misteriosa".upper())
    linha(50)
    slow_print(tx.textos.text1(), 0.08)
    linha(50)
    input("\nPressione Enter para continuar...")
    limpar_tela()

    # Introdução do fantasma
    slow_print(tx.textos.fala_fantasma_0001(), 0.05)
    linha(50)
    input("\nPressione Enter para continuar...")
    limpar_tela()

    # Seleção de personagem
    while True:
        limpar_tela()
        print("1 - Mago -------(A:5 F:3)\n2 - Guerreiro---(A:3 F:5)\n3 - Arqueiro ---(A:4 F:4)")
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

    # Criação da armadura inicial
    primeira_armadura = ar.armadura("roupa", defesa=random.randint(1,10), durabilidade=5)

    # ===================== ITENS INICIAIS =====================
    pocao_pequena = it.consumivel("poção pequena", "consumivel", propriedades={"cura": 20})
    pocao_media = it.consumivel("poção média", "consumivel", propriedades={"cura": 50})
    pocao_grande = it.consumivel("poção grande", "consumivel", propriedades={"cura": 100})
    maca = it.consumivel("maçã", "consumivel", propriedades={"cura": 10})

    # ===================== ARMAS =====================
    estilingue = arm.armas("estilingue", dano=random.randint(5,10), durabilidade=15)

    # Criação do personagem
    j1 = pers.personagens.cria_personagem(escolha)
    j1.equipar_armadura(primeira_armadura)
    j1.inventario.extend([pocao_pequena, pocao_media, pocao_grande, maca, estilingue])

    # ===================== INIMIGO =====================
    arma_lobo = arm.armas.armas_inimigos1_e_lobos()
    lobo_gigante = pers.inimigos("lobo da floresta", 40, 4, 100)
    lobo_gigante.inventario.append(arma_lobo)
    graveto = arm.armas("graveto", dano=random.randint(30, 50), durabilidade=999)

    # ===================== BATALHA =====================
    slow_print(tx.textos.text2(), 0.05)
    linha(50)
    input("\nPressione Enter para continuar...")
    limpar_tela(j1)
    batalha1 = batalha_simples(j1, lobo_gigante)

    if batalha1 == "skip":
        slow_print("Você escapou da batalha!", 0.05)
        continue
    elif batalha1 is False:
        slow_print("GAME OVER!", 0.1)
        input("Pressione Enter para voltar do início...")
        continue
    elif batalha1 is True:
        slow_print("Você venceu a batalha!", 0.05)
        slow_print(f"O {lobo_gigante.nome} deixou cair uma {arma_lobo.nome}!", 0.05)
        j1.inventario.append(arma_lobo)
        graveto = None
        slow_print(f"{j1.nome} pegou a {arma_lobo.nome} e a colocou no inventário.", 0.05)
        input("Pressione Enter para continuar...")
        limpar_tela(j1)

    # Sugestão de checar inventário após a primeira batalha
    slow_print("Agora que você venceu sua primeira batalha, que tal dar uma olhada no seu inventário?", 0.05)
    input("Pressione Enter para abrir o inventário...")
    j1.mostrar_inventario()
    init = False
