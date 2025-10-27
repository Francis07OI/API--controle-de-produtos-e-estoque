from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from funcao import criar_tabela, cadastrar_produtos
from conexao import conectar

app = FastAPI(title="API Controle de Produtos e Estoque")


class Produto(BaseModel):
    nome: str
    categoria: str
    preco: float
    quantidade: int


    @app.on_event("startup")
def startup_event():
    criar_tabela()

#  cadastrar um produto
@app.post("/produtos/")
def adicionar_produto(produto: Produto):
    try:
        cadastrar_produtos(
            produto.nome, produto.categoria, produto.preco, produto.quantidade
        )
        return {"mensagem": "Produto cadastrado com sucesso!"}
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))

        app.get("/produtos/")
def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM produtos")
            produtos = cursor.fetchall()
            return {"produtos": produtos}
        except Exception as erro:
            raise HTTPException(status_code=500, detail=str(erro))
        finally:
            cursor.close()
            conexao.close()

# Atualizar produto
@app.put("/produtos/{id}")
def atualizar_produto(id: int, produto: Produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                """
                UPDATE produtos
                SET nome=%s, categoria=%s, preco=%s, quantidade=%s
                WHERE id=%s
                """,
                (produto.nome, produto.categoria, produto.preco, produto.quantidade, id)
            )
            conexao.commit()
            return {"mensagem": "Produto atualizado com sucesso!"}
        except Exception as erro:
            raise HTTPException(status_code=500, detail=str(erro))
        finally:
            cursor.close()
            conexao.close()

# Deletar produto
@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM produtos WHERE id=%s", (id,))
            conexao.commit()
            return {"mensagem": "Produto removido com sucesso!"}
        except Exception as erro:
            raise HTTPException(status_code=500, detail=str(erro))
        finally:
            cursor.close()
            conexao.close()
            