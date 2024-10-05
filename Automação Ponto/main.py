from lib.tratar_env import arquivo_vazio, buscar_file_path, criar_arquivo
from lib.interface import criar_interface
from lib.automacao import iniciar_automacao

def main():
    caminho = buscar_file_path()
    criar_arquivo(caminho)

    if arquivo_vazio(caminho):
        criar_interface()
    
    iniciar_automacao()


main()
