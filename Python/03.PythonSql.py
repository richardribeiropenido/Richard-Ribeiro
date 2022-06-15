import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-HFQTK7G;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Coenxão Bem-Sucedida")

cursor = conexao.cursor()

id = 3
cliente = "Richard Python"
produto = "Carro"
data = "15/05/2022"
preco = 50000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', {produto}' {data}' {preco}' {quantidade})"""
cursor.execute(comando)
cursor.commit()
