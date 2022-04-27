cadastro = {
    'id' : 1,
    'nome' : 'Amendoa Silva',
    'filhos' : ['João', 'elber'],
    'compras' : [
        {
            'id' : 4758,
            'produto' : 'Notebook Gamer',
            'preco' : 2142.99
        }
    ]
}

altura = cadastro.get('altura', None)

print(altura)

#notebookGamer = cadastro["compras"][0]["produto"]

#print(f'O usuário {cadastro["nome"]} realizou a seguinte compra: {notebookGamer} ')