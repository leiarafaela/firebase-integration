import mysql.connector
from dotenv import load_dotenv
import os
from contextlib import closing
from db.util import row_to_dict, rows_to_dict

load_dotenv()


user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')


def conectar_mysql():
    conn = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )

    return conn





class Produto():
    def getAll():
        with closing(conectar_mysql()) as con, closing(con.cursor()) as cur:
            cur.execute("SELECT * FROM produtos")
            return rows_to_dict(cur.description, cur.fetchall())
        
    
    def getById(id):
        with closing(conectar_mysql()) as con, closing(con.cursor()) as cur:
            cur.execute("SELECT * FROM produtos WHERE id = %s", [id])
            return row_to_dict(cur.description, cur.fetchone())
        
    def create(produtos):
        with closing(conectar_mysql()) as con, closing(con.cursor()) as cur:
            cur.execute("INSERT INTO produtos (nome, preco, img) VALUES(%s,%s,%s)", [
                produtos['nome'], produtos['preco'], produtos['img']])
            auth = cur.lastrowid
            con.commit()
            con.close()
            return auth
        
    def update(id, produtos):
        with closing(conectar_mysql()) as con, closing(con.cursor()) as cur:
                cur.execute("UPDATE produtos SET  name = %s, preco = %s, img = %s  WHERE id = %s", [
                            produtos['nome'], produtos['preco'], produtos['img'],id])
                con.commit()
                con.close()

    def delete(id):
        with closing(conectar_mysql()) as con, closing(con.cursor()) as cur:
            cur.execute("DELETE FROM produtos WHERE id = %s", [id])
            con.commit()
            con.close()



produto = {
    "nome": "livro oab",
    "preco": 50.0,
    "img": "top.webp"
}
Produto.create(produto)