# BHubCase
Esse projeto tem por objetivo criar uma API simplificada de gerenciamento e armazenamento de regras de negócio para um sistema de pagamentos.

## Tecnologias utilizadas:
- Flask
- Python3
- VSCode
- Postman

## Problema

<img width="959" alt="Screenshot 2023-10-03 at 15 05 37" src="https://github.com/mikuIsCoding/BHubCase/assets/146866917/c9435d30-3854-454d-87c7-7fbc78a749e4">


## Solução

![Blank diagram - Page 1 (1)](https://github.com/mikuIsCoding/BHubCase/assets/146866917/dcf6534b-8e54-48cb-8a95-b84c5d8bcabc)

- Rule
  - id
  - rule expression
  - actions
- Produto
  - id
  - name
  - product_type (book, video, membership)
  - product_format (physical, digital) 

- Features desse projeto:
  - Operações báicas de um CRUD
    
- Cenário ideal:
  - Autenticação / Segurança
  - Objetos podem ser de qualquer tipo, não apenas produtos
  - Regras são separadas por área, nesse caso estamos lidando com pagamentos
  - Ações são programadas a parte do sistema de Regras
  - Regras são armazenadas em um banco de dados   

## Entrypoints
- /rules
- /rules/id
- /rules/id/actions

## How to Run

- Install [python3](https://www.python.org/downloads/)
- Install [flask](https://flask.palletsprojects.com/en/3.0.x/)
- In the terminal run the following commands
  - ``` export FLASK_APP=main.py ```
  - ``` flask run ```

## Testes
- Instale o [Postaman](https://www.postman.com/downloads/)
- Consulte todas as regras disponíveis no sistema

<img width="852" alt="Screenshot 2023-10-03 at 15 34 41" src="https://github.com/mikuIsCoding/BHubCase/assets/146866917/d9594800-791e-47d9-8d74-cd2661e359f5">


- Consulte uma regra por id

<img width="855" alt="Screenshot 2023-10-03 at 15 34 58" src="https://github.com/mikuIsCoding/BHubCase/assets/146866917/86cb6073-ed07-4d86-ace4-9e0fb9960825">


- Atualize o conteúdo de uma regra por id

<img width="853" alt="Screenshot 2023-10-03 at 15 35 22" src="https://github.com/mikuIsCoding/BHubCase/assets/146866917/3f28e164-fb51-4cee-853c-831cb68610be">


- Crie uma nova regra
<img width="863" alt="Screenshot 2023-10-03 at 15 38 47" src="https://github.com/mikuIsCoding/BHubCase/assets/146866917/648db26e-20f0-4c2b-a573-a3688b299563">


