import random

class armas:
    def __init__(self, nome, dano, durabilidade, tipo="Comum"):
        self.nome = nome
        self.dano = dano
        self.durabilidade = durabilidade
        self.tipo = tipo
        self.propriedades = f"Dano: {self.dano}, Durabilidade: {self.durabilidade}, Tipo: {self.tipo}"

    def usar_arma(self):
        if self.durabilidade > 0:
            self.durabilidade -= 1
        else:
            print(f"A arma {self.nome} está quebrada e não pode ser usada.")

    @staticmethod
    def armas_randomicas_base1(classe):
        if classe == "Mago":
            armas_lista = [
                armas("Cajado de Madeira", dano=5, durabilidade=10, tipo="Cajado"),
                armas("Varinha Mágica", dano=7, durabilidade=8, tipo="Varinha"),
                armas("Orbe Arcano", dano=10, durabilidade=5, tipo="Orbe")
            ]
        elif classe == "Guerreiro":
            armas_lista = [
                armas("Espada Longa", dano=8, durabilidade=15, tipo="Espada Longa"),
                armas("Machado de Batalha", dano=10, durabilidade=12, tipo="Machado"),
                armas("Martelo de Guerra", dano=12, durabilidade=10, tipo="Martelo")
            ]
        elif classe == "Arqueiro":
            armas_lista = [
                armas("Arco Curto", dano=6, durabilidade=10, tipo="Arco Curto"),
                armas("Besta", dano=9, durabilidade=8, tipo="Besta"),
                armas("Arco Longo", dano=11, durabilidade=6, tipo="Arco Longo")
            ]
        else:
            armas_lista = [armas("Mãos", dano=1, durabilidade=999, tipo="Comum")]
        return random.choice(armas_lista)

    @staticmethod
    def armas_inimigos1_e_lobos():
        garra = armas("Garra", dano=3, durabilidade=999, tipo="Animal")
        dentes = armas("Dentes Afiados", dano=4, durabilidade=999, tipo="Animal")
        return random.choice([garra, dentes])
