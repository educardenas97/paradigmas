def mostrar_lista(lista, titulo=" ", mostrarNro=True):
    print("\n--------------------------------")
    print("{}".format(titulo))
    item = 1
    for element in lista:
        print("{}- {}".format(item if mostrarNro == True else " ", element))
        item += 1

    print("--------------------------------\n")


def sub_menu(items, titulo=" ", mostrarNro=True):
    print("\n--------------")
    mostrar_lista(items, titulo, mostrarNro)
    print("--------------")
    return int(input("Seleccionar: "))
