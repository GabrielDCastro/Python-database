# membros:
import sqlite3

a = 0
z = 0

conn = sqlite3.connect('registro.db')
try:
    # definindo um cursor
    cursor = conn.cursor()

    # criando a tabela (schema)
    cursor.execute("""
    CREATE TABLE registro (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf     VARCHAR(11) NOT NULL,
            email TEXT NOT NULL,
            fone TEXT,
            cidade TEXT,
            uf VARCHAR(2) NOT NULL,
            criado_em DATE NOT NULL
    );
    """)
    conn.commit()
    print('Tabela criada com sucesso.')
except:
    print(" ")
    conn.rollback()

while a == 0:
    print('\n(1)Inserir registro')
    print('(2)Ver registros')
    print('(3)Atualizar dado')
    print('(4)Deletar registro')
    print('(5)Desconectar do banco')
    z = int(input())

    if z == 1:
        # solicitando os dados ao usuário
        p_nome = input('Nome: ')
        p_idade = input('Idade: ')
        p_cpf = input('CPF: ')
        p_email = input('Email: ')
        p_fone = input('Fone: ')
        p_cidade = input('Cidade: ')
        p_uf = input('UF: ')
        p_criado_em = input('Criado em (yyyy-mm-dd): ')

        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO registro (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES (?,?,?,?,?,?,?,?)
        """, (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf, p_criado_em))

        conn.commit()

        print('Dados inseridos com sucesso.')

    elif z == 2:
        cursor.execute("""
        SELECT * FROM registro;
        """)

        for linha in cursor.fetchall():
            print(linha)

    elif z == 3:
        id_cliente = input('Id cliente: ')
        novo_fone = input('Novo fone: ')
        novo_criado_em = input('Data de alteracao: ')

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE registro
        SET fone = ?, criado_em = ?
        WHERE id = ?
        """, (novo_fone, novo_criado_em, id_cliente))

        conn.commit()

        print('Dados atualizados com sucesso.')

    elif z == 4:
        id_cliente = input('Id cliente: ')

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM registro
        WHERE id = ?
        """, (id_cliente,))

        conn.commit()

        print('Registro excluido com sucesso.')

    elif z == 5:
        conn.close()
        a += 1

