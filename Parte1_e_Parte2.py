import json
import base64

# ==============================================================================
# FUNÇÃO PARA CARREGAR DADOS DO ARQUIVO JSON
# ==============================================================================
def carregar_entradas(nome_arquivo='Entradas_Parte1_e_Parte2.json'):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            # Retorna apenas a seção relevante para este script
            return dados.get('s_aes')
    except FileNotFoundError:
        print(f"ERRO: O arquivo de entrada '{nome_arquivo}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"ERRO: O arquivo '{nome_arquivo}' contém um erro de formatação JSON.")
        return None

# ==============================================================================
# IMPLEMENTAÇÃO DO S-AES
# ==============================================================================
s_box = [0x9, 0x4, 0xA, 0xB, 0xD, 0x1, 0x8, 0x5, 0x6, 0x2, 0x0, 0x3, 0xC, 0xE, 0xF, 0x7]
mix_matrix = [[1, 4], [4, 1]]

def gmul(a, b):
    p = 0
    for _ in range(4):
        if b & 1:
            p ^= a
        high_bit_set = a & 0b1000
        a <<= 1
        if high_bit_set:
            a ^= 0b10011
        b >>= 1
    return p & 0b1111

def sub_nibbles(state):
    return [[s_box[nibble] for nibble in row] for row in state]

def shift_rows(state):
    return [state[0], [state[1][1], state[1][0]]]

def mix_columns(state):
    new_state = [[0, 0], [0, 0]]
    for c in range(2):
        new_state[0][c] = gmul(mix_matrix[0][0], state[0][c]) ^ gmul(mix_matrix[0][1], state[1][c])
        new_state[1][c] = gmul(mix_matrix[1][0], state[0][c]) ^ gmul(mix_matrix[1][1], state[1][c])
    return new_state

def add_round_key(state, key):
    return [[state[r][c] ^ key[r][c] for c in range(2)] for r in range(2)]

def key_expansion(key):
    r_con1, r_con2 = 0b10000000, 0b00110000
    w = [(key >> 8), key & 0xFF]
    sub_w1 = (s_box[(w[1] & 0xF0) >> 4] << 4) | s_box[w[1] & 0xF]
    w.append(w[0] ^ sub_w1 ^ r_con1)
    w.append(w[2] ^ w[1])
    sub_w3 = (s_box[(w[3] & 0xF0) >> 4] << 4) | s_box[w[3] & 0xF]
    w.append(w[2] ^ sub_w3 ^ r_con2)
    w.append(w[4] ^ w[3])
    return ((w[0] << 8) | w[1]), ((w[2] << 8) | w[3]), ((w[4] << 8) | w[5])

def to_matrix(block):
    return [[(block >> 12) & 0xF, (block >> 8) & 0xF], [(block >> 4) & 0xF, block & 0xF]]

def from_matrix(matrix):
    return (matrix[0][0] << 12) | (matrix[0][1] << 8) | (matrix[1][0] << 4) | matrix[1][1]

def saes_encrypt(plain_text_block, key):
    k0, k1, k2 = key_expansion(key)
    state = add_round_key(to_matrix(plain_text_block), to_matrix(k0))
    print(f"Estado Pré-Rodada: {from_matrix(state):04X}")
    # Rodada 1
    state = sub_nibbles(state); print(f"R1 SubNibbles: {from_matrix(state):04X}")
    state = shift_rows(state); print(f"R1 ShiftRows:  {from_matrix(state):04X}")
    state = mix_columns(state); print(f"R1 MixColumns: {from_matrix(state):04X}")
    state = add_round_key(state, to_matrix(k1)); print(f"R1 AddRoundKey: {from_matrix(state):04X}")
    # Rodada 2
    state = sub_nibbles(state); print(f"R2 SubNibbles: {from_matrix(state):04X}")
    state = shift_rows(state); print(f"R2 ShiftRows:  {from_matrix(state):04X}")
    state = add_round_key(state, to_matrix(k2)); print(f"R2 AddRoundKey: {from_matrix(state):04X}")
    return from_matrix(state)

def encrypt_saes_ecb(texto, chave):
    byte_array = texto.encode('utf-8')
    if len(byte_array) % 2 != 0: byte_array += b'\x00'
    blocos = [int.from_bytes(byte_array[i:i+2], 'big') for i in range(0, len(byte_array), 2)]
    print(f"Blocos originais (Hex): {[f'{b:04X}' for b in blocos]}")
    blocos_cifrados = []
    for i, bloco in enumerate(blocos):
        print(f"\n--- Cifrando Bloco {i+1} ({bloco:04X}) ---")
        blocos_cifrados.append(saes_encrypt(bloco, chave))
    return b''.join([b.to_bytes(2, 'big') for b in blocos_cifrados])

# ==============================================================================
# BLOCO DE EXECUÇÃO PRINCIPAL
# ==============================================================================
if __name__ == "__main__":
    s_aes_config = carregar_entradas()
    if s_aes_config:
        print("### PARTE 1 & 2: S-AES com Modo ECB ###\n")
        mensagem_saes = s_aes_config['mensagem']
        chave_saes = int(s_aes_config['chave_hex'], 16)
        
        print(f"Mensagem de Entrada: '{mensagem_saes}'")
        print(f"Chave (Hex): {s_aes_config['chave_hex']}\n")
        
        cifrado_ecb = encrypt_saes_ecb(mensagem_saes, chave_saes)
        
        print(f"\nSaída Final S-AES (Base64): {base64.b64encode(cifrado_ecb).decode('utf-8')}\n")
