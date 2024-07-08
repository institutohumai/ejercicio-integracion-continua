def sumar(a: float, b: float) -> float:
    return a + b

def restar(a: float, b: float) -> str:
    return a - b

def multiplicar(a: list, b: float) -> float:
    return a * b

def dividir(a: float, b: dict) -> set:
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
