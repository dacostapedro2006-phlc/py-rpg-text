#gerar atributos da armadura
class armadura:
    def __init__(self, nome, defesa, durabilidade):
        self.nome = nome
        self.defesa = defesa
        self.durabilidade = durabilidade
    def status_armadura(self):
        return f"Armadura: {self.nome} | Defesa: {self.defesa} | Durabilidade: {self.durabilidade}"
    def usar_armadura(self, dano):
        self.durabilidade -= dano
        if self.durabilidade < 0:
            self.durabilidade = 0
            print(f"A armadura {self.nome} quebrou!")
        else:
            print(f"A armadura {self.nome} agora tem durabilidade {self.durabilidade}")
    def reparar_armadura(self, valor):
        self.durabilidade += valor
        print(f"A armadura {self.nome} foi reparada para durabilidade {self.durabilidade}")
    def equipar_armadura(self, personagem):
        personagem.armadura = self
        print(f"{personagem.nome} equipou a armadura: {self.nome}")

    