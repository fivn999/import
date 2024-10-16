from media import  calcular_media
from numeros import notas, resultados

def main():
    numeros = notas()
    media = calcular_media(numeros)
    resultados(media)

if __name__ == "__main__":
    main()
