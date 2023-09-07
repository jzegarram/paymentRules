mercadoPago_Rule = {
  "id": "mercado-pago",
  "priority": 1,
  "condition": {
    "type": "GROUP",
    "properties": {
      "conjunction": "AND"
    },
    "children": [
      {
        "type": "RULE",
        "field": "fee",
        "ruleType": "BOOLEAN",
        "value": True
      },
      {
        "type": "RULE",
        "field": "transferAmount",
        "ruleType": "RANGE",
        "operator": "<=",
        "value": 500
      },
      {
        "type": "RULE",
        "field": "speedProcessing",
        "ruleType": "SELECT",
        "value": "Inmediata"
      }
    ]
  },
  "action": {
      "type": "paymentGateway",
      "value": "Mercado Pago"
  }
}