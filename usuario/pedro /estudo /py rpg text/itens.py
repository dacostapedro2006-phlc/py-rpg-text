class item:
    def __init__(self, nome, tipo, propriedades):
        self.nome = nome          # Ex: "Poção de Vida", "Chave Dourada"
        self.tipo = tipo          # Ex: "consumivel", "quest", "ingrediente"
        self.propriedades = propriedades  # Dicionário com qualquer característica

    def mostrar(self):
        print(f"{self.nome} ({self.tipo}): {self.propriedades}")

    def usar(self, jogador):
        # Aqui você decide o que acontece quando o jogador usa o item
        pass
class Consumivel(item):
    def usar(self, jogador):
        if "cura" in self.propriedades:
            jogador.vida += self.propriedades["cura"]
            print(f"{jogador.nome} recuperou {self.propriedades['cura']} de vida!")

class QuestItem(item):
    pass
