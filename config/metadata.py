actionTypes = {
    "paymentGateway": "Pasarela de Pago"
}

fieldTypes = {
    "BOOLEAN": "Verdadero/falso",
    "SELECT": "Opcion Multiple",
    "RANGE": "Rango"
}

operators = {
    "==": lambda x, y: x == y,
    "<": lambda x, y: x < y,
    "<=": lambda x, y: x <= y,
    ">": lambda x, y: x > y,
    ">=": lambda x, y: x >= y
}