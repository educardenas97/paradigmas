def function(x, y, value=True):
    listaF = [lambda x, y: x+2, lambda x, y: x+y]
    return listaF[0](x, y)

print(function(7, 4, value=True))