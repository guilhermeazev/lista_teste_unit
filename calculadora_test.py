import calculadora_1

def teste_calculadora():
    resultado = calculadora_1.soma(1, 2)
    assert resultado == 3

def teste_caldora2():
    resultado = calculadora_1.sub(2, 1)
    assert resultado == 1

def teste_caldora3():
    resultado = calculadora_1.mult(1, 2)
    assert resultado == 2

def teste_caldora4():
    resultado = calculadora_1.soma(2, 1)
    assert resultado == 2
 