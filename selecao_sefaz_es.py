import sqlite3

# 1) Para conectar (ou criar) o arquivo de banco
conn = sqlite3.connect("selecao_sefaz_es.db")
cursor = conn.cursor()

print("Conexão estabelecida com sucesso, SQLite!")

# 2) Criar as tabelas SELECAO_CANDIDATO e SELECAO_TESTE
cursor.execute("""
CREATE TABLE IF NOT EXISTS SELECAO_CANDIDATO (
    ID_CANDIDATO INTEGER PRIMARY KEY AUTOINCREMENT,
    NME_CANDIDATO TEXT NOT NULL,
    DAT_INSCRICAO TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS SELECAO_TESTE (
    ID_TESTE INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_CANDIDATO INTEGER NOT NULL,
    NUM_FIBONACCI INTEGER NOT NULL,
    NUM_PAR INTEGER NOT NULL CHECK (NUM_PAR IN (0,1)),
    NUM_IMPAR INTEGER NOT NULL CHECK (NUM_IMPAR IN (0,1)),
    FOREIGN KEY (ID_CANDIDATO) REFERENCES SELECAO_CANDIDATO(ID_CANDIDATO)
);
""")

# Salva as alterações no banco
conn.commit()
print(" Tabelas criadas com sucesso!")

# 3) Para inserir um candidato na tabela 
nome= "João Victor Gonçalves Oliveira"
cursor.execute(
    "INSERT INTO SELECAO_CANDIDATO (NME_CANDIDATO) VALUES (?);",
    (nome,)
)
conn.commit()
# Peaga o ID que foi gerado
id_candidato = cursor.lastrowid
print(f"Candidato inserido com sucesso! ID_CANDIDATO = {id_candidato}")

# 4) Gerando e inserindo 30 numeros de Fibonacci
def gerar_fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Gera sequência
fib30 = gerar_fibonacci(30)

# Insere cada número com flags de par/ímpar
for num in fib30:
    is_par   = 1 if num % 2 == 0 else 0
    is_impar = 1 - is_par
    cursor.execute(
        "INSERT INTO SELECAO_TESTE (ID_CANDIDATO, NUM_FIBONACCI, NUM_PAR, NUM_IMPAR) VALUES (?, ?, ?, ?);",
        (id_candidato, num, is_par, is_impar)
    )

conn.commit()
print(" 30 números de Fibonacci inseridos com sucesso!")

# 5) Selecionar toda a sequência Fibonacci
cursor.execute(
    "SELECT NUM_FIBONACCI FROM SELECAO_TESTE WHERE ID_CANDIDATO = ? ORDER BY ID_TESTE;",
    (id_candidato,)
)
fib_all = [row[0] for row in cursor.fetchall()]
print("Sequência completa de Fibonacci:", fib_all)

# 6) Top 5 maiores números
cursor.execute("""
    SELECT NUM_FIBONACCI
      FROM SELECAO_TESTE
     WHERE ID_CANDIDATO = ?
  ORDER BY NUM_FIBONACCI DESC
     LIMIT 5;
""", (id_candidato,))
top5 = [row[0] for row in cursor.fetchall()]
print("Top 5 maiores números:", top5)

# 7) Contar pares e ímpares
cursor.execute("""
    SELECT SUM(NUM_PAR), SUM(NUM_IMPAR)
      FROM SELECAO_TESTE
     WHERE ID_CANDIDATO = ?;
""", (id_candidato,))
soma_par, soma_impar = cursor.fetchone()
print(f"Total de pares: {soma_par}, total de ímpares: {soma_impar}")  

# 8) Deletar registros com Fibonacci > 5000
cursor.execute("""
    DELETE
      FROM SELECAO_TESTE
     WHERE ID_CANDIDATO = ? 
       AND NUM_FIBONACCI > 5000;
""", (id_candidato,))
conn.commit()
print("Registros com número > 5000 removidos.")

# 9) Sequência após remover > 5000
cursor.execute(
    "SELECT NUM_FIBONACCI FROM SELECAO_TESTE WHERE ID_CANDIDATO = ? ORDER BY ID_TESTE;",
    (id_candidato,)
)
fib_after = [row[0] for row in cursor.fetchall()]
print("Sequência após deleção:", fib_after)

# 10) Fechar conexão
conn.close()
print("Conexão SQLite fechada. Script concluído com sucesso!")