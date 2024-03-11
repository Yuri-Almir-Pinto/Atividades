def isNum(num: int | float) -> bool:
    return type(num) is int or type(num) is float

def calcular_imc(peso: int | float, altura: int | float) -> int | float | None:
    if isNum(peso) and isNum(altura) and peso > 0 and altura > 0:
        return peso / (altura * altura)

    return None

def descrever_imc(valorIMC: int | float):
    if valorIMC < 18.5:
        return "Magreza"
    elif valorIMC >= 18.5 and valorIMC < 25:
        return "Normal"
    elif valorIMC >= 25 and valorIMC < 30:
        return "Sobrepeso"
    elif valorIMC >= 30 and valorIMC < 35:
        return "Obesidade grau 1"
    elif valorIMC >= 35 and valorIMC < 40:
        return "Obesidade grau 2"
    elif valorIMC >= 40:
        return "Obesidade grau 3"