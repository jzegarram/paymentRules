pagoEfectivo_Rule = {
  "id": "pago-efectivo",
  "priority": 2,
  "condition": {
    "type": "GROUP",
    "properties": {
      "conjunction": "OR"
    },
    "children": [
      {
        "type": "RULE",
        "field": "fee",
        "ruleType": "BOOLEAN",
        "value": False
      },
      {
        "type": "RULE",
        "field": "transferAmount",
        "ruleType": "RANGE",
        "operator": ">=",
        "value": 0
      },
      {
        "type": "RULE",
        "field": "speedProcessing",
        "ruleType": "SELECT",
        "value": "2-4 horas"
      }
    ]
  },
  "action": {
    "type": "paymentGateway",
    "value": "Pago Efectivo"
  }
}
