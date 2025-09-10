import json

def salvar_jogo(jogador):
    dados = {
        "nome": jogador.nome,
        "classe": jogador.classe,
        "vida": jogador.vida,
        "mana": jogador.mana,
        "nivel": jogador.nivel,
        "inventario": [item.nome for item in jogador.inventario]
    }
    with open("save.json", "w") as f:
        json.dump(dados, f, indent=4)

def carregar_jogo():
    try:
        with open("save.json", "r") as f:
            dados = json.load(f)
            return dados
    except FileNotFoundError:
        return None
