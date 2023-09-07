culqi_Rule = {
  "id": "culqi",
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
        "operator": ">=",
        "value": 100
      }
    ]
  },
  "action": {
    "type": "paymentGateway",
    "value": "Culqi"
  }
}
