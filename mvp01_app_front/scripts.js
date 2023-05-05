/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/ferramentas';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      
      data.ferramentas.forEach(item => insertList(item.descricao_longa, item.descricao_curta,
        item.nome_curto_fornecedor, item.quantidade_estoque,
        item.valor_unitario_venda, item.valor_unitario_compra))
      data.ferramentas.forEach(item => pegaListaId(item.id));
      
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

let ids = [];
let id;

function pegaListaId(idn) {
  ids.push(idn);
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()


/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
async function postItem(descricao_longa, descricao_curta, nome_curto_fornecedor, quantidade_estoque, valor_unitario_venda, valor_unitario_compra) {
  
  const formData = new FormData();
  formData.append('descricao_longa', descricao_longa);
  formData.append('descricao_curta', descricao_curta);
  formData.append('nome_curto_fornecedor', nome_curto_fornecedor);
  formData.append('quantidade_estoque', quantidade_estoque);
  formData.append('valor_unitario_venda', valor_unitario_venda);
  formData.append('valor_unitario_compra', valor_unitario_compra);
  let url = 'http://127.0.0.1:5000/ferramenta';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
function removeElement() {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML;
      let linha = this.parentNode.parentElement; // Seleciona a linha que contém a célula clicada
      let idLinha = linha.id - 1;
      id = ids[idLinha]; //Id do produto referente a linha

      if (confirm("Você tem certeza?")) {
        div.remove();
        deleteItem(id);
        alert("Removido!");

      }
    };
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (id_item) => {
  
  let url = 'http://127.0.0.1:5000/ferramenta?id=' + id_item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = () => {
  
  console.log(document.getElementById("valor_unitario_compra"));
  //let id_ferramenta = document.getElementById("newInput").value;
  let descricao_longa = document.getElementById("descricao_longa").value;
  let descricao_curta = document.getElementById("descricao_curta").value;
  let nome_curto_fornecedor = document.getElementById("nome_curto_fornecedor").value;
  let quantidade_estoque = document.getElementById("quantidade_estoque").value;
  let valor_unitario_venda = document.getElementById("valor_unitario_venda").value;
  let valor_unitario_compra = document.getElementById("valor_unitario_compra").value;

  if (descricao_curta === '') {
    alert("Escreva o nome de um item!");
  } else if (isNaN(quantidade_estoque) || isNaN(valor_unitario_venda) || isNaN(valor_unitario_compra)) {
    alert("Quantidade e valor precisam ser números!");
  } else {
    insertList(descricao_longa, descricao_curta, nome_curto_fornecedor, quantidade_estoque, valor_unitario_venda, valor_unitario_compra)
    postItem(descricao_longa, descricao_curta, nome_curto_fornecedor, quantidade_estoque, valor_unitario_venda, valor_unitario_compra)
    alert("Item adicionado!")

    ferramentas();
  }

}

/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
let rowId = 1;
function insertList(descricao_longa, descricao_curta, nome_curto_fornecedor, quantidade_estoque, valor_unitario_venda, valor_unitario_compra) {
  var item = [descricao_longa, descricao_curta, nome_curto_fornecedor, quantidade_estoque, valor_unitario_venda, valor_unitario_compra];
  var table = document.getElementById('myTable');
  var row = table.insertRow();
  row.id = `${rowId++}`; // atribui um id à linha e incrementa o contador

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1));
  document.getElementById("descricao_curta").value = "";
  document.getElementById("descricao_longa").value = "";
  document.getElementById("nome_curto_fornecedor").value = "";
  document.getElementById("quantidade_estoque").value = "";
  document.getElementById("valor_unitario_venda").value = "";
  document.getElementById("valor_unitario_compra").value = "";
  removeElement();
}

function feramentas() {
  window.location.href = "index.html";

}