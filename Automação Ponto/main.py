from lib.tratar_txt import arquivo_vazio, buscar_file_path, arquivo_existe
from lib.interface import criar_interface
from lib.automacao import iniciar_automacao

def main():
    caminho = buscar_file_path()
    arquivo_existe(caminho)

    if arquivo_vazio(caminho):
        criar_interface()
    
    iniciar_automacao(caminho)


main()