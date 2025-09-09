import random

# ==========================
# CLASSE ITEM BASE
# ==========================
class item:
    def __init__(self, nome, tipo, propriedades):
        self.nome = nome                  # Ex: "Poção de Vida", "Chave Dourada"
        self.tipo = tipo                  # Ex: "consumivel", "amuletos", "quest"
        self.propriedades = propriedades  # Dicionário com características (cura, abrir porta, bônus)

    def mostrar(self):
        print(f"{self.nome} ({self.tipo}): {self.propriedades}")

    def usar(self, jogador):
        # Para ser sobrescrito nas subclasses
        pass

# ==========================
# SUBCLASSE CONSUMÍVEL
# ==========================
class consumivel(item):
    def usar(self, jogador):
        if "cura" in self.propriedades:
            jogador.vida += self.propriedades["cura"]
            print(f"{jogador.nome} recuperou {self.propriedades['cura']} de vida!")

# ==========================
# SUBCLASSE AMULETO
# ==========================
class amuleto(item):
    def __init__(self, nome, elemento, poder):
        super().__init__(nome, "amuletos", {"elemento": elemento, "poder": poder})
        self.elemento = elemento
        self.poder = poder

    def usar_amuleto(self, jogador):
        print(f"{jogador.nome} usa o amuleto {self.nome} e ativa seu poder de {self.elemento} ({self.poder})")

    @staticmethod
    def amuleto_randomico(classe_personagem):
        if classe_personagem == "Mago":
            lista = [
                amuleto("amuleto de Fogo", "Fogo", 5),
                amuleto("amuleto de Gelo", "Gelo", 5),
                amuleto("amuleto de Raio", "Raio", 5)
            ]
        elif classe_personagem == "Guerreiro":
            lista = [
                amuleto("amuleto da Força", "Força", 5),
                amuleto("amuleto da Resistência", "Resistência", 5),
                amuleto("amuleto da Vitalidade", "Vitalidade", 5)
            ]
        elif classe_personagem == "Arqueiro":
            lista = [
                amuleto("amuleto da Agilidade", "Agilidade", 5),
                amuleto("amuleto da Precisão", "Precisão", 5),
                amuleto("amuleto da Velocidade", "Velocidade", 5)
            ]
        return random.choice(lista)

# ==========================
# SUBCLASSE QUEST ITEM
# ==========================
class QuestItem(item):
    pass
