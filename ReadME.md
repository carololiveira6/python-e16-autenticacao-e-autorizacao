## **Table of Contents**
- [Objetivos da entrega](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5b_e_01_autenticacao.html&ref=master#mcetoc_1f9effaeg0)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5b_e_01_autenticacao.html&ref=master#mcetoc_1f9egmnnd0)
- [Requisitos da v1](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5b_e_01_autenticacao.html&ref=master#mcetoc_1f9effaeg1)
- [Requisitos da v2](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5b_e_01_autenticacao.html&ref=master#mcetoc_1f9effaeg2)
- [Requisitos da v3](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5b_e_01_autenticacao.html&ref=master#mcetoc_1f9effaeg3)
# **Objetivos da entrega**
- Autenticação de páginas com método Basic e Digest
- Proteção de APIs com API Key e JWT
- Refatoração


# **Entregáveis**
Um cadastro de usuários onde o usuário consegue se cadastrar, logar, gerar chaves de acesso à API e utilizar a API para manipular seus dados.



Você vai entregar um repositório contendo uma aplicação em um diretório chamado app.

Esse repositório deve conter pelo menos **3 commits**, cada um indicando cada versão solicitada no seguinte formato: v1 Finalizada, por exemplo. Você pode ter mais commits no repositório se desejar, mas precisa conter um para cada versão finalizada com o nome correto para correção.




# **Requisitos da v1**
- Possuir duas blueprints:  
  - **ADMIN**: url\_prefix='**/admin**'
  - **API**: url\_prefix='**/api**'
- O método de autenticação do **ADMIN** deve ser do tipo **Basic** (pop-up de login).
- Tabela **users** referente a única model (**UserModel**) do projeto, seguindo o seguinte diagrama:

![](Aspose.Words.3efe2b40-6e6b-46b9-8566-f81ba10b9d9f.001.png)



- Tela com formulário para criar conta (usar o jinja para facilitar, rota **API ('/api/signup'))**. Essa tela faz um post para a rota **API ('/api/')** de criação de usuários, a rota de criação **não** deve ser protegida.
- Cadastro de usuários com senha criptografada na rota **'/api/signup'**.
- **APIKey** é gerada no momento da criação do usuário. 
  - **Dica**: Utilize a biblioteca built-in [secrets](https://dev.to/1blademaster/the-python-secrets-module-1c3).
- Um usuário (após logado) ao acessar o **ADMIN** (**'/admin/'**) é retornado um JSON da api\_key do usuário atual.
- Na rota **API** (**'/api/'**), apenas os métodos **PUT,** **DELETE e GET** devem ser protegidos pelo APIKey, utilizando o módulo **HTTPTokenAuth** da biblioteca **Flask-HTTPAuth**. 
  - O usuário consegue editar e acessar somente os seus próprios dados via **API** (**PUT**, **DELETE e GET**).
  - O APIKey deve ser passado pelo header como **Bearer**.
- Rota **GET API** ('**/api/**') deve retornar somente as informações sobre o próprio usuário **EXCETO O SEU PASSWORD**,** baseada no **Bearer Token** do header.


# **Requisitos da v2**
- Alterar o método de autenticação do admin de Basic para Digest.


# **Requisitos da v3**
- Alterar o método de autenticação da API de APIKeys para JWT.
- Remover o módulo admin do sistema, desabilitando o registro da blueprint '**admin\_bp**'. Usando JWT não é mais necessária uma tela para gerar o API Key, por isso vamos desabilita-la.




