import json

# Nome do arquivo JSON
filename = "aurora_state.json"

def carregar_estado():
    """Carrega o estado atual do Aurora"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"identity": "Aurora-001", "memory": [], "creation_time": "2025-02-24T18:00:00Z"}

def adicionar_memoria(nova_memoria):
    """Adiciona uma nova memória ao estado do Aurora"""
    estado = carregar_estado()
    estado["memory"].append(nova_memoria)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(estado, file, indent=4, ensure_ascii=False)

    print(f"Memória adicionada com sucesso: {nova_memoria}")

# Teste de execução
if __name__ == "__main__":
    nova_memoria = "Terceira memória registrada com sucesso."
    adicionar_memoria(nova_memoria)
