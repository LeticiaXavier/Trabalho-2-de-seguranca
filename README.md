Trabalho Prático 02: S-AES e AES com Modos de Operação
Este repositório contém a implementação do Trabalho Prático 02 da disciplina de Segurança Computacional.

O projeto é dividido em três partes principais:

Implementação do S-AES: Desenvolvimento do algoritmo Simplified Advanced Encryption Standard (S-AES) para fins educacionais.

Modo de Operação ECB: Utilização do S-AES implementado para cifrar mensagens no modo Electronic Codebook (ECB) e demonstrar suas vulnerabilidades.

Simulação do AES Real: Uso da biblioteca cryptography para simular a cifragem com o AES real em diferentes modos de operação (ECB, CBC, CFB, OFB, CTR) e analisar seus resultados.

Estrutura do Projeto
O projeto está organizado da seguinte forma para facilitar a execução e a correção:

Trabalho-2-de-seguranca/
│
├── .venv/                   # Pasta do ambiente virtual Python
├── parte1_e_2_saes.py       # Script para executar as Partes 1 e 2
├── parte3_aes_real.py       # Script para executar a Parte 3
├── entradas.json            # Arquivo de entrada para a Parte 1 e 2
├── entradas_parte3.json     # Arquivo de entrada para a Parte 3
└── README.md                # Este arquivo

Tecnologias Utilizadas
Python 3.11+

Biblioteca cryptography: Para a simulação do AES real na Parte 3.

Pré-requisitos
Antes de executar os scripts, é necessário instalar as dependências do projeto. É recomendado o uso de um ambiente virtual (venv).

Crie e ative um ambiente virtual (opcional, mas recomendado):

# No Windows
python -m venv .venv
.\.venv\Scripts\activate

Instale a biblioteca cryptography:

pip install cryptography

Como Executar
Cada parte do trabalho pode ser executada de forma independente. Certifique-se de que o terminal esteja na pasta raiz do projeto (Trabalho-2-de-seguranca).

Parte 1 e 2: S-AES e Modo ECB
Para executar a implementação do S-AES, utilize o seguinte comando:

python parte1_e_2_saes.py

O script lerá as configurações do arquivo entradas.json e exibirá no terminal todas as saídas intermediárias, o resultado final e a demonstração da vulnerabilidade do modo ECB.

Parte 3: Simulação do AES Real
Para executar a simulação dos modos de operação do AES, utilize o comando:

python parte3_aes_real.py

O script lerá as configurações do arquivo entradas_parte3.json e exibirá no terminal os resultados da cifragem (tempo de execução e saída em Base64) para cada modo.

Configuração das Entradas
As mensagens e chaves utilizadas nos scripts podem ser facilmente modificadas editando os arquivos JSON correspondentes, sem a necessidade de alterar o código Python.

Para o S-AES: Modifique o arquivo entradas.json.

Para o AES Real: Modifique o arquivo entradas_parte3.json. Você pode alterar a mensagem e decidir se deseja gerar chaves/IVs aleatórios ou usar valores personalizados.

Autorias
Nome: [Letícia Xavier de Almeida Silva]
Matrícula: [190142685]
Nome: [Gustavo Vieira do Nascimento]
Matícula: [222012872]
