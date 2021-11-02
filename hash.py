import os
from Crypto.Hash import SHA256


FILE_NAME = "exemplo2.mp4"
BLOCK_SIZE = 1024

def main():
    file_path = 'videos/' + FILE_NAME

    # Retorna array com:
    # [0] Hash do último bloco
    # [1] Tamanho do último bloco
    print('--- Calculating hash')
    results = execute(file_path)
    last_block_hash = results[0]
    last_block_size = results[1]
    last_block_hash_hex = last_block_hash.hex()
    print('--- Finished calculating hash')

    print('--- Last block size: ' + str(last_block_size))
    print('--- Last block hash: ' + last_block_hash_hex)


def execute(file_path):
    size = os.path.getsize(file_path)
    last_block_size = size % BLOCK_SIZE
    result = ''
    
    with open(file_path,'rb') as video:
        
        # Laço para calcular hash
        # Posição inicial ajustada de acordo com tamanho ultimo bloco
        position = size - last_block_size
        while position >= 0:
            # Carrega bloco do video
            video.seek(position)
            block_info = video.read(BLOCK_SIZE)
            
            # Utiliza a biblioteca para calcular hash
            sha256 = SHA256.new()
            sha256.update(block_info)
            if(result): sha256.update(result)
            result = sha256.digest()
        
            # Recalcula posição a cada fim de iteração do laço, para bloco anterior
            position = position - BLOCK_SIZE

        video.close()

    # Retorna hash e tamanho do último bloco        
    return [result, last_block_size]


if __name__ == "__main__":
    main()
