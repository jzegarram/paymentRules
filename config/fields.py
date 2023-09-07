fields = [
    {
        "id": "transferAmount",
        "type": "amount",
        "label": "Ingrese el monto de la transferencia: ",
        "answer": None,
        "indications": "Debe ser un número positivo",
        "validation": "^[1-9][0-9]*(\.[0-9]{1,2})?$"
    },
    {
        "id": "speedProcessing",
        "type": "select",
        "label": "Seleccione la velocidad de procesamiento: ",
        "answer": None,
        "indications": "1 para Inmediata, 2 para 2-4 horas",
        "options": ["Inmediata", "2-4 horas"],
        "validation": "^[1-3]$"
    },
    {
        "id": "fee",
        "type": "boolean",
        "label": "¿Acepta comisión? (si/no): ",
        "answer": None,
        "indications": "Ingrese 'si' o 'no'",
        "validation": "^(si|no)$"
    }
]
