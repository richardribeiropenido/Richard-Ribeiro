from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"Item": "lata", "preço_unitario": 4, "quantidade": 5},
    2: {"Item": "garrafa 2L", "preço_unitario": 15, "quantidade": 5},
    3: {"Item": "garrafa 750ml", "preço_unitario": 10, "quantidade": 5},
    4: {"Item": "lata mini", "preço_unitario": 2, "quantidade": 5},
}


@app.get("/")
def home():
    return {"Vendas": len(vendas)}


@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    return vendas[id_venda]
    if id_venda in venda:
        return vendas[id_venda]
    else:
        return {"Erro": "ID Venda inexistente"}
