def notas():
    numeros = input("Digite suas notas: ")
    lista_notas = [float(num) for num in numeros.split()]
    return lista_notas

def resultados(media):
    print(f"A sua média é de: {media}")
