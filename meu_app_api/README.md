# O que consta na apresentacao

Este pequeno projeto faz parte do aprendizado adiquirido no curso **Desenvolvimento Full Stack Básico - Sprint 1**.
Nesta demosntração esta sendo apresentada um CRUD basico para gerenciar registros na base de dados, que simula um cadastro de Ferramentas. 
O objetivo aqui é demonstrar os conhecimentos básicos aprendidos no período das aulas apresentadas na sprint1 do calendário acadêmico.


Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Básico** 

O objetivo aqui é ilutsrar o conteúdo apresentado ao longo das três aulas da disciplina.

---
## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).
pip install -r requirements.txt
```
(env)$ 
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
