# 🛒 Mini Loja Online

## Descrição
Este projeto implementa uma **Mini Loja Online** com **backend em Python (Flask)** e armazenamento de dados em arquivos JSON.  
O sistema permite:

- Cadastro de usuários;
- Login de usuários;
- Visualização de produtos;
- Criação de pedidos e histórico de compras.

O backend fornece **API REST**, que pode ser consumida por qualquer frontend (HTML, React, etc).

---

## Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-CORS
- JSON para armazenamento de dados
- Frontend opcional (HTML, CSS, JS)

---

## Estrutura do Projeto

```
mini_loja_backend/
│
├── app.py            # Backend em Flask
├── produtos.json     # Banco de dados de produtos
├── usuarios.json     # Banco de dados de usuários
└── pedidos.json      # Banco de dados de pedidos
```

---

## Como Rodar o Backend

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/mini-loja-online.git
```

2. Instale as dependências:
```bash
pip install flask flask-cors
```

3. Rode o servidor:
```bash
python app.py
```

O backend estará disponível em `http://localhost:5000`.

---

## Endpoints da API

### Produtos
- **GET `/produtos`**  
  Retorna todos os produtos cadastrados.

### Usuários
- **POST `/usuarios/cadastro`**  
  Cadastro de usuário.  
  **Body JSON:**
```json
{
  "usuario": "nomeusuario",
  "senha": "senha123"
}
```

- **POST `/usuarios/login`**  
  Login de usuário.  
  **Body JSON:**
```json
{
  "usuario": "nomeusuario",
  "senha": "senha123"
}
```

### Pedidos
- **POST `/pedidos`**  
  Cria um pedido.  
  **Body JSON:**
```json
{
  "usuarioId": "id_do_usuario",
  "itens": [
    {"produtoId": 1, "quantidade": 2},
    {"produtoId": 3, "quantidade": 1}
  ]
}
```

---

## Exemplo de Uso (Frontend ou Postman)

1. **Carregar produtos**
```javascript
fetch('http://localhost:5000/produtos')
  .then(res => res.json())
  .then(data => console.log(data));
```

2. **Cadastrar usuário**
```javascript
fetch('http://localhost:5000/usuarios/cadastro', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ usuario: "joao", senha: "1234" })
})
.then(res => res.json())
.then(data => console.log(data));
```

3. **Fazer login**
```javascript
fetch('http://localhost:5000/usuarios/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ usuario: "joao", senha: "1234" })
})
.then(res => res.json())
.then(data => console.log(data));
```

4. **Criar pedido**
```javascript
fetch('http://localhost:5000/pedidos', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    usuarioId: "id_do_usuario",
    itens: [
      {"produtoId": 1, "quantidade": 2}
    ]
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## Possíveis Melhorias

- Adicionar **autenticação JWT** para maior segurança;
- Conectar a um **banco de dados real** (PostgreSQL, MySQL, MongoDB);
- Criar **frontend completo** com HTML/CSS/JS ou React;
- Implementar **carrinho de compras e pagamento online**.

---

## Licença

Uso pessoal.
