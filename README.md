# SefazES

> **Processo Seletivo SEFAZ‑ES**  
> Script em Python que cria um banco SQLite, popula com 30 números da sequência de Fibonacci e executa consultas conforme solicitado pela Secretaria de Estado da Fazenda do Espírito Santo (SEFAZ‑ES).

---

## 📋 Descrição do Projeto

Este repositório contém a solução completa para o processo seletivo da SEFAZ‑ES.  
O script principal (`selecao_sefaz_es.py`) realiza:

1. **Criação do Banco**  
   - Abre ou cria o arquivo `selecao_sefaz_es.db` (SQLite).
2. **Definição de Tabelas**  
   - `SELECAO_CANDIDATO` (ID, nome, data de inscrição).  
   - `SELECAO_TESTE` (ID, referência ao candidato, valor Fibonacci, flags de par/ímpar).
3. **Inserção de Dados**  
   - Registro do candidato (nome, timestamp automático).  
   - Geração dos 30 primeiros números de Fibonacci.  
   - Marcação de cada número como par ou ímpar.
4. **Consultas e Processos**  
   - Lista completa da sequência.  
   - Top 5 maiores valores.  
   - Contagem de pares e ímpares.  
   - Remoção de valores maiores que 5000.  
   - Exibição da sequência após remoção.
5. **Encerramento**  
   - Fecha a conexão com o banco e finaliza o script.

---

## 🚀 Tecnologias

- **Python** ≥ 3.7 (testado em 3.13)  
- **SQLite** via biblioteca padrão `sqlite3`

---

## ⚙️ Uso

1. **Clone este repositório**  
   ```bash
   git clone https://github.com/SeuUsuario/SefazES.git
   cd SefazES

# para executar o SCRIPT Windows
py selecao_sefaz_es.py
# ou
python selecao_sefaz_es.py

---

## 👤 Autor & Contato

**João Victor Gonçalves Oliveira**

🔗 LinkedIn: joão-victor-oliveira-2440231ab

📧 Email: joaovictorgoncalvsoliveira450@gmail.com

📱 Telefone: (27) 99604‑3451

