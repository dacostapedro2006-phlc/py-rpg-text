import itens
import random
import armadura as ar
import armas as arm
import os # para limpar a tela

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# ==========================
# ARMA INICIAL PADRÃO
# ==========================
maos = arm.armas("Mãos", dano=1, durabilidade=999)  # arma padrão caso não tenha nenhuma equipada

# ==========================
# CLASSE PRINCIPAL: PERSONAGENS
# ==========================
class personagens:
    def __init__(self, classe, nome, idade, agilidade, forca, vida):
        # Atributos básicos do personagem
        self.classe = classe
        self.nome = nome
        self.idade = idade
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida
        self.vida_maxima = vida  # Armazena vida máxima para controle de poções
        self.arma = maos       # Inicialmente com arma padrão
        self.armadura = None   # Inicialmente sem armadura
        self.mana = 100 if classe == "Mago" else 50  # Mana inicial baseada na classe
        self.xp = 0             # Experiência inicial
        self.nivel = 1          # Nível inicial
        self.inventario = []   # Inventário inicialmente vazio

    # --------------------------
    # Criação de personagens
    # --------------------------
    @staticmethod
    def cria_personagem(i):
        # Método estático: cria um personagem com base na escolha do jogador
        if i == 1:
            return personagens("Mago", input("Qual o seu nome? "), input("Qual a sua idade? "), 5, 3, 100)
        elif i == 2:
            return personagens("Guerreiro", input("Qual o seu nome? "), input("Qual a sua idade? "), 3, 5, 100)
        elif i == 3:
            return personagens("Arqueiro", input("Qual o seu nome? "), input("Qual a sua idade? "), 4, 4, 100)  

    # --------------------------
    # Status horizontal do personagem
    # --------------------------
    def status_horizontal(self, dano_recebido=0):
        arma_nome = self.arma.nome if self.arma else "---"
        armadura_nome = self.armadura.nome if self.armadura else "---"
        dano_ataque = self.arma.dano if self.arma else 0
        defesa = self.armadura.defesa if self.armadura else 0
        durabilidade = self.armadura.durabilidade if self.armadura else 0
        vida_display = f"{self.vida + dano_recebido} - {dano_recebido} = {self.vida}" if dano_recebido > 0 else str(self.vida)
        return f"CLASSE: {self.classe} | NOME: {self.nome} | IDADE: {self.idade} | FORÇA: {self.forca} | AGILIDADE: {self.agilidade} | VIDA: {vida_display} | ARMA: {arma_nome} (dano:{dano_ataque})) | ARMADURA: {armadura_nome} (d:{defesa})(u:{durabilidade} \n | MANA: {self.mana} | NÍVEL: {self.nivel} | XP: {self.xp} | ITENS: {len(self.inventario)}"

    # --------------------------
    # Mostrar inventário do jogador
    # --------------------------
    def mostrar_inventario(self):
        vermelho = "\033[91m"  # Cor para armas equipadas
        azul = "\033[94m"      # Cor para armaduras equipadas
        reset = "\033[0m"      # Reset de cor

        while True:
            clear()
            print("-"*50)
            print(f"Inventário de {self.nome}")
            print("-"*50)
            if not self.inventario:
                print("Inventário vazio.")
                input("Pressione Enter para continuar...")
                break

            print("\nInventário:")
            for idx, item in enumerate(self.inventario, 1):
                status = ""
                if hasattr(item, "tipo"):
                    if item.tipo == "arma" and self.arma == item:
                        status = f"{vermelho}[equipado]{reset}"
                    elif item.tipo == "armadura" and self.armadura == item:
                        status = f"{azul}[equipado]{reset}"
                    elif item.tipo == "amuletos" and getattr(item, "ativado", False):
                        status = f"[ativado]"
                propriedades = getattr(item, "propriedades", "")
                print(f"{idx}. {item.nome} ({item.tipo}) {status} - {propriedades}")

            escolha = input("Digite o número do item para usar/equipar ou 'sair' para fechar: ")
            if escolha.lower() == 'sair':
                break

            try:
                indice = int(escolha) - 1
                if 0 <= indice < len(self.inventario):
                    item_selecionado = self.inventario[indice]

                    # --------------------------
                    # Consumíveis
                    # --------------------------
                    if item_selecionado.tipo == "consumivel":
                        if self.vida >= self.vida_maxima:
                            print("Sua vida já está cheia! Não é necessário usar esta poção.")
                        else:
                            usar = input(f"Quer usar {item_selecionado.nome}? (s/n): ").lower()
                            if usar == 's':
                                item_selecionado.usar(self)
                                self.inventario.pop(indice)
                    
                    # --------------------------
                    # Armas
                    # --------------------------
                    elif item_selecionado.tipo == "arma":
                        if self.arma == item_selecionado:
                            print(f"{item_selecionado.nome} já está equipada.")
                        else:
                            self.equipar_arma(item_selecionado)
                    
                    # --------------------------
                    # Armaduras
                    # --------------------------
                    elif item_selecionado.tipo == "armadura":
                        if self.armadura == item_selecionado:
                            print(f"{item_selecionado.nome} já está equipada.")
                        else:
                            self.equipar_armadura(item_selecionado)

                    # --------------------------
                    # Amuletos
                    # --------------------------
                    elif item_selecionado.tipo == "amuletos":
                        ativar = getattr(item_selecionado, "ativado", False)
                        item_selecionado.ativado = not ativar
                        estado = "ativado" if item_selecionado.ativado else "desativado"
                        print(f"{item_selecionado.nome} agora está {estado}.")

                    else:
                        print(f"{item_selecionado.nome} não pode ser usado agora.")
                else:
                    print("Número inválido. Tente novamente.")
                input("Pressione Enter para continuar...")
            except ValueError:
                print("Entrada inválida. Tente novamente.")
                input("Pressione Enter para continuar...")

    # --------------------------
    # Equipar arma ou armadura
    # --------------------------
    def equipar_arma(self, arma):
        self.arma = arma
        print(f"{self.nome} equipou a arma: {arma.nome}")

    def equipar_armadura(self, armadura):
        self.armadura = armadura
        print(f"{self.nome} equipou a armadura: {armadura.nome}")
    
    # --------------------------
    # Métodos de combate
    # --------------------------
    def atacar(self, alvo):
        if self.arma:
            dano = self.forca + self.arma.dano
            print(f"{self.nome} ataca {alvo.nome} com {self.arma.nome}, causando {dano} de dano!")
            alvo.receber_dano(dano)
        else:
            print(f"{self.nome} não tem uma arma equipada e não pode atacar!")
        self.xp += 10  # Ganha XP por atacar
        if self.xp >= self.nivel * 100:
            self.nivel += 1
            self.xp = 0
            self.forca += 1
            self.agilidade += 1
            self.vida_maxima += 10
            self.vida = self.vida_maxima
            print(f"{self.nome} subiu para o nível {self.nivel}! Atributos aumentados.")
        self.receber_mana(5, alvo)  # Ganha mana ao atacar inimigos mágicos
    
    def receber_dano(self, dano):
        defesa_total = 0
        if self.armadura:
            if self.armadura.durabilidade > 0:
                defesa_total += self.armadura.defesa
                self.armadura.usar_armadura(1)
                if self.armadura.durabilidade <= 0:
                    print(f"A armadura {self.armadura.nome} quebrou!")
                    self.armadura = None
            else:
                print(f"A armadura {self.armadura.nome} já está quebrada e não protege mais.")
        
        for item in self.inventario:
            if hasattr(item, "defesa"):
                defesa_total += item.defesa

        dano_reduzido = max(dano - defesa_total, 0)
        self.vida -= dano_reduzido
        print("-"*50)
        print(f"{self.nome} recebeu {dano_reduzido} de dano (defesa total: {defesa_total})!")
        
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} agora tem {self.vida} de vida.")


    # --------------------------
    # Fugir da batalha
    # --------------------------
    def fugir(self):
        if self.classe == "Arqueiro":
            chance_fuga = 0.8
        elif self.classe == "Mago":
            chance_fuga = 0.6
        else:  # Guerreiro  
            chance_fuga = 0.4
        return random.random() < chance_fuga

    # --------------------------
    # Receber bônus de status
    # --------------------------
    def receber_status(self, status):
        self.forca += status.get("forca", 0)
        self.agilidade += status.get("agilidade", 0)
        self.vida += status.get("vida", 0)
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
        print(f"{self.nome} recebeu um bônus de status: {status}")
    # --------------------------
    # Receber XP por completar quests
    # --------------------------
    def receber_xp_quest(self, xp):
        self.xp += xp
        print(f"{self.nome} recebeu {xp} de XP por completar a quest!")
        if self.xp >= self.nivel * 100:
            self.nivel += 1
            self.xp = 0
            self.forca += 1
            self.agilidade += 1
            self.vida_maxima += 10
            self.vida = self.vida_maxima
            print(f"{self.nome} subiu para o nível {self.nivel}! Atributos aumentados.")
    # --------------------------        
    # Receber mana ao atacar inimigos mágicos
    # --------------------------
    def receber_mana(self, quantidade, inimigo):
        if inimigo.raca == "magico":
            self.mana += quantidade
            if self.mana > 100:
                self.mana = 100
            print(f"{self.nome} recuperou {quantidade} de mana! Mana atual: {self.mana}")

    # --------------------------
    # Inventário geral
    # --------------------------
    def pegar_item(self, item):
        self.inventario.append(item)
        print(f"{self.nome} pegou o item: {item.nome}")

