import sqlite3
from pathlib import Path

#Conexão com o banco de dados
ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
print(conexao)

#Ativando Executar comandos SQL
cursor=conexao.cursor()

#Criando Tabela clientes
cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY, nome VARCHAR(100), email VARCHAR(150))")

# Inserindo dados na tabela clientes
def InserirRegistro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", data)
    conexao.commit()
InserirRegistro(conexao, cursor, "Teste2", "teste2@gmail.com")

# Atualizando registros na tabela clientes
def Atualizar(conexao,cursor,nome,email,id):
    data=(nome,email,id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", data)
    conexao.commit()
Atualizar(conexao,cursor,"Testeonaldo","Teste@gmail.com", 1)

# Excluindo registros na tabela clientes
def ExcluirRegistro(conexao,cursor,id):
    data=(id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conexao.commit()
ExcluirRegistro(conexao,cursor,1)

# Inserir vários registros
def InserirMuitos(conexao,cursor, registros):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", registros)
    conexao.commit()
registros = [("Metapod", "metpod@gmail.com"),
          ("Pikachu", "pikapika@gmail.com"),
          ("Charmander", "charchar@gmail.com")]
InserirMuitos(conexao,cursor,registros)

# Excluir registros duplicados
def ExcluirDuplicados(conexao,cursor):
    cursor.execute("DELETE FROM clientes WHERE id NOT IN (SELECT MAX(id) FROM clientes GROUP BY nome, email)")
    conexao.commit()
ExcluirDuplicados(conexao, cursor)

# Consultar único registro
def ConsultarRegistro(conexao, cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()
consulta = ConsultarRegistro(conexao, cursor, 5)
print(consulta)

# Consultar todos os registros
def ConsultarTodos(conexao,cursor):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()