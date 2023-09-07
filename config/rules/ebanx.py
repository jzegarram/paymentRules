ebanx_Rule = {
  "id": "ebanx",
  "priority": 3,
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
        "value": 2000
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
    "value": "EBANX"
  }
}