# ==========================
# CLASSE INIMIGOS
# ==========================
class inimigos:
    vermelho = "\033[91m"  # Cor para inimigo
    reset = "\033[0m"      # Reset cor

    def __init__(self):
        # Atributos base
        self.nome = None
        self.forca = 0
        self.agilidade = 0
        self.vida = 0
        self.inventario = []
        self.armadura = None
        self.raca = None
        self.nivel = 1

    def criar_inimigo(self, nome, raca, nivel):
        # Define informações principais
        self.nome = f"{self.vermelho}{nome}{self.reset}"
        self.raca = raca
        self.nivel = nivel

        # Atributos por raça
        if raca == "magicos":
            self.forca = 2 * nivel
            self.agilidade = 3 * nivel
            self.vida = 30 * nivel
            self.inventario.append(itens.amuleto.amuleto_randomico("mago"))

        elif raca == "lobos":
            self.forca = 4 * nivel
            self.agilidade = 2 * nivel
            self.vida = 40 * nivel
            self.inventario.append(itens.amuleto.amuleto_randomico("lobos"))

        elif raca == "gigantes":
            self.forca = 5 * nivel
            self.agilidade = 1 * nivel
            self.vida = 50 * nivel
            self.inventario.append(itens.amuleto.amuleto_randomico("gigante"))

        elif raca == "monstros":
            self.forca = 3 * nivel
            self.agilidade = 2 * nivel
            self.vida = 35 * nivel
            self.inventario.append(itens.amuleto.amuleto_randomico("monstro"))

    def equipar_item(self, item):
        self.inventario.append(item)
        if hasattr(item, "dano"):
            self.forca += item.dano
        print(f"{self.nome} equipou o item: {item.nome}")

    def status_horizontal_inimigo(self, dano_recebido=0):
        nomes_itens = [item.nome for item in self.inventario if hasattr(item, "nome")]
        vida_display = (
            f"{self.vida + dano_recebido} - {dano_recebido} = {self.vida}"
            if dano_recebido > 0 else str(self.vida)
        )
        return (
            f"NOME: {self.nome} | FORÇA: {self.forca} | "
            f"AGILIDADE: {self.agilidade} | VIDA: {vida_display} | "
            f"ITENS: {', '.join(nomes_itens) if nomes_itens else '---'} | "
            f"NÍVEL: {self.nivel}"
        )

    def receber_dano(self, dano):
        defesa_total = 0
        if self.armadura:
            if self.armadura.durabilidade > 0:
                defesa_total += self.armadura.defesa
                self.armadura.usar_armadura(1)
                if self.armadura.durabilidade <= 0:
                    print(f"A armadura {self.armadura.nome} quebrou!")
                    self.armadura = None
            else:
                print(f"A armadura {self.armadura.nome} já está quebrada e não protege mais.")
        
        for item in self.inventario:
            if hasattr(item, "defesa"):
                defesa_total += item.defesa

        dano_reduzido = max(dano - defesa_total, 0)
        self.vida -= dano_reduzido
        print("-"*50)
        print(f"{self.nome} recebeu {dano_reduzido} de dano (defesa total: {defesa_total})!")
        
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} agora tem {self.vida} de vida.")

    def atacar(self, alvo):
        dano_total = self.forca
        for item in self.inventario:
            if hasattr(item, "dano"):
                dano_total += item.dano
        print(f"{self.nome} ataca {alvo.nome}, causando {dano_total} de dano!")
        alvo.receber_dano(dano_total)

# ==========================
# CLASSES ANIMAIS E ALDEOES
# ==========================
class animais:
    def __init__(self, nome, forca, agilidade, vida):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida

class aldeoes:
    def __init__(self, nome, forca, agilidade, vida):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida
