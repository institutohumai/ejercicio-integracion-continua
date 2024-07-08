import pytest
from calculadora.operaciones import sumar, restar, multiplicar, dividir


def test_dividir_por_cero():
    with pytest.raises(
        ValueError,match="No se puede dividir entre cero"
        ):
        dividir(1, 0)

# Crea el resto de los tests para subir el coverage.