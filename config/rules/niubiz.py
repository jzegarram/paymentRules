niubiz_Rule ={
  "id": "niubiz",
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
        "value": False
      },
      {
        "type": "RULE",
        "field": "transferAmount",
        "ruleType": "RANGE",
        "operator": ">=",
        "value": 1000
      }
    ]
  },
  "action": {
      "type": "paymentGateway",
      "value": "Niubiz"
  }
}
