import pytest
from calculadora.operaciones import sumar, restar, multiplicar, dividir


def test_dividir():
    assert dividir(6, 3) == 2

def test_dividir_por_cero():
    with pytest.raises(
        ValueError,match="No se puede dividir entre cero"
        ):
        divide(1, 0)

# Crea el resto de los tests para subir el coverage.