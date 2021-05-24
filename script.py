# 1. Importando módulo para conexão
import psycopg2


# 2. Conectando ao banco de dados
conn = psycopg2.connect(
    host='localhost',
    database='pessoas',
    user='postgres',
    password='!@#Udn975Cf'
)

# 3. Abrindo um cursor para manipular o banco
cur = conn.cursor()

# 4. Consultando uma tabela
cur.execute('SELECT * FROM pessoas;')
cur.fetchall()

# 5. Encerrando a comunicação com o banco de dados
cur.close()
conn.close()
exit()