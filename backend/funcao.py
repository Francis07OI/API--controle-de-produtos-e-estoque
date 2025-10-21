from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao: 
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos(
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            categoria VARCHAR (50),
            preco NUMERIC (10,2),
            quantidade INT                                        
            )
            """)
            conexao.commit()
            print("deu certo!") 
        except Exception as erro:
            print(f"erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()
