import random
class armas:
    def __init__(self, nome, dano, durabilidade):
        self.nome = nome
        self.dano = dano
        self.durabilidade = durabilidade

    def usar_arma(self):
        if self.durabilidade > 0:
            self.durabilidade -= 1
        else:
            print(f"A arma {self.nome} está quebrada e não pode ser usada.")
    def armas_randomicas_base1():
        if self.classe == "Mago":
            armas_lista = [
                armas("Cajado de Madeira", dano=5, durabilidade=10),
                armas("Varinha Mágica", dano=7, durabilidade=8),
                armas("Orbe Arcano", dano=10, durabilidade=5)
            ]
        elif self.classe == "Guerreiro":
            armas_lista = [
                armas("Espada Longa", dano=8, durabilidade=15),
                armas("Machado de Batalha", dano=10, durabilidade=12),
                armas("Martelo de Guerra", dano=12, durabilidade=10)
            ]
        elif self.classe == "Arqueiro":
            armas_lista = [
                armas("Arco Curto", dano=6, durabilidade=10),
                armas("Besta", dano=9, durabilidade=8),
                armas("Arco Longo", dano=11, durabilidade=6)
            ]
    def armas_inimigos1_e_lobos():
        garra = armas("Garra", dano=3, durabilidade=999)
        dentes = armas("Dentes Afiados", dano=4, durabilidade=999)
        return random.choice([garra, dentes])
        # armas_lista = [
        #     if self.classe == mago:
        #         armas("Cajado de Madeira", dano=5, durabilidade=10),
        #         armas("Varinha Mágica", dano=7, durabilidade=8),
        #         armas("Orbe Arcano", dano=10, durabilidade=5)
        #     elif self.classe == guerreiro:
        #         armas("Espada Longa", dano=8, durabilidade=15),
        #         armas("Machado de Batalha", dano=10, durabilidade=12),
        #         armas("Martelo de Guerra", dano=12, durabilidade=10)
        #     elif self.classe == arqueiro:
        #         armas("Arco Curto", dano=6, durabilidade=10),
        #         armas("Besta", dano=9, durabilidade=8),
        #         armas("Arco Longo", dano=11, durabilidade=6)
        #         ]
        return random.choice(armas_lista)