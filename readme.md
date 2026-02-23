# Backend Portal ST

Bem-vindo ao repositório do **Backend Portal ST**. Este projeto consiste
numa API estruturada em Python e HTML.
Teste Técnico da Super Terminais

------------------------------------------------------------------------

## 📁 Estrutura do Projeto

O código-fonte está centralizado no diretório `src/` e segue a seguinte
organização:

-   **`src/models/`**: Entidades e modelos de base de dados.
-   **`src/repositories/`**: Lógica de acesso e persistência de dados.
-   **`src/routers/`**: Definição dos endpoints da API (rotas).
-   **`src/schemas/`**: Validação e serialização de dados de entrada e
    saída.
-   **`src/security/`**: Regras de autenticação, autorização e segurança
    da aplicação.
-   **`src/static/`**: Ficheiros estáticos.
-   **`src/temp_files/`**: Gestão de ficheiros temporários.

------------------------------------------------------------------------

## 📊 Diagramas do Sistema

Abaixo encontram-se as documentações visuais que detalham o
comportamento e a arquitetura do sistema:

### Diagrama de Caso de Uso

![Caso de Uso](Caso%20de%20Uso.png)

### Diagrama de Atividade

![Diagrama de Atividade](Diagrama%20de%20Atividade.png)

### Diagrama de Classe

![Diagrama de Classe](Diagrama%20de%20Classe.jpg)

------------------------------------------------------------------------

## 🚀 Passo a Passo para Executar o Sistema

Para colocar o sistema a funcionar corretamente, certifique-se de que
tem o **Docker** e o **Docker Compose** instalados na sua máquina. O
processo de inicialização deve seguir a ordem exata abaixo:


Na raiz do projeto, execute:

``` bash
cd src
```
### 1. Construir as imagens do Docker

``` bash
docker compose build
```

### 2. Levantar os contentores

``` bash
docker compose up
```

### 3. Entrar no container do backend

``` bash
docker exec -ti backend_portal_st sh
```

### 4. Popular a base de dados

``` bash
python populate.py
```

------------------------------------------------------------------------

**⚠️ Nota Importante:**\
Não se esqueça de configurar as suas variáveis de ambiente. Copie o
arquivo `.env.example` para `.env` e ajuste as credenciais necessárias
antes de iniciar o projeto.

### Users default

Para uso interno
```bash
login: admin
senha: admin
```

Para uso externo
```bash
login: external
senha: external
```

A Parte dois do desafio está localizado dentro da pasta **queries** onde cada número corresponde a sua letra
