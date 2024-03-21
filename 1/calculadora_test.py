import lista_unitario_test

def teste_calculadora():
    resultado = lista_unitario_test.soma(1, 2)
    assert resultado == 3

def teste_caldora2():
    resultado = lista_unitario_test.sub(2, 1)
    assert resultado == 1

def teste_caldora3():
    resultado = lista_unitario_test.mult(1, 2)
    assert resultado == 2

def teste_caldora4():
    resultado = lista_unitario_test.soma(2, 1)
    assert resultado == 2
 