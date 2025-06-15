import os
import time
import base64
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


# ==============================================================================
# FUNÇÃO PARA CARREGAR DADOS DO ARQUIVO JSON ENTRADAS PARTE 3
# ==============================================================================
def carregar_entradas(nome_arquivo='entradas_parte_3.json'):
   
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            # Carrega o arquivo JSON inteiro, pois ele é dedicado à Parte 3
            dados = json.load(f)
            return dados
    except FileNotFoundError:
        print(f"ERRO: O arquivo de entrada '{nome_arquivo}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"ERRO: O arquivo '{nome_arquivo}' contém um erro de formatação JSON.")
        return None

# =====================================================================================
#   IMPLEMENTAÇÃO DO AES
# =====================================================================================

def aes_encrypt(mode_instance, mensagem, chave):
   
    backend = default_backend()
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    mensagem_bytes = mensagem.encode('utf-8')
    dados_com_padding = padder.update(mensagem_bytes) + padder.finalize()

    cipher = Cipher(algorithms.AES(chave), mode_instance, backend=backend)
    encryptor = cipher.encryptor()
    
    start_time = time.time()
    if isinstance(mode_instance, (modes.ECB, modes.CBC)):
        ct = encryptor.update(dados_com_padding) + encryptor.finalize()
    else: # Modos de fluxo
        ct = encryptor.update(mensagem_bytes) + encryptor.finalize()
    end_time = time.time()

    return ct, end_time - start_time

# =====================================================================================
# BLOCO DE EXECUÇÃO PRINCIPAL 
# =====================================================================================
 
print("### Simulação do AES Real ###\n")

# ----Carrega as configurações do arquivo JSON-----
config = carregar_entradas()

if config:
    # Obtém a mensagem do arquivo
    mensagem_para_cifrar = config['mensagem']

    # Verifica se deve gerar chave/IV aleatórios ou usar os do arquivo
    if config['gerar_chave_e_iv_aleatorios']:
        print("Gerando chave e IV aleatórios...")
        chave_aes = os.urandom(16)
        iv = os.urandom(16)
    else:
        print("Usando chave e IV personalizados do arquivo JSON...")
        chave_aes = bytes.fromhex(config['chave_personalizada_hex'])
        iv = bytes.fromhex(config['iv_personalizado_hex'])

    print(f"Chave AES (Hex): {chave_aes.hex()}")
    print(f"Vetor de Inicialização (IV/Nonce) (Hex): {iv.hex()}")
    print(f"Mensagem: '{mensagem_para_cifrar}'\n")

    # ======================================================================================
    # MODOS DE OPERAÇÕES 
    # ======================================================================================
    modos_para_testar = {
        "ECB": modes.ECB(),
        "CBC": modes.CBC(iv),
        "CFB": modes.CFB(iv),
        "OFB": modes.OFB(iv),
        "CTR": modes.CTR(iv)
    }

    resultados = {}

    for nome, modo in modos_para_testar.items():
        print(f"--- Testando AES no modo {nome} ---")
        
        texto_cifrado, tempo_exec = aes_encrypt(modo, mensagem_para_cifrar, chave_aes)
        
        print(f"Tempo de Execução: {tempo_exec:.6f} segundos")
        print(f"Texto Cifrado (Base64): {base64.b64encode(texto_cifrado).decode('utf-8')}\n")
        resultados[nome] = (tempo_exec, texto_cifrado)

else:
    print("Não foi possível executar a simulação devido a um erro ao carregar as entradas.")
