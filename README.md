# fluxo projeto

/fluxo/
├── api *Django Rest
└── front *Next

desenvolvido com base no conceito de Domain-Driven Design (DDD), ou Design Guiado pelo Domínio

Domínio: E-commerce
Subdomínios: Gestão de contas de usuários - Catálogo de produtos - Processamento de vendas

Aplicações criadas em Contexto Delimitado o código de cada uma é resolver os problemas daquele domínio especifíco.

Separation of Concerns - SoC - Separação de responsabilidades
    O software deve ser divido em partes distintas que se sobrepõem o mínimo possível em termos de funcionalidade

Modularidade - Modular architecture 
    Construir o software a partir de "módulos" independetes e intercambiáveis.

Single Responsability - SRP - Princípio de responsabilidade única
    Cada aplicação deve ter uma funcionalidade única, e principal, razão para existir e para ser modificada. Uma aplicação deve mudar por alterações na lógica de vendas e não porque você adicionou um novo campo na descrição de um produto.

BackEnd First
   Desvantagem o frontend fica bloqueado

FrontEnd First
    Pode gerar demandas difíceis para o backend

Contrato-Primeiro
    Times backend e frontend definem um contrato juntos, depois desenvolvem em parelelo

docker-compose up 
caso tenha alterado o Dockerfile ou o requirements 
docker-compose up --build

mantendo os dados
docker-compose down
apagando os dados do banco de dados
docker-compose down -v

Dont repeat yourself 

DRF
ViewSets 
    É uma super view que agrupa a lógica para todas as operações CRUD me uma única classe
Routers 
    É um gerador de URls automático que cria todas as rotas necessárias para o view set

ViewSets: 

### Guia Rápido de Customização de `ViewSets` (Django REST Framework)

Esta tabela resume os principais métodos para customizar o comportamento de um `ModelViewSet` no DRF, separando as ações de **escrita** (que usam ganchos `perform_*`) das ações de **leitura** (que usam `get_*` para filtragem).

| Ação (CRUD)             | Método HTTP     | Método Principal      | Ponto de Customização          | Propósito Principal da Customização                                                                 |
| :---------------------- | :-------------- | :-------------------- | :----------------------------- | :-------------------------------------------------------------------------------------------------- |
| **Criar** (Create)      | `POST`          | `.create()`           | `.perform_create(serializer)`  | Executar lógica customizada **antes de salvar** um novo objeto (ex: associar ao usuário, enviar e-mail). |
| **Atualizar** (Update)  | `PUT` / `PATCH` | `.update()`           | `.perform_update(serializer)`  | Executar lógica customizada **antes de salvar** uma atualização (ex: logar alteração, atualizar `modified_by`). |
| **Deletar** (Delete)    | `DELETE`        | `.destroy()`          | `.perform_destroy(instance)`   | Customizar a exclusão (ex: "soft delete" em vez de apagar do banco, invalidar um cache).              |
| **Listar** (List)       | `GET`           | `.list()`             | `.get_queryset()`              | **Filtrar** o conjunto de dados retornado (ex: mostrar apenas itens pertencentes ao usuário logado).      |
| **Detalhar** (Retrieve) | `GET`           | `.retrieve()`         | `.get_queryset()`/`.get_object()` | **Filtrar ou modificar** a busca de um único objeto (ex: garantir permissões de acesso ao objeto).   |

<br>

A filosofia é utilizar os "ganchos" (`hooks`) fornecidos pelo framework para injetar sua lógica de negócio específica sem precisar reescrever o comportamento padrão de requisição/resposta, resultando em um código mais limpo e de fácil manutenção.

Stateful - O servidor armazena em uma tabela - Aplicações monolíticas...
Stateless - O servidor não armazena nada. O estado está no cliente(que guarda o token) - APIs...