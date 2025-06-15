# Trabalho Prático 02: S-AES e AES com Modos de Operação

Este repositório contém a implementação do Trabalho Prático 02 da disciplina de **Segurança Computacional**.

## 📚 Descrição

O projeto é dividido em três partes principais:

- **Implementação do S-AES**  
  Desenvolvimento do algoritmo Simplified Advanced Encryption Standard (S-AES) para fins educacionais.

- **Modo de Operação ECB**  
  Utilização do S-AES implementado para cifrar mensagens no modo Electronic Codebook (ECB) e demonstrar suas vulnerabilidades.

- **Simulação do AES Real**  
  Uso da biblioteca `cryptography` para simular a cifragem com o AES real em diferentes modos de operação (`ECB`, `CBC`, `CFB`, `OFB`, `CTR`) e analisar seus resultados.

## 📁 Estrutura do Projeto

```
Trabalho-2-de-seguranca/
│
├── .venv/                   # Pasta do ambiente virtual Python
├── parte1_e_2_saes.py       # Script para executar as Partes 1 e 2
├── parte3_aes_real.py       # Script para executar a Parte 3
├── entradas.json            # Arquivo de entrada para a Parte 1 e 2
├── entradas_parte3.json     # Arquivo de entrada para a Parte 3
└── README.md                # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- Biblioteca [`cryptography`](https://cryptography.io): Para a simulação do AES real na Parte 3.

## ✅ Pré-requisitos

Antes de executar os scripts, é necessário instalar as dependências do projeto. Recomenda-se o uso de um ambiente virtual (`venv`).

### Criar e ativar ambiente virtual

**Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### Instalar a biblioteca necessária

```bash
pip install cryptography
```

## 🚀 Como Executar

Certifique-se de estar na pasta raiz do projeto (`Trabalho-2-de-seguranca`).

### Parte 1 e 2: S-AES e Modo ECB

Execute o script com:

```bash
python parte1_e_2_saes.py
```

- O script lerá o arquivo `entradas.json`.
- Mostrará no terminal as saídas intermediárias, o resultado final e a demonstração da vulnerabilidade do modo ECB.

### Parte 3: Simulação do AES Real

Execute o script com:

```bash
python parte3.py
```

- O script lerá o arquivo `entradas_parte3.json`.
- Exibirá os resultados da cifragem (tempo de execução e saída em Base64) para cada modo.

## ⚙️ Configuração das Entradas

As mensagens e chaves podem ser modificadas diretamente nos arquivos `.json`:

- Para o **S-AES**: edite o arquivo `entradas.json`.
- Para o **AES Real**: edite o arquivo `entradas_parte3.json`.  
  Você pode definir se deseja gerar chaves e IVs aleatoriamente ou usar valores personalizados.

## 👩‍💻 Autoria

- **Letícia Xavier de Almeida Silva**  
  Matrícula: 190142685

- **Gustavo Vieira do Nascimento**  
  Matrícula: 222012872
