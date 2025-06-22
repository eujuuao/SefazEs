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