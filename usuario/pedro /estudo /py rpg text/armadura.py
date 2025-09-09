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
    # def equipar_armadura(self, personagem):
    #     personagem.armadura = self
    #     print(f"{personagem.nome} equipou a armadura: {self.nome}")
    def armadura_randomica_base1():
        if self.classe == "Mago":
            armaduras_lista = [
                armadura("Túnica Mística", defesa=2, durabilidade=10),
                armadura("Manto Arcano", defesa=3, durabilidade=8),
                armadura("Veste Enfeitiçada", defesa=4, durabilidade=5)
            ]
        elif self.classe == "Guerreiro":
            armaduras_lista = [
                armadura("Cota de Malha", defesa=5, durabilidade=15),
                armadura("Armadura de Placas", defesa=7, durabilidade=12),
                armadura("Peitoral de Ferro", defesa=8, durabilidade=10)
            ]
        elif self.classe == "Arqueiro":
            armaduras_lista = [
                armadura("Colete de Couro", defesa=4, durabilidade=10),
                armadura("Armadura de Couro Reforçado", defesa=5, durabilidade=8),
                armadura("Veste de Caçador", defesa=6, durabilidade=6)
            ]
        return random.choice(armaduras_lista)

    