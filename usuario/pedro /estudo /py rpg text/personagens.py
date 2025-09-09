import itens
import random
import armadura as ar
import armas as arm
maos=arm.armas("Mãos", dano=1, durabilidade=999)
# ==========================
# CLASSE PRINCIPAL: PERSONAGENS
# ==========================
class personagens:
    def __init__(self, classe, nome, idade, agilidade, forca, vida):
        self.classe = classe
        self.nome = nome
        self.idade = idade
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida
        self.arma = maos       # Inicialmente sem arma
        self.armadura = None   # Inicialmente sem armadura
        self.inventario = []   # Inicialmente vazio

    # --------------------------
    # Criação de personagens
    # --------------------------
    def cria_personagem(i):
        if i == 1:
            mago = personagens("Mago", input("Qual o seu nome? "), input("Qual a sua idade? "), 5, 3, 100)
            return mago
        elif i == 2:
            guerreiro = personagens("Guerreiro", input("Qual o seu nome? "), input("Qual a sua idade? "), 3, 5, 100)
            return guerreiro
        elif i == 3:
            arqueiro = personagens("Arqueiro", input("Qual o seu nome? "), input("Qual a sua idade? "), 4, 4, 100)
            return arqueiro  

    # --------------------------
    # Status horizontal do personagem
    # --------------------------
    def status_horizontal(self, dano_recebido=0):
        arma_nome = self.arma.nome if self.arma else "---"
        armadura_nome = self.armadura.nome if self.armadura else "---"
        defesa = self.armadura.defesa if self.armadura else 0
        durabilidade = self.armadura.durabilidade if self.armadura else 0
        vida_display = f"{self.vida + dano_recebido} - {dano_recebido} = {self.vida}" if dano_recebido > 0 else str(self.vida)
        return f"CLASSE: {self.classe} | NOME: {self.nome} | IDADE: {self.idade} | FORÇA: {self.forca} | AGILIDADE: {self.agilidade} | VIDA: {vida_display} | ARMA: {arma_nome} | ARMADURA: {armadura_nome} (d:{defesa})(u:{durabilidade})"

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
    
    def receber_dano(self, dano):
        defesa_total = 0
        if self.armadura:
            if self.armadura.durabilidade > 0:
                defesa_total += self.armadura.defesa
                self.armadura.usar_armadura(1)
                # Verifica se a armadura quebrou
                if self.armadura.durabilidade <= 0:
                    print(f"A armadura {self.armadura.nome} quebrou!")
                    self.armadura = None  # Remove a armadura ou define como quebrada
            else:
                print(f"A armadura {self.armadura.nome} já está quebrada e não protege mais.")
        
        # Considera itens de defesa do inventário
        for item in self.inventario:
            if hasattr(item, "defesa"):
                defesa_total += item.defesa

        dano_reduzido = max(dano - defesa_total, 0)
        self.vida -= dano_reduzido
        print("-"*50)  # Linha separadora
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
        print(f"{self.nome} recebeu um bônus de status: {status}")

    # --------------------------
    # Inventário
    # --------------------------
    def iventario(self, inventario):
        self.inventario = inventario
        print(f"{self.nome} possui os seguintes itens no inventário: {[item.nome for item in inventario]}")

    def pegar_item(self, item):
        self.inventario.append(item)
        print(f"{self.nome} pegou o item: {item.nome}")

# ==========================
# CLASSE INIMIGOS
# ==========================
class inimigos:
    vermelho = "\033[91m"  # Atributo de classe para exibição em vermelho
    reset = "\033[0m"      # Reset da cor

    def __init__(self, nome, forca, agilidade, vida):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida
        self.inventario = []
        self.armadura = None

    # --------------------------
    # Equipar item (bonus de força ou defesa)
    # --------------------------
    def equipar_item(self, item):
        self.inventario.append(item)
        if hasattr(item, "dano"):
            self.forca += item.dano
        print(f"{self.nome} equipou o item: {item.nome}")

    # --------------------------
    # Status horizontal do inimigo
    # --------------------------
    def status_horizontal_inimigo(self, dano_recebido=0):
        nomes_itens = [item.nome for item in self.inventario if hasattr(item, "nome")]
        vida_display = f"{self.vida + dano_recebido} - {dano_recebido} = {self.vida}" if dano_recebido > 0 else str(self.vida)
        return f"NOME: {self.nome} | FORÇA: {self.forca} | AGILIDADE: {self.agilidade} | VIDA: {vida_display} | ITENS: {', '.join(nomes_itens) if nomes_itens else '---'}"

    # --------------------------
    # Receber dano considerando defesa da armadura e itens
    # --------------------------
    def receber_dano(self, dano):
        defesa_total = 0
        if self.armadura:
            if self.armadura.durabilidade > 0:
                defesa_total += self.armadura.defesa
                self.armadura.usar_armadura(1)
                # Verifica se a armadura quebrou
                if self.armadura.durabilidade <= 0:
                    print(f"A armadura {self.armadura.nome} quebrou!")
                    self.armadura = None  # Remove a armadura ou define como quebrada
            else:
                print(f"A armadura {self.armadura.nome} já está quebrada e não protege mais.")
        
        # Considera itens de defesa do inventário
        for item in self.inventario:
            if hasattr(item, "defesa"):
                defesa_total += item.defesa

        dano_reduzido = max(dano - defesa_total, 0)
        self.vida -= dano_reduzido
        print("-"*50)  # Linha separadora
        print(f"{self.nome} recebeu {dano_reduzido} de dano (defesa total: {defesa_total})!")
        
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} agora tem {self.vida} de vida.")


# ==========================
# CLASSE ANIMAIS
# ==========================
class animais:
    def __init__(self, nome, forca, agilidade, vida):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida

# ==========================
# CLASSE ALDEOES
# ==========================
class aldeoes:
    def __init__(self, nome, forca, agilidade, vida):
        self.nome = nome
        self.forca = forca
        self.agilidade = agilidade
        self.vida = vida
