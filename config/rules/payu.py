payU_Rule = {
  "id": "payu",
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
        "field": "speedProcessing",
        "ruleType": "SELECT",
        "value": "Inmediata"
      }
    ]
  },
  "action": {
    "type": "paymentGateway",
    "value": "PayU"
  }
}
