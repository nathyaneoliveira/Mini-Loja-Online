async function carregarProdutos() {
  const res = await fetch('http://localhost:5000/produtos');
  const produtos = await res.json();
  mostrarProdutos(produtos);
}

async function cadastroUsuario(usuario, senha) {
  const res = await fetch('http://localhost:5000/usuarios/cadastro', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ usuario, senha })
  });
  return await res.json();
}

async function loginUsuario(usuario, senha) {
  const res = await fetch('http://localhost:5000/usuarios/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ usuario, senha })
  });
  return await res.json();
}

async function finalizarCompra(usuarioId, itens) {
  const res = await fetch('http://localhost:5000/pedidos', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ usuarioId, itens })
  });
  return await res.json();
}
